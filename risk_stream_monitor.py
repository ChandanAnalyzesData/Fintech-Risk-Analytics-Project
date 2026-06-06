"""
Fintech Risk Stream Monitor Engine - Pro Version
Purpose: Audits data and persists results to disk for reporting.
"""
import pandas as pd
import datetime

def audit_risk_data(df):
    print("--- Initializing Automated Risk Audit (Pro-Log) ---")
    
    # 1. Open the audit file in 'a' (append) mode
    with open("risk_audit_log.csv", "a") as log_file:
        
        for index, row in df.iterrows():
            amt = row["amount"]
            score = row["risk_score"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Logic Gate
            if score >= 80 or amt >= 100000:
                status = "FLAGGED"
            else:
                status = "CLEARED"
            
            # Create a comma-separated log entry
            log_entry = f"{timestamp},Row {index},{status},Amount:{amt},Score:{score}\n"
            
            # Write to file
            log_file.write(log_entry)
            print(f"Logged: {log_entry.strip()}")

    # 2. Bulk Export (The "Data Analyst" way)
    # This saves the entire processed view for further analysis in Excel/BI tools
    df.to_csv("full_risk_report.csv", index=False)
    print("\n--- Audit Complete. Log and Report updated. ---")