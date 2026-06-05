# Notebooks — 7 EDA Pipelines

This folder contains **7 comprehensive Jupyter notebooks** that walk through the entire data analysis pipeline from raw data to business insights.

## 📚 Notebook Overview

| Pipeline | File | Purpose | Key Output |
|----------|------|---------|-----------|
| **Pipeline 1** | Datacleaning.ipynb | Data load, type conversion, handling nulls | df.csv (master) |
| **Pipeline 2** | Full-Analysis.ipynb | Feature engineering, summary tables | RFM, CLV, segments |
| **Pipeline 3** | Charts_plots-1.ipynb | Static visualizations (Matplotlib) | Revenue, category charts |
| **Pipeline 4** | Charts_plots-Copy1.ipynb | Product & regional charts | State, category deep dives |
| **Pipeline 5** | DataProfiling_ DataQualityAssessment.ipynb | Data quality, distributions | Profile report |
| **Pipeline 6** | matplotlib-pipeline.ipynb | Interactive charts (Plotly) | Dashboard HTML |
| **Pipeline 7** | ML Churn Prediction.ipynb | ML modeling, scoring | Repeat-purchase risk |

---

## 🔄 Data Flow

```
Raw 9 CSV files
    ↓
[Pipeline 1: Datacleaning]
    ↓
Master DataFrame (df.csv)
    ↓
[Pipeline 2: Full-Analysis] → Feature engineering → RFM, CLV
    ↓
[Pipeline 3-4: Charts] → Static visualizations
    ↓
[Pipeline 5: Data Profiling] → Quality assessment
    ↓
[Pipeline 6: Plotly] → Interactive dashboard
    ↓
[Pipeline 7: ML] → Repeat-purchase modeling
```

---

## 📋 Pipeline Details

### **Pipeline 1 — Data Cleaning (Datacleaning.ipynb)**

**What it does:**
- Loads all 9 raw CSV tables from Olist dataset
- Type conversions (object → datetime, category)
- Handles missing values (drop critical rows, fill medians)
- Removes duplicates
- Merges all 9 tables into single master dataframe

**Input:** 9 CSV files (orders, customers, products, payments, sellers, etc.)

**Output:** `df.csv` (115,011 rows × 44 columns)

**Skills demonstrated:**
- ✅ Pandas read_csv() and merge()
- ✅ Datetime handling
- ✅ Missing value strategy
- ✅ Data validation checks

---

### **Pipeline 2 — Feature Engineering & Aggregation (Full-Analysis.ipynb)**

**What it does:**
- Creates 15+ derived features (revenue, profit, margins, delays, freight ratios)
- Builds summary tables:
  - Monthly revenue / profit trends
  - Top 10 categories
  - State-wise performance
  - RFM segmentation
  - Customer Lifetime Value (CLV)
  - Pareto analysis (80/20 rule)

**Output:** Summary tables, RFM segments, CLV scores

**Skills demonstrated:**
- ✅ Feature engineering logic
- ✅ GroupBy aggregation
- ✅ Time-based analysis
- ✅ Customer segmentation
- ✅ Business metric calculation

**Example calculations:**
```python
# Revenue & Profit
df['revenue'] = df['price'] * df['quantity']
df['cost'] = df['revenue'] * 0.8  # ASSUMED
df['profit'] = df['revenue'] - df['cost']

# RFM scores
recency = (today - last_order_date).days
frequency = count(orders)
monetary = sum(revenue)

# Pareto: Find top 20% customers by revenue
customers_ranked = df.groupby('customer_id')['revenue'].sum().sort_values(ascending=False)
top_20_pct = customers_ranked.head(int(len(customers_ranked) * 0.2))
```

---

### **Pipeline 3 & 4 — Static Visualizations (Matplotlib)**

**Charts_plots-1.ipynb:**
- Monthly revenue and profit trends (24-month time series)
- Top 10 categories by revenue
- Top 10 categories by profit
- Revenue distribution by state
- Histogram of order values

**Charts_plots-Copy1.ipynb:**
- Product category performance heatmaps
- Freight cost analysis
- Delivery time vs. state
- Seller performance ranking
- Customer acquisition trends

**Output:** PNG/JPG visualizations saved locally

**Skills demonstrated:**
- ✅ Matplotlib figure creation
- ✅ Multi-subplot layouts
- ✅ Bar, line, heatmap, histogram charts
- ✅ Axis labeling & legends
- ✅ Business storytelling with visuals

---

### **Pipeline 5 — Data Profiling & Quality (DataProfiling_ DataQualityAssessment.ipynb)**

**What it does:**
- Statistical summary (mean, median, std dev, min, max)
- Null value analysis
- Duplicate detection
- Outlier identification
- Distribution checks
- Data quality scorecard

**Output:** Quality assessment report

**Skills demonstrated:**
- ✅ Descriptive statistics
- ✅ Data quality frameworks
- ✅ Identifying data issues early
- ✅ Documentation & reporting

---

### **Pipeline 6 — Interactive Dashboard (Plotly)**

**Notebooks:**
- **matplotlib-pipeline.ipynb** — Plotly interactive charts
- **ml-pipeline-main.ipynb** — Dashboard aggregation

**What it does:**
- Creates interactive charts (hover for details)
- Builds HTML dashboard
- Enables drill-down exploration
- Exports as standalone HTML

**Output:** `.html` dashboard file

**Skills demonstrated:**
- ✅ Plotly Express & Graph Objects
- ✅ Interactive design
- ✅ Dashboard composition
- ✅ HTML export for sharing

**Example:**
```python
import plotly.express as px

fig = px.bar(top_categories, x='category', y='revenue', 
             hover_data=['profit', 'orders'],
             title='Top 10 Categories by Revenue')
fig.show()
```

---

### **Pipeline 7 — Repeat-Purchase Risk Modeling (ML Churn Prediction.ipynb)**

**What it does:**
- Engineer 10+ features (recency, frequency, monetary, avg price, freight ratio, etc.)
- Train ML models: Logistic Regression, Decision Tree, Random Forest
- Evaluate models (accuracy, precision, recall, ROC-AUC)
- Score all customers with repeat-purchase risk
- Output risk labels: High / Medium / Low

**Output:** Customer risk scores, model metrics, churn_model.pkl

**Skills demonstrated:**
- ✅ Feature engineering for ML
- ✅ Model selection & evaluation
- ✅ Classification metrics
- ✅ Model serialization
- ✅ Risk scoring

**Note:** This is optional for your resume. Focus on analytics (pipelines 1-6) first.

---

## 🎯 How to Use These Notebooks

### For Learning

1. **Start with Datacleaning.ipynb** — Understand data structure and cleaning logic
2. **Review Full-Analysis.ipynb** — See feature engineering and business calculations
3. **Study Charts_plots-1.ipynb** — Learn visualization best practices
4. **Explore ml-pipeline-main.ipynb** — Understand dashboard design

### For Your Resume

Focus on **Pipelines 1-4** (data → analysis → visualization):

**Resume bullet:**
> **Built 7-pipeline Python EDA framework covering data cleaning, feature engineering (15+ derived metrics), exploratory analysis, static & interactive visualizations, and customer segmentation on 96K+ orders using Pandas, NumPy, Matplotlib, and Plotly.**

---

## 🛠️ Tech Stack Used

| Library | Purpose |
|---------|---------|
| **Pandas** | Data loading, manipulation, groupby, merge |
| **NumPy** | Numerical operations, statistics |
| **Matplotlib** | Static charts, multi-subplot layouts |
| **Seaborn** | Statistical visualizations |
| **Plotly** | Interactive dashboards |
| **Scikit-learn** | ML models (optional, Pipeline 7) |
| **Jupyter** | Notebook environment |

---

## 📊 Key Outputs Produced

| Output | File | Used For |
|--------|------|----------|
| Master data | df.csv | All analysis pipelines |
| RFM segments | RFM table | Customer segmentation |
| CLV scores | CLV by customer | Lifetime value analysis |
| Revenue trends | CSV + chart | Time series analysis |
| Category analysis | CSV + visualizations | Product strategy |
| Dashboard | HTML file | Interactive exploration |

---

## 💡 Best Practices Demonstrated

✅ **Modular code** — Each pipeline is standalone but interdependent  
✅ **Clear naming** — Variable and function names are descriptive  
✅ **Documentation** — Markdown cells explain logic and findings  
✅ **Error handling** — Checks for nulls, duplicates, outliers  
✅ **Reproducibility** — Same code always produces same results  
✅ **Business context** — Every analysis ties back to business questions  

---

## 📈 Running These Notebooks

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn plotly jupyter scikit-learn
```

### Run all notebooks in order
```bash
jupyter notebook
# Then open each notebook and run cells in sequence
```

### Quick start (if data already exists)
1. Open `Full-Analysis.ipynb`
2. Run all cells
3. Check outputs in console and generated files

---

## 🚨 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "df.csv not found" | Run Datacleaning.ipynb first to generate master data |
| "Module not found" | Install missing packages with pip |
| "Plotly charts won't display" | Run in Jupyter, not VSCode terminal |
| "Null values in analysis" | Check Pipeline 1 cleaning logic |

---

## 📞 For Interview Prep

**Potential questions:**
- "Walk me through your data cleaning process"
  → Talk about Pipeline 1, handling nulls, merging tables

- "How did you calculate profit?"
  → Explain the 0.8 multiplier assumption (important!)

- "Why use RFM segmentation?"
  → Explain customer value stratification, targeting campaigns

- "What features did you engineer?"
  → Mention revenue, margins, delays, frequency, monetary

---

Last Updated: June 2026

> **Pro Tip:** For your cleaner project version, create a single master notebook that walks through all pipelines end-to-end with clear section headers and business insights marked clearly.
