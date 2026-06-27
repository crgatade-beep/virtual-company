# tech/deployment_pipeline.md
Skill ID: tech-deploy-02
Category: Technology
Agent: T-01, MGR-TECH
Difficulty: Advanced

## Definition
Automated workflow for building, testing, and deploying code changes from development to production environments with zero downtime.

## Pipeline Stages
1. **Commit**: Developer pushes code
2. **Lint/Typecheck**: Code quality gate
3. **Unit tests**: Isolated component tests
4. **Integration tests**: Cross-component tests
5. **Build**: Compile, optimize, create artifact
6. **Staging deploy**: Deploy to mirror of prod
7. **E2E tests**: Full user journey tests
8. **Canary deploy**: 5% → 25% → 100% traffic
9. **Production**: Full deployment
10. **Smoke tests**: Verify health post-deploy

## Best Practices
- Every commit triggers pipeline (no manual deploys for main branch)
- Feature flags for risky changes
- Rollback button tested monthly
- Deployment windows: Tue/Wed/Thu, 10am-2pm only
- Zero deploys on Friday, weekends, holidays

## KPIs
- Deployment frequency: Daily+
- Lead time for changes: < 2 hours
- Change failure rate: < 5%
- MTTR from failed deploy: < 15 min

## Tooling Examples
- CI/CD: GitHub Actions, GitLab CI, CircleCI
- Containers: Docker, Kubernetes
- IaC: Terraform, Pulumi
- Monitoring: Datadog, New Relic
