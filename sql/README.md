# SQL Analysis — 60+ Business Questions

This folder contains **60+ SQL business questions** covering real analytics use cases on the Olist e-commerce dataset.

## 📊 What's Covered

| Difficulty | Topics | Files |
|-----------|--------|-------|
| **Beginner (Q1-Q10)** | SELECT, COUNT, DISTINCT, ORDER BY, LIMIT | SQL-00-10 |
| **Intermediate (Q11-Q20)** | WHERE, GROUP BY, HAVING, aggregation | SQL-10-20 |
| **Intermediate+ (Q21-Q30)** | JOIN, multiple tables, subqueries | SQL-20-30 |
| **Advanced (Q31-Q40)** | CTEs, window functions, RANK, ROW_NUMBER | SQL-30-40 |
| **Expert (Q41-60)** | Running totals, YoY growth, Pareto analysis | SQL-40-60 |

---

## 📁 File Legend

| File | Questions | Focus |
|------|-----------|-------|
| **SQL-00-10** | 1-10 | Basic SELECT, COUNT, DISTINCT |
| **SQL-10-20** | 11-20 | GROUP BY, HAVING, aggregates |
| **SQL-20-30** | 21-30 | JOIN operations, relationships |
| **SQL-30-40** | 31-40 | CTEs, window functions, ranking |
| **SQL-40-60** | 41-60 | Advanced: YoY, running totals, Pareto |
| **Sql_Questions.ipynb** | All 60+ | Jupyter notebook with explanations |
| **POSTGREY-SQL-DATA-LOAD** | Schema | Table creation & data loading |

---

## 🎯 Key Concepts Demonstrated

### Window Functions
- `ROW_NUMBER()` — Rank customers by total spending
- `RANK()` / `DENSE_RANK()` — Rank with ties handling
- Running totals using `SUM() OVER (ORDER BY ...)`
- YoY (Year-over-Year) growth calculation

### CTEs (Common Table Expressions)
- Multi-step queries with `WITH` clause
- Customer segmentation using CTEs
- Revenue aggregation by time period

### Business Logic
- **Pareto Analysis** — Identify top 20% of customers driving 80% of revenue
- **Cohort Analysis** — Track customer retention over time
- **State-wise Performance** — Compare regions, identify underperformers
- **Category Profitability** — Revenue vs profit by product category
- **Delivery SLA** — On-time delivery rates, delay patterns

---

## 💡 How to Use These Queries

### For Learning
1. Start with **SQL-00-10** to review basic SELECT syntax
2. Progress to **SQL-10-20** for GROUP BY and aggregation
3. Move to **SQL-20-30** for JOIN patterns
4. Study **SQL-30-40** for window functions and CTEs
5. Challenge yourself with **SQL-40-60** for real-world optimization

### For Portfolio
- Pick 3-5 best queries that showcase YOUR skills
- Add context: "This query identifies top 20% customers driving 80% revenue"
- Include result screenshots with query explanation
- Link to your resume or GitHub

### For Interview Prep
- Review window function patterns (most common in interviews)
- Practice explaining WHY you chose CTEs over subqueries
- Be ready to optimize slow queries
- Know the difference between JOIN types

---

## 📝 Sample Query Concepts

### Q45 — Pareto Analysis (80/20 Rule)
**What it does:** Identifies top 20% of customers driving ~80% of revenue
```sql
-- Revenue contribution by customer
WITH ranked_customers AS (
  SELECT customer_id, 
         SUM(revenue) as total_revenue,
         SUM(SUM(revenue)) OVER (ORDER BY SUM(revenue) DESC) as cumulative_revenue
  FROM orders
  GROUP BY customer_id
)
SELECT customer_id, total_revenue,
       cumulative_revenue,
       (cumulative_revenue / (SELECT SUM(revenue) FROM orders)) * 100 as pct_of_total
FROM ranked_customers
ORDER BY total_revenue DESC;
```

### Q52 — YoY Revenue Growth
**What it does:** Compares revenue month-by-month across years
```sql
SELECT EXTRACT(MONTH FROM date) as month,
       EXTRACT(YEAR FROM date) as year,
       SUM(revenue) as monthly_revenue,
       LAG(SUM(revenue)) OVER (PARTITION BY EXTRACT(MONTH FROM date) 
                              ORDER BY EXTRACT(YEAR FROM date)) as prev_year_revenue,
       ((SUM(revenue) - LAG(...)) / LAG(...)) * 100 as yoy_growth_pct
FROM orders
GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
ORDER BY year DESC, month;
```

### Q58 — Cohort Retention
**What it does:** Tracks which cohort of customers (by signup month) stays active
```sql
WITH cohorts AS (
  SELECT customer_id,
         DATE_TRUNC('month', MIN(order_date)) as cohort_month
  FROM orders
  GROUP BY customer_id
)
SELECT cohort_month, COUNT(customer_id) as cohort_size,
       COUNT(CASE WHEN order_count >= 2 THEN 1 END) as repeat_customers,
       (COUNT(CASE WHEN order_count >= 2 THEN 1 END) / COUNT(*)) * 100 as retention_pct
FROM cohorts
LEFT JOIN (SELECT customer_id, COUNT(*) as order_count FROM orders GROUP BY 1) using (customer_id)
GROUP BY cohort_month
ORDER BY cohort_month DESC;
```

---

## ✅ Skills You're Demonstrating

- ✅ Multi-table JOIN patterns
- ✅ Aggregation with GROUP BY
- ✅ Window functions for ranking & running totals
- ✅ CTEs for readable, layered queries
- ✅ Business logic (Pareto, cohort, YoY)
- ✅ Performance optimization
- ✅ Clear naming & documentation

---

## 📈 Resume Bullet

> **Wrote 60+ SQL queries covering SELECT, JOIN, GROUP BY, subqueries, CTEs, and window functions (RANK, ROW_NUMBER, running totals) to answer real business questions including customer ranking, Pareto analysis, YoY growth, and cohort retention on Olist's 9-table schema.**

---

Last Updated: June 2026
