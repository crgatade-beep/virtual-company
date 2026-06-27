#!/usr/bin/env python3
"""VirtualCompany — lightweight simulated company runtime.

This runs the CEO/manager/employee workflow locally.
No CrewAI runtime is used to avoid env conflicts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROLES_DIR = BASE_DIR / "roles"
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

COMPANY = {
    "CEO-01": {
        "reports_to": "Owner",
        "manages": ["MGR-SALES", "MGR-OPS", "MGR-TECH"],
        "role_file": str(ROLES_DIR / "ceo/ceo.md"),
    },
    "MGR-SALES": {
        "reports_to": "CEO-01",
        "manages": ["S-01", "S-02"],
        "role_file": str(ROLES_DIR / "managers/sales.md"),
    },
    "MGR-OPS": {
        "reports_to": "CEO-01",
        "manages": ["O-01"],
        "role_file": str(ROLES_DIR / "managers/ops.md"),
    },
    "MGR-TECH": {
        "reports_to": "CEO-01",
        "manages": ["T-01"],
        "role_file": str(ROLES_DIR / "managers/tech.md"),
    },
    "S-01": {"reports_to": "MGR-SALES", "manages": [], "role_file": str(ROLES_DIR / "sales/s01.md")},
    "S-02": {"reports_to": "MGR-SALES", "manages": [], "role_file": str(ROLES_DIR / "sales/s02.md")},
    "O-01": {"reports_to": "MGR-OPS", "manages": [], "role_file": str(ROLES_DIR / "ops/o01.md")},
    "T-01": {"reports_to": "MGR-TECH", "manages": [], "role_file": str(ROLES_DIR / "tech/t01.md")},
}


def print_org() -> None:
    print("CEO-01")
    for mgr in ["MGR-SALES", "MGR-OPS", "MGR-TECH"]:
        print(f"  {mgr}")
        for emp in COMPANY[mgr]["manages"]:
            print(f"    {emp}")


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] == "tree":
        print(json.dumps(COMPANY, indent=2, ensure_ascii=False))
        return 0
    if args[0] == "org":
        print_org()
        return 0
    if args[0] == "workflow":
        print("workflow started")
        print("CEO-01: assign goals to managers")
        print("MGR-SALES / MGR-OPS / MGR-TECH: create task plans")
        print("Employees: execute assigned tasks")
        print("CE-01: review everything")
        print("workflow complete")
        return 0
    print("Usage: python company_sim.py <tree|org|workflow>")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
