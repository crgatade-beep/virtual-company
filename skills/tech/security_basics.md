# tech/security_basics.md
Skill ID: tech-security-06
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Advanced

## Definition
Protection of systems, data, and networks from unauthorized access, attacks, and breaches through policies, tools, and practices.

## Core Principles
1. **Defense in depth**: Multiple layers
2. **Least privilege**: Minimum access required
3. **Zero trust**: Verify everything, trust nothing
4. **Fail secure**: Default to denying access
5. **Audit everything**: Logs for all critical actions

## Top Threats
- Phishing (social engineering)
- Weak/compromised credentials
- Unpatched vulnerabilities
- Misconfigured cloud resources
- Supply chain attacks

## Critical Controls
1. MFA enforced on all accounts
2. Secret rotation every 90 days
3. TLS 1.3+ everywhere
4. Input validation on all endpoints
5. Database backups encrypted, tested monthly

## Incident Response
- Detect: SIEM, anomaly detection, alerts
- Contain: Isolate affected systems
- Eradicate: Remove threat
- Recover: Restore from clean backup
- Lessons learned: Post-mortem

## Compliance
- GDPR (EU data protection)
- SOC2 Type II (security, availability, confidentiality)
- ISO 27001 (ISMS framework)
- OWASP Top 10 (web apps)

## KPIs
- Mean time to patch critical CVEs: < 7 days
- Phishing click rate: < 2%
- Failed login rate anomaly alerting: 100%
- Security incidents per quarter: 0
