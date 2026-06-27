# ops/quality_control.md
Skill ID: ops-qc-05
Category: Operations
Agent: O-01, MGR-OPS
Difficulty: Intermediate

## Definition
Systematic processes to ensure products/services meet defined quality standards consistently, with tools to detect, report, and correct deviations.

## Framework
1. **Define quality standard**: What does "done" mean?
2. **Measure**: qc checklist per process
3. **Analyze**: Defect categorization (type, severity, frequency)
4. **Improve**: Root cause fixes, not band-aids
5. **Control**: Automated checks, periodic audits

## QC Checklist Template
| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| Output matches spec | [ ] | |
| No errors/warnings in logs | [ ] | |
| Within acceptable tolerance | [ ] | |
| Approval signatures present | [ ] | |

## Defect Response
- Critical (<1% of output): Stop line, root cause, fix, restart
- Major (1-5%): Hold batch, review, decide
- Minor (>5%): Log, trend weekly, improve process

## KPIs
- Defective rate: < 2%
- First-pass yield: 95%+
- Cost of quality: < 5% of revenue
- Customer complaints about quality: 0 per month
