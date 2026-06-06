"""
Fintech Risk Stream Monitor Engine
Purpose: Modular function to process SQL-extracted dataframes.
"""

def audit_risk_data(df):
    print("--- Initializing Automated SQL Risk Scan ---\n")
    
    for index, row in df.iterrows():
        # Using the column names we defined in our SQL query
        amt = row["amount"]
        score = row["risk_score"]
        
        # Risk Logic Gates
        if score >= 80 or amt >= 100000:
            print(f"Row {index}: [FLAGGED] High Risk - Amount: {amt}, Score: {score}")
        else:
            print(f"Row {index}: [CLEARED] Amount: {amt}, Score: {score}")
    
    print("\n--- Scan Sequence Complete ---")