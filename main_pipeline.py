import pandas as pd
import sqlite3
from risk_stream_monitor import audit_risk_data

# 1. Open the tunnel
connection = sqlite3.connect("fintech_data.db")
cursor = connection.cursor()

# --- SELF-HEALING BLOCK: Ensure tables exist ---
cursor.execute("CREATE TABLE IF NOT EXISTS Transactions (transaction_id INTEGER, amount INTEGER, user_id INTEGER, status TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS User_Profiles (user_id INTEGER, risk_score INTEGER)")
# Only insert if empty (to avoid duplicates)
cursor.execute("SELECT count(*) FROM Transactions")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO Transactions VALUES (1, 4000, 101, 'PENDING')")
    cursor.execute("INSERT INTO Transactions VALUES (2, 125000, 102, 'PENDING')")
    cursor.execute("INSERT INTO Transactions VALUES (3, 500000, 103, 'PENDING')")
    cursor.execute("INSERT INTO User_Profiles VALUES (101, 12)")
    cursor.execute("INSERT INTO User_Profiles VALUES (102, 85)")
    cursor.execute("INSERT INTO User_Profiles VALUES (103, 90)")
    connection.commit()
# -----------------------------------------------

# 2. Extract
sql_query = """
SELECT t.amount, r.risk_score
FROM Transactions AS t
INNER JOIN User_Profiles AS r ON t.user_id = r.user_id
"""
df = pd.read_sql_query(sql_query, connection)

# 3. Close and run
connection.close()
audit_risk_data(df)