"""
Fintech Risk Stream Monitor Engine
Purpose: Simulates an automated risk engine checking a continuous stream 
         of batch transaction amounts for high-value anomalies and systemic threats.
"""
# TODO:
# 1. Replace hardcoded 'transaction_batch' with dynamic SQL/Pandas extraction.
# 2. Integrate 'audit_risk_data' function into the main execution pipeline.
# 3. Add error handling for database connection drops.

# Simulated batch data extracted from database operations

transaction_batch = [4000, 125000, 60000, 2500, 500000, 15000]

print("=========================================")
print("  INITIALIZING RISK STREAM MONITOR...   ")
print("=========================================\n")

# Tracking accumulator to measure total high-risk exposure counts
high_value_count = 0

for amount in transaction_batch:
    
    # Rule 1: Kill-switch evaluation for extreme, systemic threats
    if amount == 500000:
        print(f"🚨 CRITICAL THRESHOLD MET: {amount} INR detected!")
        print("   [SYSTEM ACTION] Halting operational scan to prevent capital drain.\n")
        break
        
    # Rule 2: Tiered risk classification matrix
    if amount > 100000:
        print(f"Transaction: {amount:<7} INR  -->  [FLAG: HIGH RISK]")
        high_value_count += 1
    elif amount > 50000:
        print(f"Transaction: {amount:<7} INR  -->  [FLAG: MEDIUM RISK - Trigger Verification]")
    else:
        print(f"Transaction: {amount:<7} INR  -->  [FLAG: LOW RISK - Auto-Approve]")

print("=========================================")
print("             SCAN TERMINATED             ")
print(f"Total High-Risk Anomalies Intercepted: {high_value_count}")
print("=========================================")
