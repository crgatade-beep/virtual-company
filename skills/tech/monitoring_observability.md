# tech/monitoring_observability.md
Skill ID: tech-monitoring-09
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Advanced

## Definition
Continuous visibility into system health, performance, and behavior through metrics, logs, and traces to detect and diagnose issues before they become incidents.

## Three Pillars
1. **Metrics**: Numeric measurements (CPU, latency, error rate)
2. **Logs**: Discrete event records (request logs, error traces)
3. **Traces**: End-to-end request journey across services

## Monitoring Tiers
- **L1 (Alert)**: Pages on-call, immediate action needed
- **L2 (Awareness)**: Dashboard, track trends
- **L3 (Investigation)**: Deep dive, debug specific issue
- **L4 (Business)**: Revenue impact, customer experience

## Alert Design Principles
- Alert on customer impact, not internal metrics
- Every alert needs: title, severity, runbook link, owner
- Quiet hours enforced for non-SEV1
- Escalation: 5 min → 10 min → escalate to tech lead

## Golden Signals (Google SRE)
1. **Latency**: Time to serve request
2. **Traffic**: Requests per second
3. **Errors**: Rate of failed requests
4. **Saturation**: Capacity utilization (CPU, memory, disk)

## Error Budgets
- Budget = 100% - SLO (e.g., 99.9% uptime → 43.2 min/month budget)
- Spend budget on risky features, otherwise stable branch is priority

## KPIs
- Alert-to-resolution time: < 30 min for SEV1
- False positive rate: < 10%
- Dashboard coverage: All critical services
- On-call burnout score: < 20% weekends
