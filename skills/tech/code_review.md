# tech/code_review.md
Skill ID: tech-codereview-03
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Intermediate

## Definition
Systematic examination of code changes by peers before merge to catch bugs, ensure quality, share knowledge, and maintain consistency.

## What to Review
- Logic and correctness
- Security (injection, auth, data exposure)
- Performance (N+1 queries, unnecessary loops, memory leaks)
- Readability (naming, structure, comments)
- Tests (coverage, edge cases, quality)
- Breaking changes and migration path

## Review Guidelines
- Review within 4 business hours
- Max 400 lines per review request
- Title: [Type] Brief description (e.g., [FEAT] User search autocomplete)
- Approval required: 1 senior, 1 peer
- Critical path changes: 2 seniors + tech lead

## Comment Standards
```
🔴 MUST FIX: Blocks merge
🟡 SHOULD FIX: Important, not blocking
🟢 NIT: Nice to have
💡 SUGGEST: Alternative idea
❓ QUESTION: Need clarification
✅ PRAISE: Good call, call this out
```

## Prohibited
- "LGTM" without reading changes
- Reviewing own PRs to main
- Nitpicking formatting (use linter instead)
- Blocking on personal preference

## KPIs
- PR review time: < 4 hours
- First-pass approval rate: 70%+
- Post-merge bugs from PRs: < 2%
- Review coverage: 100% of PRs
