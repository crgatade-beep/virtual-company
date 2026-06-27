#!/usr/bin/env python3
"""VirtualCompany — simplified CrewAI runtime without file-package coupling."""
from __future__ import annotations

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROLES_DIR = BASE_DIR / "roles"

os.environ.setdefault("OPENAI_API_KEY", "ollama")
os.environ.setdefault("OPENAI_BASE_URL", "http://localhost:11434/v1")

from crewai import Agent, Crew, Process, Task
from langchain_ollama import OllamaLLM

LLM = OllamaLLM(model="deepseek-r1:1.5b", temperature=0.7)


def _read(rel: str) -> str:
    path = ROLES_DIR / rel
    return path.read_text(encoding="utf-8") if path.exists() else rel


def make_agents() -> dict[str, Agent]:
    return {
        "CEO-01": Agent(
            role="Chief Strategist",
            goal="Oversee all departments and convert company goals into clear manager tasks.",
            backstory=_read("ceo/ceo.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=True,
        ),
        "MGR-SALES": Agent(
            role="Sales Manager",
            goal="Align sales team to revenue targets and remove blockers.",
            backstory=_read("managers/sales.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "MGR-OPS": Agent(
            role="Operations Manager",
            goal="Keep delivery, finance and logistics smooth and low-cost.",
            backstory=_read("managers/ops.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "MGR-TECH": Agent(
            role="Technology Manager",
            goal="Run stable, scalable tech with tight budgets.",
            backstory=_read("managers/tech.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "S-01": Agent(
            role="Sales Executive",
            goal="Generate leads and follow up fast.",
            backstory=_read("sales/s01.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "S-02": Agent(
            role="Sales Executive",
            goal="Close small deals and collect feedback.",
            backstory=_read("sales/s02.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "O-01": Agent(
            role="Operations Executive",
            goal="Execute SOPs and report exceptions.",
            backstory=_read("ops/o01.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
        "T-01": Agent(
            role="Tech Executive",
            goal="Ship small fixes and keep infra healthy.",
            backstory=_read("tech/t01.md"),
            llm=LLM,
            verbose=False,
            allow_delegation=False,
        ),
    }


def make_tasks(agents: dict[str, Agent]) -> list[Task]:
    return [
        Task(
            description="CEO-01: Turn company goal 'increase revenue 20%' into 3 concrete manager tasks for Sales, Ops and Tech.",
            agent=agents["CEO-01"],
            expected_output="3 bullet tasks, each tagged with manager id.",
        ),
        Task(
            description="MGR-SALES: Draft a 5-step outbound sales plan for S-01 and S-02.",
            agent=agents["MGR-SALES"],
            expected_output="Numbered sales plan with owner per step.",
        ),
        Task(
            description="S-01: List 10 cold outreach subjects for Indian SaaS founders.",
            agent=agents["S-01"],
            expected_output="Plain numbered list of subject lines.",
        ),
        Task(
            description="O-01: Summarize 3 process risks hurting delivery speed.",
            agent=agents["O-01"],
            expected_output="Risk, impact, one-line fix per item.",
        ),
        Task(
            description="T-01: Propose 3 low-cost infra changes to save monthly cloud spend.",
            agent=agents["T-01"],
            expected_output="Short suggestion list with estimated saving.",
        ),
    ]


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "tree":
        sys.path.insert(0, str(BASE_DIR))
        try:
            from company.main import company_tree
            import json
            print(json.dumps(company_tree(), indent=2, ensure_ascii=False))
        except Exception as exc:
            print(f"tree failed: {exc}")
            return 1
        return 0

    print("Loading agents...")
    agents = make_agents()
    print(f"Loaded {len(agents)} agents.")

    tasks = make_tasks(agents)
    print(f"Prepared {len(tasks)} tasks.")

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=False,
    )
    print("\n=== Crew run starting ===\n")
    result = crew.kickoff()
    print("\n=== Crew run finished ===\n")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
