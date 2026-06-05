# 🚀 PROJECT SETUP & EXECUTION GUIDE

## ⚠️ Prerequisites

Before you can run this project, you need:

1. **Python 3.11+** ✅ (You have 3.13)
2. **Required packages** (pandas, numpy, matplotlib, seaborn, plotly, jupyter)
3. **Raw Olist CSV data** from Kaggle (9 files)

---

## 📥 Step 1: Download Raw Data from Kaggle

### Option A: Using Kaggle CLI (Recommended)

```bash
# 1. Install Kaggle CLI
pip install kaggle

# 2. Set up Kaggle API credentials
# Go to: https://www.kaggle.com/settings/account
# Click "Create New API Token" → saves kaggle.json
# Place it in: C:\Users\[YourUsername]\.kaggle\kaggle.json

# 3. Download the dataset
kaggle datasets download -d olistbr/brazilian-ecommerce

# 4. Extract to data folder
mkdir data
cd data
unzip brazilian-ecommerce.zip
rm brazilian-ecommerce.zip
```

### Option B: Manual Download

1. Visit: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
2. Click **Download** button (requires Kaggle account)
3. Extract ZIP file to `data/` folder in project root
4. Verify you have these 9 files:
   - `olist_orders_dataset.csv`
   - `olist_customers_dataset.csv`
   - `olist_order_items_dataset.csv`
   - `olist_products_dataset.csv`
   - `olist_order_payments_dataset.csv`
   - `olist_sellers_dataset.csv`
   - `olist_geolocation_dataset.csv`
   - `olist_order_reviews_dataset.csv`
   - `product_category_name_translation.csv`

---

## 📦 Step 2: Install Python Packages

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

# Install all required packages
pip install -r requirements.txt
```

---

## ▶️ Step 3: Run the Project

### Option A: Run All Notebooks in Sequence (Recommended)

```bash
jupyter notebook
```

Then manually run notebooks in this order:

1. **Datacleaning.ipynb** — Loads raw data, cleans, outputs `df.csv`
2. **Full-Analysis.ipynb** — Feature engineering, RFM, CLV, summary tables
3. **Charts_plots-1.ipynb** — Static visualizations (matplotlib)
4. **Charts_plots-Copy1.ipynb** — Regional & product charts
5. **DataProfiling_ DataQualityAssessment.ipynb** — Data quality report
6. **matplotlib-pipeline.ipynb** — Interactive plots (plotly)
7. **ML Churn Prediction.ipynb** — ML modeling (optional)

### Option B: Run Python Script (Auto-Run All)

```bash
python run_pipeline.py
```

(Script will be created next)

---

## ✅ Verification

After running, you should have:

- ✅ `data/df.csv` — Master dataset (115K rows)
- ✅ `output/rfm_segments.csv` — RFM analysis
- ✅ `output/monthly_revenue.csv` — Monthly trends
- ✅ `output/charts/` — PNG visualizations
- ✅ `output/dashboard.html` — Interactive dashboard
- ✅ `models/churn_model.pkl` — Trained ML model

---

## 🐛 Troubleshooting

### "Module not found: pandas"
```bash
pip install -r requirements.txt
```

### "File not found: olist_orders_dataset.csv"
- Download data from Kaggle (see Step 1)
- Ensure CSVs are in `data/` folder

### "Path doesn't exist"
- Notebook has hardcoded Linux path
- Edit first notebook cell to use local `data/` folder

### "Permission denied" (Windows)
- Run terminal as Administrator
- Or use: `python -m pip install --user pandas`

---

## 📊 Expected Output

When complete, you'll have:

1. **Clean data:** `df.csv` with 115K rows, 44 columns
2. **RFM segments:** 5 customer segments
3. **KPIs:** Revenue, profit, AOV, repeat rate
4. **Visualizations:** 50+ charts
5. **Dashboard:** Interactive HTML file
6. **ML model:** Churn prediction scores

---

**Total runtime:** ~15-20 minutes (depending on your system)

Last Updated: June 2026
