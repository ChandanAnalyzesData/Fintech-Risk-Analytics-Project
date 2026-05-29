# Fintech Risk Analytics Project

## 📅 Week 1: Core Transaction Retrieval & Sorting

### 🏢 Case Study: Regional Hub Data Extraction
**1. The Business Problem:**
The risk operations team needs to identify high-value transaction patterns specifically within the regional hub of Bengaluru to monitor local cash flows and spot potential anomalies.

**2. The Technical Approach:**
I structured a targeted data retrieval query using conditional filtering to isolate local records and applied a descending sort to instantly surface the highest financial exposure.

```sql
SELECT user_id, amount, status
FROM Transactions
WHERE location = 'Bengaluru'
ORDER BY amount DESC;
