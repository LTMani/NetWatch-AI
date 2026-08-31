# NetWatch AI — Enterprise Network Usage & Intelligence Platform

**Watch Smarter. Detect Faster.**

AI-powered enterprise network usage and intelligence platform for authorized monitoring of network activity, domain-level website analytics, anomaly detection, risk scoring, network diagnostics, and actionable security insights.

---

## 🏗 Build & Project Structure

NetWatch AI is a production-grade Python web application built using Flask, SQLAlchemy 2.0, and pure ES6 JavaScript / CSS3 without heavyweight node dependencies.

```bash
# Build / syntax validation check
make build
# or with npm/package.json
npm run build
```

---

## 📦 Installation

Ensure Python 3.10+ is installed on your system.

```bash
# 1. Clone repository
git clone https://github.com/LTMani/NetWatch-AI.git
cd netwatch-ai

# 2. Install dependencies via manifest or lockfile
pip install -r requirements.txt

# (Optional) Using Poetry
poetry install
```

---

## 🚀 Running / Usage

### Development Server
```bash
# Using Python directly
python run.py
# or
python app.py
# or
python main.py

# Using Makefile
make run

# Using NPM Script
npm start
```
The platform will launch and be accessible at:
👉 **http://127.0.0.1:5000**

### Default Enterprise Credentials
- **Super Administrator**: `admin` / `Admin@NetWatch2026!`
- **Network Admin**: `netadmin` / `NetAdmin@2026!`
- **SOC Analyst**: `soc_analyst` / `Analyst@2026!`

---

## 🧪 Testing & Quality Assurance

Run the comprehensive test suite across unit, integration, and end-to-end workflows:

```bash
# Run pytest automated test suite (23 tests)
pytest

# Run full platform and 25-view subset audit
python scripts/verify_all_subsets.py
```

---

## 🔒 Security & Privacy Notice
NetWatch AI operates exclusively on **authorized metadata** (flow statistics, domain query names, IP/MAC bindings). It never captures webpage content, passwords, private messages, keystrokes, form data, or personal files.
