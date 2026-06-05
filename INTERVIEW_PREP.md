# 🎤 INTERVIEW CHEAT SHEET — Olist Project

**Quick reference for technical interviews. Practice these answers!**

---

## 🔴 RED FLAGS TO AVOID

### ❌ Don't Say This
```
"I predicted 98.74% churn with Random Forest"
"We calculated profit using a 0.8 cost multiplier"
"I built a scalable FastAPI backend"
"This is production-ready"
```

### ✅ Say This Instead
```
"I identified 97.6% of customers made only one purchase (repeat-purchase risk)"
"Profit is estimated using an assumed 0.8 cost ratio; actual cost data wasn't available"
"I built a BI dashboard and analytical notebooks for decision-making"
"This is a portfolio project demonstrating analytics skills"
```

---

## 📊 THE 3 BUSINESS PROBLEMS YOU CAN EXPLAIN

### 1️⃣ Customer Retention Crisis
- 97.6% of customers never repeat (single-purchase)
- 2.4% are repeat customers (champions + loyal)
- **Action:** Retention campaigns for at-risk, onboarding sequence for new customers

### 2️⃣ São Paulo Dependency
- 37.5% of revenue from one state (SP)
- Other states underperforming
- **Action:** Regional seller recruitment, regional marketing

### 3️⃣ Revenue Concentration
- Top 20% of categories drive ~80% of revenue (Pareto)
- Untapped potential in low-margin categories
- **Action:** Price optimization, bundling, category promotions

---

## 🎯 STRONGEST FEATURES TO TALK ABOUT

| Feature | What to Say | Interview Value |
|---------|-----------|-----------------|
| **RFM Segmentation** | "Segmented 93K customers into 5 groups by recency, frequency, monetary. Champions earn 12x more lifetime value than at-risk customers." | ⭐⭐⭐⭐⭐ |
| **SQL Window Functions** | "Used RANK, ROW_NUMBER, running totals to calculate Pareto analysis and YoY growth in 30+ queries." | ⭐⭐⭐⭐⭐ |
| **Power BI Dashboard** | "Connected 9 relational tables with proper star schema. Built executive dashboard with slicers, KPI cards, trend charts." | ⭐⭐⭐⭐ |
| **CLV Calculation** | "Calculated Customer Lifetime Value for all 93K customers using recency, frequency, monetary metrics." | ⭐⭐⭐⭐ |
| **Cohort Analysis** | "Tracked customer cohorts over 24 months to measure retention rates by acquisition month." | ⭐⭐⭐⭐ |
| **Profit Disclaimer** | "Acknowledged that profit is estimated, not actual — kept assumptions transparent." | ⭐⭐⭐⭐ |

---

## 💬 INTERVIEW Q&A PREP

### Q: "Walk me through this project."

**30-second version:**
"I analyzed 96K e-commerce orders from Olist. I cleaned and merged 9 tables, engineered 15+ features, and built SQL queries to answer business questions. I segmented 93K customers using RFM to identify 2.4% repeat customers vs. 97.6% single-purchase. I created Power BI dashboards and identified three key business problems: retention crisis, regional concentration, and revenue concentration. The whole project demonstrates SQL, Python, Excel, and BI skills."

**3-minute version:**
[Add specifics from project, mention business context]

---

### Q: "Why did you choose RFM instead of other segmentation?"

**Good answer:**
"RFM is the industry standard for e-commerce customer segmentation. Recency tells you recent engagement, frequency tells you loyalty, monetary tells you value. Together, they give a quick 5-segment view (Champions, Loyal, At Risk, Lost, Need Attention) that's actionable for marketing campaigns."

---

### Q: "How did you calculate profit?"

**Honest answer:**
"The Olist dataset doesn't include actual cost data, so I used an estimated cost ratio of 80% of price. This is noted in the README. It's useful for relative comparisons (category A vs B) but not suitable for real business decisions. In a real scenario, I'd use actual cost data."

---

### Q: "Why is your churn rate 98%?"

**Clear answer:**
"It's not traditional 'churn.' I defined it as single-purchase customers — people who made only one order in the 24-month observation window. In e-commerce, many customers are one-time buyers (not churned, just single-purchase). The business problem is: how do we convert these 97.6% into repeat customers?"

---

### Q: "What would you do differently?"

**Good answer:**
"Three things:

1. **Actual cost data** — Get real cost breakdowns instead of assumed ratio
2. **Longer observation window** — Current data is 2 years; need 3-5 years to distinguish true churn from seasonal buyers
3. **Control variables** — Include external factors (market conditions, competitors, seasonality) in analysis
4. **CLV prediction** — Use RFM to predict future CLV, not just describe past behavior"

---

### Q: "Which SQL query are you most proud of?"

**Answer:**
"Query 45 on Pareto analysis. It uses a CTE to rank customers by revenue, then calculates cumulative revenue percentage using a window function. That's the top 20% of customers driving 80% of revenue. It demonstrates CTEs, window functions, and business logic all together."

---

### Q: "How does your Power BI dashboard filter data?"

**Answer:**
"The dashboard has slicers at the top for date range, state, category, and seller. These are connected to the fact table and filter all visualizations below. The design uses a star schema: dim_customers, dim_products, dim_sellers on the outside; fact_orders in the center. All relationships are Many-to-One."

---

### Q: "How would you improve this project?"

**Honest answer:**
"1. Include .pbix file for download (not just screenshots)
2. Publish Power BI to Service (live dashboard)
3. Add more advanced analysis: propensity modeling, LTV prediction, churn probability scoring
4. Create actionable recommendations with ROI calculations
5. Build a clean, single master notebook instead of 7 separate ones"

---

## 🚨 RED FLAGS IF YOU CAN'T ANSWER

If interviewer asks and you DON'T know:
- "What's your most complex SQL query?" → You didn't review your own work
- "How did you handle missing values?" → You don't understand data cleaning
- "What does RFM mean?" → You copy-pasted the project
- "Why these 9 tables?" → You don't understand the schema

**Fix:** Before ANY interview, know your project inside-out.

---

## 📚 PRACTICE ROUTINE

**Before interview:**
1. Read BUSINESS_INSIGHTS.md (5 min)
2. Review sql/README.md, pick 2 queries to explain (10 min)
3. Review Powerbi_dashboard/README.md, understand each visualization (10 min)
4. Practice 30-second, 2-minute, and 5-minute project pitches (15 min)
5. Answer the Q&A above out loud (15 min)

**Total prep: 1 hour**

---

## 🎯 THE SCORING RUBRIC (What Interviewers Care About)

| Area | What They Check | Your Answer |
|------|-----------------|-----------|
| **SQL** | Can you explain CTEs, window functions, joins? | ✅ Yes (see Query 45) |
| **Python** | Feature engineering? Data cleaning logic? | ✅ Yes (15+ features) |
| **BI** | Can you design a dashboard? Star schema? | ✅ Yes (9-table model) |
| **Business Logic** | Do you think like a business analyst? | ✅ Yes (3 problems + actions) |
| **Communication** | Can you explain technical work in business terms? | ✅ Yes (this doc) |
| **Honesty** | Do you acknowledge limitations? | ✅ Yes (profit disclaimer) |

**You score high on ALL of these.** 🎉

---

## ⚠️ FINAL WARNINGS

1. **Don't overclaim ML expertise** — The Random Forest model is optional, focus on analytics
2. **Don't pretend cost data is real** — Always mention it's estimated
3. **Don't call it "production-ready"** — It's a portfolio project
4. **Don't ignore the disclaimers** — They show maturity and honesty
5. **Don't memorize answers** — Understand concepts, speak naturally

---

**You're ready. Go crush that interview! 💪**

Last updated: June 2026
