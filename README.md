# Fintech Risk Analytics Project

## 📌 Project Overview
A production-ready data automation pipeline designed for fintech risk operations. This project demonstrates end-to-end data engineering: from SQL-based relational data extraction to automated Python-based risk gating and persistent audit logging.

## 🛠️ Technical Stack
* **SQL:** Relational data engineering, complex table joins (`INNER JOIN`), and conditional aggregation (`GROUP BY`, `HAVING`).
* **Python (Pandas):** DataFrame manipulation, modular function architecture, and automated risk-gating logic.
* **Data Persistence:** Persistent audit trails using CSV logging, timestamping, and bulk reporting.
* **Version Control:** Git/GitHub workflow for professional code life-cycle management.

## 📂 Project Directory Structure
* `database_queries.sql`: Houses production-grade SQL scripts for data merging and risk profiling.
* `risk_stream_monitor.py`: The modular core engine containing the logic for transaction evaluation and audit trail generation.
* `main_pipeline.py`: The orchestration script that bridges the database to the Python engine (includes self-healing initialization).
* `risk_audit_log.csv`: Persistent, timestamped record of all flagged anomalies.
* `full_risk_report.csv`: Bulk snapshot of processed transaction data for downstream BI tools.

## 🚀 Key Features
* **Self-Healing Pipeline:** Automatically detects and initializes missing database structures on execution.
* **Automated Audit Logging:** Implements context-managed file writing to ensure persistent tracking of system flags.
* **Modular Design:** Decouples data extraction logic from evaluation logic, allowing for seamless scaling of risk rules.

## 📈 Current Project Status
- [x] **Phase 1 (SQL Engineering):** Complete.
- [x] **Phase 2 (Python Core Automation):** Complete.
- [x] **Phase 3 (Pipeline Integration):** Complete. Pipeline bridged via Pandas/SQLite.
- [x] **Phase 4 (Production Readiness):** Complete. Audit logging and persistent reporting implemented.