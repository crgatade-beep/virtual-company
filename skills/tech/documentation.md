# tech/documentation.md
Skill ID: tech-docs-08
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Intermediate

## Definition
Creating, maintaining, and delivering clear, accurate technical documentation that enables onboarding, reduces support burden, and preserves institutional knowledge.

## Documentation Types
1. **ADRs (Architecture Decision Records)**: Why decisions were made
2. **RUNBOOKS**: Step-by-step operational procedures
3. **API docs**: Endpoint reference, examples, error codes
4. **README**: What, why, how to start
5. **Incident post-mortems**: Learnings, not blame

## Writing Standards
- Single source of truth (no outdated copies)
- Code examples are executable (copy-paste runs)
- Version-tagged (docs v2.1.0 for API v2)
- Last-updated date on every doc
- Diagrams for complex flows (Mermaid, Excalidraw)

## ADR Template
```
# ADR-001: [Title]
Date: YYYY-MM-DD
Status: Accepted | Deprecated | Superseded

## Context
Why are we making this decision?

## Options Considered
1. Option A: ...
2. Option B: ...
3. Option C: ...

## Decision
We chose X because [data/evidence].

## Consequences
Positive: ...
Negative: ...
Mitigations: ...
```

## KPIs
- Documentation coverage for critical systems: 100%
- Onboarding time reduction: 40%+
- Support tickets from "how do I": < 5%
