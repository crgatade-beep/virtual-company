#!/usr/bin/env python3
"""VirtualCompany local orchestrator.
Usage:
  python main.py tree
  python main.py agents
  python main.py tasks list
  python main.py tasks add <ASSIGNED_TO> <description>
  python main.py tasks approve <TASK_ID>
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent
COMPANY_DIR = BASE_DIR / "company"
ROLES_DIR = BASE_DIR / "roles"
TASKS_DIR = BASE_DIR / "tasks"
LOGS_DIR = BASE_DIR / "logs"
BUDGETS_DIR = BASE_DIR / "budgets"


@dataclass(frozen=True)
class Agent:
    id: str
    name: str
    department: str
    role_file: Path


@dataclass(frozen=True)
class Task:
    id: str
    assigned_to: str
    description: str
    approved: bool = False


def bootstrap() -> None:
    for path in [COMPANY_DIR, ROLES_DIR, TASKS_DIR, LOGS_DIR, BUDGETS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def load_agents() -> List[Agent]:
    agents: List[Agent] = []
    for dept_dir in sorted(ROLES_DIR.iterdir()):
        if not dept_dir.is_dir():
            continue
        department = dept_dir.name
        for role_file in sorted(dept_dir.glob("*.md")):
            agent_id = role_file.stem.upper()
            name = role_file.stem.upper()
            agents.append(
                Agent(
                    id=agent_id,
                    name=name,
                    department=department,
                    role_file=role_file,
                )
            )
    return agents


def _task_file() -> Path:
    return TASKS_DIR / "tasks.json"


def load_tasks() -> List[Task]:
    tasks: List[Task] = []
    task_file = _task_file()
    if not task_file.exists():
        return tasks
    try:
        data = json.loads(task_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return tasks
    for item in data:
        tasks.append(
            Task(
                id=item["id"],
                assigned_to=item["assigned_to"],
                description=item["description"],
                approved=bool(item.get("approved")),
            )
        )
    return tasks


def save_tasks(tasks: List[Task]) -> None:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    payload = [
        {
            "id": task.id,
            "assigned_to": task.assigned_to,
            "description": task.description,
            "approved": task.approved,
        }
        for task in tasks
    ]
    _task_file().write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def company_tree() -> Dict[str, Dict]:
    tree: Dict[str, Dict] = {}
    for path in sorted(ROLES_DIR.glob("*/*.md")):
        dept = path.parts[-2]
        agent_id = path.stem.upper()
        tree.setdefault(dept, {})[agent_id] = {
            "role_file": str(path),
        }
    return tree


def main() -> int:
    bootstrap()
    args = sys.argv[1:]
    if not args:
        print("Usage: python main.py <tree|agents|tasks>")
        return 0

    command = args[0].lower()

    if command == "tree":
        print(json.dumps(company_tree(), indent=2, ensure_ascii=False))
    elif command == "agents":
        agents = load_agents()
        print(json.dumps([agent.__dict__ for agent in agents], indent=2, ensure_ascii=False, default=str))
    elif command == "tasks":
        if len(args) == 1:
            print("Usage: python main.py tasks <list|add|approve> ...")
            return 1
        mode = args[1].lower()
        tasks = load_tasks()
        if mode == "list":
            print(json.dumps([task.__dict__ for task in tasks], indent=2, ensure_ascii=False))
        elif mode == "add":
            if len(args) < 4:
                print("Usage: python main.py tasks add <ASSIGNED_TO> <description>")
                return 1
            assigned_to = args[2].upper()
            description = " ".join(args[3:])
            task_id = f"T{len(tasks)+1:03d}"
            tasks.append(
                Task(
                    id=task_id,
                    assigned_to=assigned_to,
                    description=description,
                    approved=False,
                )
            )
            save_tasks(tasks)
            print(f"added {task_id} -> {assigned_to}")
        elif mode == "approve":
            if len(args) < 3:
                print("Usage: python main.py tasks approve <TASK_ID>")
                return 1
            task_id = args[2].upper()
            found = False
            for task in tasks:
                if task.id == task_id:
                    task.approved = True
                    found = True
            if not found:
                print(f"task {task_id} not found")
                return 1
            save_tasks(tasks)
            print(f"approved {task_id}")
        else:
            print("unknown tasks mode")
            return 1
    else:
        print(f"unknown command: {command}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
