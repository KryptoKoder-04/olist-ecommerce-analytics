# 🛒 E-Commerce Revenue, Retention & Profitability Analytics Platform

> **End-to-end analytics project on 96,454 real Olist e-commerce orders.**
>
> **Core skills:** SQL | Python | Excel | Power BI | Business Analytics | Data Storytelling

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-Dashboards-green?style=flat-square)
![Power BI](https://img.shields.io/badge/PowerBI-Visualizations-yellow?style=flat-square)

---

📦 **Dataset:** [Olist Brazilian E-Commerce — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 📋 Quick Navigation

- [What This Covers](#-what-this-covers)
- [Business Snapshot](#-business-snapshot)
- [Key Deliverables](#-key-deliverables)
- [Data & Method Disclaimers](#-data--method-disclaimers)
- [Analyses Performed](#-analyses-performed)
- [RFM Customer Segments](#-rfm-customer-segments)
- [Folder Structure](#-folder-structure)
- [How to Use This Repo](#-how-to-use-this-repo)

---

## 🧠 What This Covers

This project demonstrates **end-to-end data analytics** on a real e-commerce dataset:

1. **SQL Analysis** — 60+ business questions using joins, CTEs, window functions, ranking, Pareto analysis
2. **Python EDA** — Data cleaning, feature engineering, exploratory analysis (7 pipelines)
3. **Customer Analytics** — RFM segmentation, Customer Lifetime Value (CLV), repeat-purchase patterns
4. **Business KPIs** — Revenue trends, category performance, state-wise sales, delivery SLA issues
5. **Excel Dashboards** — Pivot tables, slicers, KPI summaries
6. **Power BI Visualizations** — Multi-table dashboards with interactive filters
7. **Repeat-Purchase Risk Analysis** — Identify single-purchase vs. repeat customers using segmentation

**Who should review this?**

- **Data Analysts** looking for a portfolio project covering SQL, Python, BI, business metrics
- **Business Analysts** interested in customer segmentation, retention, and revenue analysis
- **Hiring managers** evaluating analytics and BI skills on real-world data

---

## 📊 Business Snapshot

| Metric | Value | Note |
|--------|-------|------|
| **Total Revenue** | R$16,110,492 | Oct 2016 – Aug 2018 |
| **Total Profit** | R$5,061,907 | *Estimated (see disclaimers)* |
| **Profit Margin** | 32.3% | |
| **Total Orders** | 96,454 | |
| **Unique Customers** | 93,335 | |
| **Avg Order Value** | R$167.03 | |
| **Top Category** | beleza_saude (Health & Beauty) | |
| **Highest Revenue State** | SP (São Paulo) | R$6.04M (37.5% of total) |
| **States Covered** | 27 | All Brazilian states |
| **Product Categories** | 74 | |
| **Repeat Customers** | 2,221 (2.4%) | Made 2+ purchases |
| **Single-Purchase Customers** | 91,114 (97.6%) | Made only 1 purchase |

---

## 🎯 Key Deliverables

### ✅ SQL Analysis

- **60+ business questions** covering real analytics use cases
- **Techniques:** SELECT, JOIN, GROUP BY, HAVING, subqueries, CTEs, window functions (RANK, ROW_NUMBER, running totals)
- **Real-world queries:** Customer ranking, Pareto analysis, YoY growth, monthly trends
- **Location:** [sql/](./sql/) folder

### ✅ Python Data Pipeline

- **7 EDA notebooks** covering data load → cleaning → analysis → visualization
- **Feature engineering:** 15+ derived features (revenue, profit, margins, delays, freight ratios)
- **Visualizations:** Matplotlib (static) and Plotly (interactive)
- **Location:** [notebooks/](./notebooks/) folder

### ✅ Customer Segmentation

- **RFM Analysis:** Recency, Frequency, Monetary segmentation
- **Customer Lifetime Value (CLV):** Calculated for all 93K+ customers
- **Repeat-Purchase Risk Scoring:** Identify single-purchase vs. repeat customers
- **Output:** 5 customer segments with revenue and retention profiles

### ✅ Excel Dashboards

- Interactive pivot tables for category, monthly, and state analysis
- Slicers for dynamic filtering
- KPI summary sheet with key metrics
- **Location:** [MsExcel_Dashboard/](./MsExcel_Dashboard/) folder

### ✅ Power BI Dashboard

- All 9 tables connected with proper star schema relationships
- Interactive KPI cards, slicers, bar/line/trend charts
- Filters by date range, category, state, seller
- **Location:** [Powerbi_dashboard/](./Powerbi_dashboard/) folder

### ✅ Business Insights Report

- 6 real business problems with data-backed root causes
- Actionable recommendations for revenue growth and retention
- Interview-ready narrative with metrics and trends
- **Location:** [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md)

---

## ⚠️ Data & Method Disclaimers

### 🔴 Profit Calculation is Estimated

**How it was calculated:**
```
cost = 0.8 × price
profit = revenue - cost
```

**Important:** The Olist dataset does NOT include actual cost data. The `0.8` multiplier is an **assumption** made for this analysis.

**What this means for you:**
- ✅ Profit figures are useful for **relative comparisons** (category A vs category B)
- ❌ Profit is NOT suitable for real business decisions
- 💡 In interviews: Be ready to explain "Where did the 0.8 come from?"
- 📝 Better approach: Always note this assumption in your analysis

---

### 🔴 Repeat-Purchase Definition

**How it's defined in this project:**
> **Single-Purchase Customer:** Customers who made only one order within the observation window (Oct 2016 – Aug 2018).

> **Repeat-Purchase Customer:** Customers who made 2+ orders.

**Why not call it "churn"?**
- Traditional "churn" applies to subscriptions (SaaS, memberships)
- E-commerce is different — many customers buy once intentionally
- The dataset covers ~2 years, a limited window
- Using "churn" without context can mislead recruiters

**How it's used:**
- ✅ Identify low-frequency vs. high-frequency customers
- ✅ Flag single-purchase customers as retention targets
- ✅ Segment customers for targeted campaigns
- ❌ NOT predicting true subscription churn

---

## 📊 Analyses Performed

### 1. **Revenue & Profitability**
- Monthly revenue and profit trends (24-month time series)
- Top 10 categories by revenue and profit
- Pareto analysis — which categories drive 80% of revenue
- State-wise revenue distribution (27 states)

### 2. **Customer Intelligence**
- Customer acquisition trends
- Order frequency distribution
- Customer lifetime value (CLV) by segment
- Repeat purchase rates by cohort

### 3. **Category Performance**
- Revenue, profit, and order count by category
- Average price and profit margin by category
- Top-performing categories by revenue

### 4. **Delivery & Operations**
- On-time delivery rates by state
- Delivery delay analysis
- Freight cost as % of revenue by state
- State-wise SLA compliance

### 5. **RFM Segmentation**
- Recency, Frequency, Monetary scores
- 5 customer segments: Champions, Loyal, At Risk, Lost, Need Attention
- Revenue impact of each segment
- Retention rates by segment

---

## 👥 RFM Customer Segments

| Segment | Count | Total Revenue | Avg CLV | Repeat Rate |
|---------|-------|---------------|---------|------------|
| **Champions** | 141 | R$78,577 | R$2,174 | 100% |
| **Loyal** | 1,408 | R$427,886 | R$608 | 100% |
| **At Risk** | 672 | R$218,009 | R$696 | 100% |
| **Single-Purchase** | 91,114 | R$15,385,020 | R$169 | 0% |
| **Total** | 93,335 | R$16,110,492 | R$173 | 2.4% |

---

## 📁 Folder Structure

| Folder / File | Purpose |
|---|---|
| [README.md](./README.md) | You are here |
| [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md) | Business problems, root causes, recommendations |
| [notebooks/](./notebooks/) | 7 EDA pipelines (Jupyter notebooks) |
| [sql/](./sql/) | 60+ SQL business questions + queries |
| [MsExcel_Dashboard/](./MsExcel_Dashboard/) | Excel pivot tables + slicers + KPIs |
| [Powerbi_dashboard/](./Powerbi_dashboard/) | Power BI dashboard screenshots |
| [HLD.md](./HLD.md) | High-level architecture notes |
| [LLD.md](./LLD.md) | Technical formulas & calculations |

---

## 🚀 How to Use This Repo

### Quick Start (No Setup Required)

1. **Browse the SQL queries** — [sql/](./sql/) folder
   - See example business questions and their solutions
   - Learn window functions, CTEs, Pareto analysis

2. **View the notebooks** — [notebooks/](./notebooks/) folder
   - Full EDA pipeline with code and explanations
   - Data cleaning, feature engineering, visualizations

3. **Check the dashboards** — [Powerbi_dashboard/](./Powerbi_dashboard/)
   - Power BI screenshot gallery
   - See interactive visualizations and KPI designs

4. **Read business insights** — [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md)
   - Real problems identified in the data
   - Business recommendations with metrics

### If You Want to Run It Locally

**Prerequisites:** Python 3.11+, Jupyter, Git

```bash
# Clone the repo
git clone https://github.com/[your-repo]/olist-ecommerce-analytics.git
cd olist-ecommerce-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly jupyter

# Open notebooks
jupyter notebook notebooks/
```

---

## 📞 Questions?

- Review [BUSINESS_INSIGHTS.md](./BUSINESS_INSIGHTS.md) for business context
- Check [notebooks/](./notebooks/) for technical implementation
- Refer to [sql/](./sql/) for database queries

---



---

## 📊 Analyses Performed
| 🔗 LinkedIn | [linkedin.com/in/KabirSinghKhair](https://www.linkedin.com/in/kabirsinghkhair/) |

---

## 👤 Author


**Kabir Singh Khair**

B.Tech · Batch 2026
[GitHub](https://github.com/KryptoKoder-04) 

