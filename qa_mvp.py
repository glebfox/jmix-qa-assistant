#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
KNOWLEDGE_DIR = ROOT / "knowledge"


@dataclass
class KnowledgeModule:
    id: str
    title: str
    applies_to: set[str]
    triggers: list[str]
    always: bool
    path: Path
    questions: list[str] = field(default_factory=list)
    checklist: OrderedDict[str, list[str]] = field(default_factory=OrderedDict)
    risks: list[str] = field(default_factory=list)


@dataclass
class TaskInput:
    title: str
    task_type: str
    labels: list[str]
    description: str
    acceptance_criteria: list[str]
    changed_areas: list[str]
    known_risks: list[str]
    context: str
    raw_text: str


def parse_key_value_block(lines: list[str]) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip().lower()] = value.strip()
    return data


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("Knowledge file must start with front matter")

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise ValueError("Knowledge file front matter is not closed")

    metadata = parse_key_value_block(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :]).strip()
    return metadata, body


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def split_csv(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def parse_knowledge_body(body: str) -> tuple[list[str], OrderedDict[str, list[str]], list[str]]:
    questions: list[str] = []
    checklist: OrderedDict[str, list[str]] = OrderedDict()
    risks: list[str] = []
    current_section = ""
    current_group = "General"

    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("## "):
            current_section = line[3:].strip().lower()
            current_group = "General"
            continue
        if line.startswith("### "):
            current_group = line[4:].strip()
            checklist.setdefault(current_group, [])
            continue
        if line.startswith("- "):
            item = line[2:].strip()
            if current_section == "questions":
                questions.append(item)
            elif current_section == "risks":
                risks.append(item)
            elif current_section == "checklist":
                checklist.setdefault(current_group, []).append(item)

    return questions, checklist, risks


def load_knowledge_modules(knowledge_dir: Path) -> list[KnowledgeModule]:
    modules: list[KnowledgeModule] = []
    for path in sorted(knowledge_dir.rglob("*.md")):
        metadata, body = parse_front_matter(path.read_text(encoding="utf-8"))
        questions, checklist, risks = parse_knowledge_body(body)
        modules.append(
            KnowledgeModule(
                id=metadata["id"],
                title=metadata["title"],
                applies_to=set(split_csv(metadata.get("applies_to", "all"))),
                triggers=[value.lower() for value in split_csv(metadata.get("triggers", ""))],
                always=metadata.get("always", "false").lower() == "true",
                path=path,
                questions=questions,
                checklist=checklist,
                risks=risks,
            )
        )
    return modules


def parse_markdown_sections(text: str) -> tuple[dict[str, str], dict[str, list[str] | str]]:
    lines = text.splitlines()
    header_lines: list[str] = []
    sections: OrderedDict[str, list[str]] = OrderedDict()
    current_section: str | None = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith("## "):
            current_section = line[3:].strip().lower()
            sections[current_section] = []
            continue
        if current_section is None:
            header_lines.append(line)
        else:
            sections[current_section].append(line)

    header = parse_key_value_block(header_lines)
    parsed_sections: dict[str, list[str] | str] = {}
    for name, section_lines in sections.items():
        cleaned_lines = [line for line in section_lines if line.strip()]
        bullets = [line[2:].strip() for line in cleaned_lines if line.strip().startswith("- ")]
        if bullets and len(bullets) == len(cleaned_lines):
            parsed_sections[name] = bullets
        else:
            parsed_sections[name] = "\n".join(cleaned_lines).strip()
    return header, parsed_sections


def parse_task(path: Path) -> TaskInput:
    text = path.read_text(encoding="utf-8")
    header, sections = parse_markdown_sections(text)
    return TaskInput(
        title=header.get("title", "Untitled task"),
        task_type=header.get("type", "feature").strip().lower(),
        labels=split_csv(header.get("labels", "")),
        description=str(sections.get("description", "")).strip(),
        acceptance_criteria=list(sections.get("acceptance criteria", []))
        if isinstance(sections.get("acceptance criteria", []), list)
        else [],
        changed_areas=list(sections.get("changed areas", []))
        if isinstance(sections.get("changed areas", []), list)
        else [],
        known_risks=list(sections.get("known risks", []))
        if isinstance(sections.get("known risks", []), list)
        else [],
        context=str(sections.get("context", "")).strip(),
        raw_text=text,
    )


def read_optional_text(path: Path | None) -> str:
    if path is None:
        return ""
    text = path.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    if lines and lines[0].strip().startswith("# "):
        return "\n".join(lines[1:]).strip()
    return text


def task_search_blob(task: TaskInput) -> str:
    parts = [
        task.title,
        task.task_type,
        ", ".join(task.labels),
        task.description,
        "\n".join(task.acceptance_criteria),
        "\n".join(task.changed_areas),
        "\n".join(task.known_risks),
        task.context,
    ]
    return normalize_text("\n".join(parts))


def select_modules(task: TaskInput, modules: Iterable[KnowledgeModule]) -> list[tuple[KnowledgeModule, list[str]]]:
    search_blob = task_search_blob(task)
    selected: list[tuple[KnowledgeModule, list[str]]] = []

    for module in modules:
        if "all" not in module.applies_to and task.task_type not in module.applies_to:
            continue

        matched_triggers = [trigger for trigger in module.triggers if trigger in search_blob]
        if module.always or matched_triggers:
            reasons = ["always included"] if module.always else [f"matched: {', '.join(matched_triggers[:4])}"]
            selected.append((module, reasons))

    return selected


def unique_keep_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        key = normalize_text(item)
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def generate_questions(task: TaskInput, selected_modules: list[tuple[KnowledgeModule, list[str]]]) -> list[str]:
    questions: list[str] = []

    if not task.acceptance_criteria:
        questions.append("Which acceptance criteria are mandatory for this task?")
    if not task.changed_areas:
        questions.append("Which areas are actually affected by this change: UI, data, security, API, configuration?")
    if "security" not in task_search_blob(task):
        questions.append("Does this task change roles, permissions, or action visibility?")
    if not task.context:
        questions.append("Are there important browser, database, configuration, or feature-flag constraints?")

    for module, _ in selected_modules:
        questions.extend(module.questions)

    return unique_keep_order(questions)


def build_acceptance_section(task: TaskInput) -> OrderedDict[str, list[str]]:
    checklist: OrderedDict[str, list[str]] = OrderedDict()
    if task.acceptance_criteria:
        checklist["Acceptance Criteria Coverage"] = [
            f"Verify criterion: {criterion}" for criterion in task.acceptance_criteria
        ]
    if task.known_risks:
        checklist["Task-Specific Risks"] = [
            f"Explicitly test risk: {risk}" for risk in task.known_risks
        ]
    return checklist


def merge_checklists(
    task: TaskInput, selected_modules: list[tuple[KnowledgeModule, list[str]]]
) -> tuple[OrderedDict[str, list[str]], list[str]]:
    merged: OrderedDict[str, list[str]] = build_acceptance_section(task)
    risks: list[str] = []

    for module, _ in selected_modules:
        for section, items in module.checklist.items():
            merged.setdefault(section, [])
            merged[section].extend(items)
        risks.extend(module.risks)

    for section, items in list(merged.items()):
        merged[section] = unique_keep_order(items)

    if "Acceptance Criteria Coverage" in merged and "Acceptance Coverage" in merged:
        del merged["Acceptance Coverage"]

    return merged, unique_keep_order(risks + task.known_risks)


def render_questions(task: TaskInput, selected_modules: list[tuple[KnowledgeModule, list[str]]]) -> str:
    lines = [
        "# Clarifying Questions",
        "",
        f"Task: {task.title}",
        f"Type: {task.task_type}",
        "",
        "## Selected Knowledge Modules",
    ]

    for module, reasons in selected_modules:
        lines.append(f"- {module.title} (`{module.id}`) — {', '.join(reasons)}")

    lines.append("")
    lines.append("## Questions")
    for question in generate_questions(task, selected_modules):
        lines.append(f"- {question}")

    return "\n".join(lines).strip() + "\n"


def render_checklist(
    task: TaskInput,
    selected_modules: list[tuple[KnowledgeModule, list[str]]],
    answers_text: str,
) -> str:
    checklist, risks = merge_checklists(task, selected_modules)
    lines = [
        "# QA Checklist Draft",
        "",
        "## Task Summary",
        f"- Title: {task.title}",
        f"- Type: {task.task_type}",
        f"- Labels: {', '.join(task.labels) if task.labels else 'n/a'}",
        f"- Changed areas: {', '.join(task.changed_areas) if task.changed_areas else 'n/a'}",
        "",
        "## Applied Knowledge Modules",
    ]

    for module, reasons in selected_modules:
        lines.append(f"- {module.title} (`{module.id}`) — {', '.join(reasons)}")

    lines.extend(["", "## Clarifications"])
    if answers_text:
        lines.append(answers_text)
    else:
        lines.append("- No additional answers were provided. Use the open questions from `ask` mode if the scope is still fuzzy.")

    lines.extend(["", "## Checklist"])
    for section, items in checklist.items():
        if not items:
            continue
        lines.append(f"### {section}")
        for item in items:
            lines.append(f"- [ ] {item}")
        lines.append("")

    if risks:
        lines.append("## Focus Areas")
        for risk in risks:
            lines.append(f"- {risk}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_output(text: str, out_path: Path | None) -> None:
    if out_path is None:
        sys.stdout.write(text)
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate clarifying questions and QA checklist drafts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ask_parser = subparsers.add_parser("ask", help="Generate clarifying questions for a task")
    ask_parser.add_argument("task", type=Path, help="Path to task markdown")
    ask_parser.add_argument("--out", type=Path, help="Optional output file path")

    generate_parser = subparsers.add_parser("generate", help="Generate checklist draft for a task")
    generate_parser.add_argument("task", type=Path, help="Path to task markdown")
    generate_parser.add_argument("--answers", type=Path, help="Optional answers markdown")
    generate_parser.add_argument("--out", type=Path, help="Optional output file path")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    task = parse_task(args.task)
    modules = load_knowledge_modules(KNOWLEDGE_DIR)
    selected_modules = select_modules(task, modules)

    if args.command == "ask":
        write_output(render_questions(task, selected_modules), args.out)
        return 0

    if args.command == "generate":
        write_output(render_checklist(task, selected_modules, read_optional_text(args.answers)), args.out)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
