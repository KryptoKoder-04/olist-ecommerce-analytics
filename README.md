# 🛒 E-Commerce Revenue, Retention & Profitability Analytics Platform

> End-to-end analytics project on **96,454 real Olist e-commerce orders**.
> 
> **Core deliverables:** SQL analysis, Python EDA, RFM segmentation, CLV modeling, repeat-purchase risk analysis, Excel dashboards, and Power BI visualizations.
> 
> **For:** Data Analyst and Business Analyst portfolio.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Dashboards-green?style=flat-square)
![Power BI](https://img.shields.io/badge/PowerBI-Visualizations-yellow?style=flat-square)

---

📦 **Dataset:** [Olist Brazilian E-Commerce — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 📋 Quick Navigation

- [What This Project Covers](#-what-this-project-covers)
- [Business Snapshot](#-business-snapshot)
- [Key Deliverables](#-key-deliverables)
- [Analyses Performed](#-analyses-performed)
- [Data & Method Disclaimers](#️-data--method-disclaimers)
- [Folder Structure](#-folder-structure)
- [Setup](#-setup)

---

## 🧠 What This Project Covers

This project demonstrates **end-to-end data analytics** on a real e-commerce dataset:

1. **SQL Analysis** — 60+ business questions using joins, CTEs, window functions, Pareto analysis
2. **Python EDA** — Data cleaning, feature engineering, exploratory analysis (7 pipelines)
3. **Customer Analytics** — RFM segmentation, Customer Lifetime Value (CLV), repeat-purchase patterns
4. **Business KPIs** — Revenue trends, category performance, state-wise sales, delivery SLA issues
5. **Excel Dashboards** — Pivot tables, slicers, KPI summaries
6. **Power BI Visualizations** — Multi-table dashboards with filters and charts
7. **Repeat-Purchase Risk Modeling** — Identify non-repeat customers using predictive features

**Who should use this?**

Data Analysts, Business Analysts, and BI professionals looking for a real-world portfolio project.

---

## 📊 Business Snapshot

| Metric | Value | Note |
|--------|-------|------|
| **Total Revenue** | R$16,110,492 | |
| **Total Profit** | R$5,061,907 | *Estimated (see disclaimers)* |
| **Total Orders** | 96,454 | Oct 2016 – Aug 2018 |
| **Unique Customers** | 93,335 | |
| **Avg Order Value** | R$167.03 | |
| **Top Category** | beleza_saude (Health & Beauty) | |
| **Highest Revenue State** | SP (São Paulo) | R$6.04M (37.5% of total) |
| **States** | 27 | All Brazilian states |
| **Categories** | 74 | Product categories |
| **At-Risk Customers** | 90,535 / 93,335 (97%) | Non-repeat customers |
| **Repeat Customers** | 2,221 (2.4%) | Champions + Loyal + At-Risk repeaters |

---

## 🎯 Key Deliverables

### ✅ Core Analytics

1. **SQL Analysis** — [sql/](./sql/)
   - 60 business questions with queries
   - Covers SELECT, JOIN, GROUP BY, window functions, CTEs
   - Real-world metrics: YoY growth, running totals, customer ranking, Pareto analysis

2. **Python Data Pipeline** — [notebooks/](./notebooks/)
   - 7 EDA notebooks covering data load → cleaning → analysis → visualization
   - Feature engineering (15+ derived features)
   - Monthly revenue/profit trends, category performance, state analysis

3. **Customer Segmentation** — RFM + CLV
   - 5 RFM segments with revenue impact
   - Customer Lifetime Value for all 93K customers
   - Repeat-purchase risk scoring

4. **Excel Dashboards** — [MsExcel_Dashboard/](./MsExcel_Dashboard/)
   - Interactive pivot tables with slicers
   - Category, monthly, and state breakdowns
   - KPI summary sheet

5. **Power BI Dashboard** — [Powerbi_dashboard/](./Powerbi_dashboard/)
   - All 9 tables connected with proper relationships
   - KPI cards, slicers, bar/line/trend charts
   - Filters by date, category, state, seller

6. **Business Insights Report** — [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md)
   - 6 real business problems with root causes
   - Revenue strategy and action recommendations
   - Interview-ready narrative

---

## ⚠️ Data & Method Disclaimers

### 1. Profit Calculation is Estimated

**How it was calculated:**
```
cost = 0.8 × price
profit = revenue - cost
```

**Important:** Olist's dataset does NOT include actual cost data. The `0.8` multiplier is an assumption made for this analysis.

**What this means:**
- Profit figures are illustrative, not actual costs
- Useful for relative comparisons (category A vs B)
- Not suitable for real business decisions without actual cost data
- An interviewer may ask: "Where did this cost ratio come from?" Be prepared to explain.

---

### 2. Repeat-Purchase Risk vs. "Churn"

**Definition used in this project:**
> **Repeat-Purchase Risk:** Customers who made only one order within the observation window (Oct 2016 – Aug 2018).

**Why not call it "churn"?**
- The dataset covers ~2 years, a limited window
- Many customers buy once intentionally (not churned, just one-time buyers)
- E-commerce marketplace behavior differs from SaaS
- Using "churn" without context can be misleading

**How it's used:**
- Identifies customers with single-purchase pattern
- Flags them as "at-risk" for retention campaigns
- NOT a traditional subscription churn prediction

---

## 📁 Folder Structure

| Folder / File | Purpose |
|---|---|
| [README.md](./README.md) | You are here |
| [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md) | Business problems, root causes, action plans |
| [notebooks/](./notebooks/) | 7 EDA pipelines (Jupyter) |
| [sql/](./sql/) | 60 SQL business questions + queries |
| [MsExcel_Dashboard/](./MsExcel_Dashboard/) | Excel pivot tables + slicers + KPIs |
| [Powerbi_dashboard/](./Powerbi_dashboard/) | Power BI dashboard screenshots |
| [HLD.md](./HLD.md) | High-level architecture diagram |
| [LLD.md](./LLD.md) | Technical details & formulas |

---

## 📊 Analyses Performed
| 🔗 LinkedIn | [linkedin.com/in/KabirSinghKhair](https://www.linkedin.com/in/kabirsinghkhair/) |

---

## 👤 Author

**Kabir Singh Khair**
B.Tech · Batch 2026
[GitHub](https://github.com/KryptoKoder-04) 

---

> *"Everyone said get experience first.
> I said — let the project speak."*
>
> — Ashutosh, building this from zero.
```

---

**Commit message to use:**
```
docs: add live demo, dataset, GitHub, LinkedIn and portfolio links to README
