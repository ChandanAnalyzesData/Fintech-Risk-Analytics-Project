# Fintech Risk Analytics Project

## 📌 Project Overview
This repository contains an end-to-end data automation pipeline designed for fintech risk operations and fraud monitoring. The objective of this project is to showcase how relational database querying (SQL) and automated scripting (Python) work in tandem to intercept systemic financial threats, flag account anomalies, and track operational risk metrics.

## 🛠️ Technical Stack & Core Masteries
* **SQL:** Advanced data extraction, multi-table engineering (`INNER JOIN ... ON`), and grouped matrix filtering (`GROUP BY`, `HAVING`).
* **Python:** Automation loops (`for` iterators), logical control flows (`if/elif/else`), running state counters, and break-clause runtime execution.

## 📂 Project Directory Structure
* `database_queries.sql`: Houses production-grade SQL scripts that merge transaction data logs with user profile risk indices to isolate high-risk groups.
* `risk_stream_monitor.py`: An automated Python risk engine script simulating a real-time transaction processing stream that dynamically flags risk tiers and executes a kill-switch on critical threats.

## 📈 Current Project Progress
1. **Phase 1 (SQL Engineering):** Completed robust query patterns to join independent relational tables and aggregate overall financial exposures.
2. **Phase 2 (Python Core Automation):** Completed a runtime processing engine utilizing loops and conditional flags to parse batch streams.
3. **Phase 3 (Next Step):** Integrating the **Pandas** library to pipe live database queries directly into native Python DataFrames for real-time risk profiling.

