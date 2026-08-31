# NetWatch AI Architecture Specification
NetWatch AI uses a layered enterprise architecture:
- Data Tier: SQLAlchemy 2.0 ORM with SQLite / PostgreSQL backend
- Service Tier: Pluggable connectors, statistical anomaly detectors, Bayesian risk decay engines
- API Tier: Flask Blueprints with JWT and RBAC enforcement
- Presentation Tier: Pure HTML5/CSS3 with Vanilla ES6 JavaScript
