# NetWatch AI — Enterprise Network Usage & Intelligence Platform

> **Watch Smarter. Detect Faster.**

NetWatch AI is a production-grade, AI-driven enterprise network monitoring, telemetry analysis, anomaly detection, risk scoring, automated diagnostics, digital twin simulation, and incident management platform. Built strictly for authorized corporate monitoring environments, NetWatch AI adheres to uncompromising enterprise privacy boundaries by inspecting only network metadata (domains, flow statistics, bandwidth, interface health) without capturing private payloads, keystrokes, emails, or personal contents.

---

## Key Highlights & Capabilities

- **Executive & Operational Command Dashboards**: Live telemetry speedometers, composite network health gauges, real-time alert tickers, high-risk device leaderboards, and category breakdown donuts.
- **7-Stage Slow Network Diagnostic Wizard**: Automated diagnostic pipeline covering DNS resolution, path latency, packet loss, bandwidth saturation, MTU fragmentation, and interface errors with actionable remediation playbooks.
- **Multi-Algorithm Anomaly Detection**: Statistical Z-Score, EWMA, MAD, and Isolation Forest estimators detecting traffic surges, unusual off-hour exfiltrations, beaconing intervals, and novel domain spikes.
- **Dynamic Asset Risk Posture Engine**: Bayesian-decay asset scoring evaluating policy breaches, anomaly severity, threat intelligence reputation, and historical deviation.
- **Intelligent Alert Correlation**: Temporal and topological graph-based correlation collapsing raw alerts into actionable, deduped incident groups.
- **Interactive Network Topology Engine**: Canvas/SVG force-directed graph renderer with zoom/pan, node grouping (Edge, Core, Distribution, Access, Endpoints), link traffic heatmaps, and live node inspection.
- **Network Digital Twin & Scenario Simulator**: What-If failure injection sandbox modeling node outages, fiber cuts, DDoS surges, and dynamic Dijkstra failover resilience scoring.
- **Grounded AI Network Copilot**: Intent-driven RAG architecture retrieving internal metrics, SQL data, and topology states to answer administrator queries with grounded evidence and interactive remediation actions.
- **Office Hours & Bandwidth Analytics**: Workday vs off-hours traffic matrices, quiet-period violation tracking, top bandwidth consumers, and QoS bucket analysis.
- **24 Complete Frontend Pages**: Crafted with modern Vanilla ES6 JavaScript and a custom cyber-defense CSS3 design system (zero React/Vue/Angular dependencies).
- **Role-Based Access Control (RBAC)**: Super Admin, Network Admin, Security Analyst, and Auditor roles with cryptographic, tamper-evident audit logging.

---

## Technology Stack

- **Backend**: Python 3 (Flask, SQLAlchemy 2.0, Werkzeug, PyJWT)
- **Frontend**: HTML5, CSS3 Custom Theme System, Vanilla JavaScript (ES6 Modules)
- **Database**: SQLite (default local development) / PostgreSQL ready
- **Testing**: pytest (Comprehensive unit, integration, and E2E test suites)
- **Zero Credentials Policy**: Environment-variable-based configuration (.env)

---

## Directory Structure

`	ext
netwatch-ai/
├── app/
│   ├── config.py              # Environment configuration loader
│   ├── constants.py           # Enterprise enums and system constants
│   ├── models/                # 25+ SQLAlchemy ORM models
│   ├── repositories/          # Repository layer isolating SQL queries
│   ├── schemas/               # Request/Response validation schemas
│   ├── services/              # 18+ Business logic and intelligence engines
│   ├── routes/                # 20+ API and UI View Blueprints
│   ├── middleware/            # Security, Auth, Audit, and Rate Limiting
│   ├── errors/                # Global exception handlers
│   ├── utils/                 # Cryptography, math, IP utilities, exporters
│   ├── templates/             # Jinja2 HTML templates for all 24 pages
│   └── static/
│       ├── css/               # Base, layout, components, pages, responsive
│       └── js/                # Core, API client, auth, UI components, pages
├── scripts/
│   ├── seed_database.py       # Rich enterprise dataset seeder
│   ├── generate_telemetry.py  # Continuous telemetry generator
│   └── count_loc.py           # Genuine LOC reporting utility
├── tests/
│   ├── unit/                  # Engine unit tests
│   ├── integration/           # API and service integration tests
│   └── e2e/                   # Full incident lifecycle E2E tests
├── storage/                   # PDF/CSV exports and backups
├── requirements.txt
├── manage.py                  # Platform CLI management utility
├── run.py                     # Flask entrypoint
└── pytest.ini
`

---

## Quick Start Guide

### 1. Installation

`ash
# Clone the repository
git clone https://github.com/LTMani/NetWatch-AI.git
cd NetWatch-AI

# Install dependencies
pip install -r requirements.txt
`

### 2. Environment Setup

`ash
# Copy example environment configuration
cp .env.example .env
`

### 3. Initialize & Seed Database

`ash
# Create database schema and populate with enterprise simulation dataset
python manage.py init-db
python manage.py seed-db
`

### 4. Run the Application

`ash
# Start the web server
python run.py
`

Access the platform at: http://127.0.0.1:5000

### Default Enterprise Demo Accounts

| Role | Username / Email | Password | Access Scope |
|---|---|---|---|
| **Super Admin** | dmin@netwatch.internal | Admin@NetWatch2026! | Full administrative & policy access |
| **Network Admin** | 
etadmin@netwatch.internal | NetAdmin@2026! | Network, devices, diagnostics & topology |
| **Security Analyst** | nalyst@netwatch.internal | Analyst@2026! | Alerts, incidents, risk & anomalies |
| **Auditor** | uditor@netwatch.internal | Auditor@2026! | Read-only compliance & audit trails |

---

## Running Automated Tests

`ash
# Run complete test suite
pytest

# Run specific engine unit tests
pytest tests/unit/test_health_engine.py
pytest tests/unit/test_anomaly_detection.py
pytest tests/unit/test_risk_scoring.py
pytest tests/e2e/test_full_incident_flow.py
`

---

## License

Enterprise Proprietary — NetWatch AI Platform. Authorized Corporate Network Intelligence.
