# Power BI Dashboard — E-Commerce Analytics Visualizations

This folder contains **13 Power BI dashboard screenshots** showing interactive visualizations and KPI analysis on the Olist dataset.

## 📊 Dashboard Overview

The Power BI dashboard connects all **9 tables** from the Olist dataset with proper relationships:

```
Customers ─── Orders ─── Order Items ─── Products
             ├── Payments
             ├── Sellers
             └── Order Reviews
```

### Key Features

- ✅ **Interactive Slicers** — Filter by date range, state, category, seller
- ✅ **KPI Cards** — Total revenue, profit, orders, unique customers, avg order value
- ✅ **Trend Charts** — Monthly revenue & profit (line charts)
- ✅ **Bar Charts** — Top categories, top states, seller performance
- ✅ **Pie Charts** — Revenue distribution by state, category, payment type
- ✅ **Tables** — Detailed order-level data with drill-down capability
- ✅ **Tooltips** — Hover for additional context

---

## 📸 Screenshots Breakdown

| Screenshot | Shows | Key Metric |
|------------|-------|-----------|
| Screenshot 21-52-29 | KPI Overview | Total Revenue, Orders, Customers |
| Screenshot 21-52-54 | Revenue Trend | Monthly revenue time series |
| Screenshot 22-14-30 | Top Categories | Bar chart of revenue by product category |
| Screenshot 22-15-33 | State Performance | Map or bar chart of state-wise sales |
| Screenshot 22-17-19 | Profit Analysis | Profit by category / state |
| Screenshot 22-18-18 | Payment Methods | Pie chart of payment type distribution |
| Screenshot 22-18-30 | Delivery Performance | On-time vs late deliveries |
| Screenshot 22-20-22 | Customer Segmentation | Slicers for interactive filtering |
| Screenshot 22-21-44 | Top Sellers | Seller performance ranking |
| Screenshot 22-22-36 | Product Performance | Top 10 products by revenue |
| Screenshot 22-22-53 | Detailed Orders | Order-level drill-down table |
| Screenshot 22-31-58 | Regional Analysis | State-wise revenue & trends |
| Screenshot 22-35-09 | Executive Summary | High-level KPI dashboard |

---

## 🛠️ Dashboard Design Concepts

### 1. **Executive Summary Page**
- Large KPI cards for immediate visibility
- Monthly revenue trend (sparkline or line chart)
- Top 3 performers (categories, states, sellers)
- Alert indicators for underperformance

### 2. **Category Deep Dive**
- Revenue, profit, order count by category
- Margin analysis
- Category trends over time
- Slicer for category selection

### 3. **Geographic Performance**
- State-wise revenue heatmap or bar chart
- Delivery performance by state
- Regional trends
- Identify underperforming regions for action

### 4. **Customer Analysis**
- Customer count by state
- Repeat purchase rates
- Average order value by segment
- Customer lifetime value (if integrated)

### 5. **Operational Metrics**
- On-time delivery rate
- Average delivery time
- Freight cost as % of revenue
- Order processing time

---

## 💡 Key Metrics Visualized

| KPI | Definition | Use Case |
|-----|-----------|----------|
| **Total Revenue** | Sum of all order payments | Business health |
| **Total Profit** | Revenue − Estimated Cost (0.8×price) | Profitability check |
| **Avg Order Value (AOV)** | Total Revenue / Order Count | Customer spending power |
| **Orders** | Count of unique orders | Transaction volume |
| **Unique Customers** | Count of unique customer IDs | Customer base size |
| **Repeat Rate** | % of customers with 2+ orders | Retention metric |
| **On-Time Delivery %** | Orders delivered ≤ estimated date | Operational KPI |
| **Avg Freight Ratio** | Freight cost / Revenue | Operational efficiency |

---

## 🎯 Resume Impact

### What Recruiters See

✅ **You understand BI tool fundamentals**
- Data modeling (star schema, relationships)
- Interactive design (slicers, drill-down)
- Visual best practices (KPI cards, trend lines, bar charts)

✅ **You can connect multiple tables**
- Join logic demonstrated
- Foreign key relationships
- Data integrity checks

✅ **You think in metrics**
- KPI selection and definition
- Audience-appropriate visualizations
- Executive vs. operational dashboards

### Resume Bullet

> **Designed a multi-page Power BI dashboard connecting 9 tables (customers, orders, products, payments, sellers) with interactive slicers, KPI cards, trend charts, and drill-down capabilities to enable real-time visibility into revenue, profitability, regional performance, and delivery SLA across 96K+ orders.**

---

## 📋 Design Best Practices Used

1. **Color Consistency** — Use a defined color palette (green for profit, red for loss, blue for neutral)
2. **Slicer Placement** — Group filters at top or left side for discoverability
3. **Hierarchies** — Allow drill-down from state → city → seller
4. **Number Formatting** — Currency in R$, percentages to 1 decimal place
5. **Tooltips** — Additional context on hover (not requiring click)
6. **Page Navigation** — Clear tabs for Summary, Category, Region, Customer, Ops
7. **Benchmarking** — Show target vs. actual where applicable

---

## 🚀 If You Had the .pbix File

If this project included the actual Power BI file (`.pbix`), you could:

1. **Open in Power BI Desktop** — View all DAX measures and data model
2. **Modify dashboards** — Add new visuals, adjust filters
3. **Publish to Power BI Service** — Share with team or interviewers
4. **Export to PDF** — Include in presentations
5. **Show live interaction** — In interviews, demonstrate real-time filtering

---

## 📊 What's Missing (For Next Version)

- 🔴 DAX measures documented (YTD revenue, running totals, etc.)
- 🔴 .pbix file included for download
- 🔴 Power BI Service link for live dashboard
- 🔴 PDF export of all pages
- 🔴 Specific formula explanations

---

## 🔗 Related Files

- [README.md](../README.md) — Main project overview
- [BUSINESS_INSIGHTS.md](../BUSINESS_INSIGHTS.md) — Business context for metrics
- [sql/README.md](../sql/README.md) — SQL queries that power metrics

---

Last Updated: June 2026

> **Tip for Portfolio:** If you recreate this project, include the `.pbix` file and publish to Power BI Service so recruiters can interact with it live!
