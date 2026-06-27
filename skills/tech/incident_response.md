# tech/incident_response.md
Skill ID: tech-incident-01
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Expert

## Definition
Structured methodology for detecting, containing, eradicating, recovering from, and learning from technical incidents (outages, breaches, failures).

## Severity Levels
- **SEV1**: Total outage, all users affected, revenue impact > $100K/hr
- **SEV2**: Major degradation, subset affected, revenue impact > $10K/hr
- **SEV3**: Minor issue, workaround exists, no revenue impact
- **SEV4**: Cosmetic or low-priority bug

## Response Timeline
- SEV1: Detect 0-5 min → Acknowledge 5 min → Mitigate 15 min → Resolve 60 min → Post-mortem 24h
- SEV2: Detect 0-15 min → Mitigate 1h → Resolve 4h → Post-mortem 48h
- SEV3: Detect 0-1h → Resolve 24h
- SEV4: Next sprint

## Communication Protocol
1. Status page update within 5 min of detection
2. Internal Slack/team alert immediately
3. Customer comms every 30 min for SEV1, hourly for SEV2
4. Engineering lead owns comms, not customer success

## Post-Mortem Requirements
- Timeline of events (5-min granularity)
- Root cause (5-whys analysis)
- Blameless culture: what failed, not who failed
- Action items with owners and due dates
- Share within 24h

## KPIs
- MTTR: SEV1 < 30 min, SEV2 < 2h
- MTTD: < 5 min for SEV1/2
- Post-mortem completion: 100%
- Recurrence of same root cause: 0%
