# Environment Setup Guide

## Prerequisites
- Python 3.11+
- Node.js 18+ (for dashboard)
- Git 2.40+
- uv (Python package manager)

## Local Development Setup
```bash
cd ~/Desktop/VirtualCompany
python -m venv .venv
.venv/Scripts/activate  # Windows
uv pip install -r requirements.txt
python company_sim.py --help
```

## Deployment Options
- **GitHub Pages**: Static `virtual_company.html` only
- **Vercel/Netlify**: Full stack + API
- **Fly.io / Render**: Container deployment with `company_sim.py` backend
- **AWS/GCP**: Production-grade with load balancer

## Environment Variables
- `VC_OWNER_NAME`: Owner name
- `VC_OWNER_CHAT_ID`: Telegram chat ID for reports
- `VC_DEPLOY_MODE`: local | staging | production
- `VC_LOG_LEVEL`: DEBUG | INFO | WARN | ERROR

## Health Checks
```bash
python company_sim.py health
curl http://localhost:8000/health
```

## Monitoring
- Logs: `logs/work_log.xml` + `logs/performance_scorecards.md`
- Budgets: `budgets/budget_policy.md` + `budgets/risk_register.md`
- Tasks: `tasks/tasks.json` + `tasks/tasks.md`
- Skills: `skills/` directory, version-controlled
