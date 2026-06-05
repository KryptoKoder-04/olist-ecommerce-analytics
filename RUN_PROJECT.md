# ▶️ HOW TO RUN THIS PROJECT

## 📋 Quick Start (3 Steps)

### Step 1: Setup Environment
```bash
python setup.py
```
This will:
- ✅ Install all required Python packages
- ✅ Create output directories
- ✅ Check for data files

### Step 2: Download Data
Go to: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Click **Download**
- Extract ZIP file to `data/` folder

### Step 3: Run Pipeline
```bash
python run_pipeline.py
```
Or run notebooks manually:
```bash
jupyter notebook
```

---

## 📥 Download Data (Detailed)

### Option A: Kaggle CLI (Fastest)

```bash
# Install Kaggle CLI
pip install kaggle

# Get API credentials from https://www.kaggle.com/settings/account
# Click "Create New API Token" and save kaggle.json to ~/.kaggle/

# Download dataset
kaggle datasets download -d olistbr/brazilian-ecommerce
unzip brazilian-ecommerce.zip -d data/
```

### Option B: Manual Download

1. Visit: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
2. Sign in to Kaggle account
3. Click blue **Download** button
4. Wait for ZIP download (~200 MB)
5. Extract to `data/` folder

**Verify:** You should see these 9 files in `data/`:
```
olist_orders_dataset.csv
olist_customers_dataset.csv
olist_order_items_dataset.csv
olist_products_dataset.csv
olist_order_payments_dataset.csv
olist_sellers_dataset.csv
olist_geolocation_dataset.csv
olist_order_reviews_dataset.csv
product_category_name_translation.csv
```

---

## ⚙️ Setup & Installation

### Windows

**Option 1: Batch Script (Easiest)**
```bash
setup.bat
```

**Option 2: Python Script**
```bash
python setup.py
```

**Option 3: Manual**
```bash
python -m pip install -r requirements.txt
mkdir data output output\charts models logs
```

### Mac / Linux

```bash
python setup.py
```

---

## ▶️ Running the Project

### Option A: Automated (Recommended)

```bash
python run_pipeline.py
```

This will:
1. Check all requirements
2. Execute all notebooks in order
3. Generate outputs automatically
4. Create execution log

**Expected runtime:** 15-30 minutes

### Option B: Manual (Interactive)

```bash
jupyter notebook
```

Then run notebooks in this order:

1. **Datacleaning.ipynb** (5 min)
   - Loads raw data
   - Cleans and merges 9 tables
   - Outputs: `data/df.csv`

2. **Full-Analysis.ipynb** (5 min)
   - Feature engineering (15+ metrics)
   - RFM segmentation
   - CLV calculation
   - Outputs: summary tables

3. **Charts_plots-1.ipynb** (3 min)
   - Static visualizations
   - Revenue/profit trends
   - Category analysis

4. **Charts_plots-Copy1.ipynb** (3 min)
   - Product and regional charts
   - State-wise analysis
   - Delivery performance

5. **DataProfiling_ DataQualityAssessment.ipynb** (2 min)
   - Data quality report
   - Statistical summary
   - Distributions

6. **matplotlib-pipeline.ipynb** (5 min)
   - Interactive Plotly charts
   - HTML dashboard
   - Outputs: `output/dashboards/dashboard.html`

7. **ML Churn Prediction.ipynb** (5 min - Optional)
   - ML model training
   - Feature selection
   - Risk scoring

---

## 📊 Expected Outputs

After running, you'll find:

```
project-root/
├── data/
│   ├── *.csv (raw Olist data - 9 files)
│   └── df.csv (master dataset - 115K rows)
├── output/
│   ├── rfm_segments.csv
│   ├── monthly_revenue.csv
│   ├── charts/
│   │   ├── revenue_trend.png
│   │   ├── top_categories.png
│   │   ├── state_performance.png
│   │   └── ... (50+ charts)
│   └── dashboards/
│       └── dashboard.html (interactive!)
├── models/
│   └── churn_model.pkl (ML model)
├── logs/
│   └── run_YYYYMMDD_HHMMSS.log
└── output/notebooks/
    └── *_executed.ipynb (executed notebooks)
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
```bash
python setup.py
```

Or manually:
```bash
python -m pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter
```

---

### "FileNotFoundError: olist_orders_dataset.csv"

**Solution:**
1. Download data from Kaggle (see "Download Data" section)
2. Extract to `data/` folder
3. Verify 9 CSV files are present

---

### "Permission denied" (Windows)

**Solution:**
- Run terminal as Administrator
- Or use: `python -m pip install --user pandas`

---

### Notebook hangs or times out

**Solution:**
1. Close other programs to free memory
2. Restart Jupyter kernel
3. Or use: `python run_pipeline.py --skip-ml` (to skip ML notebook)

---

### "Kernel died" in Jupyter

**Solution:**
1. Restart kernel: Kernel → Restart
2. Or run: `jupyter notebook --no-browser --ip=127.0.0.1`

---

## 📈 What Each Notebook Does

| Notebook | Purpose | Time | Outputs |
|----------|---------|------|---------|
| Datacleaning | Load, clean, merge 9 tables | 5 min | `df.csv` |
| Full-Analysis | Feature engineering, RFM, CLV | 5 min | Summary tables |
| Charts_plots-1 | Revenue/profit/category charts | 3 min | PNG files |
| Charts_plots-Copy1 | Regional and product charts | 3 min | PNG files |
| DataProfiling | Quality assessment | 2 min | Report |
| matplotlib-pipeline | Interactive Plotly dashboard | 5 min | `dashboard.html` |
| ML Churn Prediction | ML model training (optional) | 5 min | `churn_model.pkl` |

**Total:** ~28 minutes

---

## 🎯 Verification Checklist

After running, verify you have:

- [ ] ✅ `data/df.csv` (115K+ rows)
- [ ] ✅ `output/rfm_segments.csv`
- [ ] ✅ `output/monthly_revenue.csv`
- [ ] ✅ `output/charts/` (50+ PNG files)
- [ ] ✅ `output/dashboards/dashboard.html`
- [ ] ✅ `models/churn_model.pkl`
- [ ] ✅ `logs/` (execution log)

---

## 💡 Tips

1. **First time?** Use automated runner:
   ```bash
   python run_pipeline.py
   ```

2. **Want to explore?** Use Jupyter:
   ```bash
   jupyter notebook
   ```

3. **Need logs?** Check:
   ```bash
   logs/run_YYYYMMDD_HHMMSS.log
   ```

4. **Want to modify?** Edit notebook cells, then:
   ```bash
   jupyter notebook
   ```

5. **Share results?** Upload `output/dashboards/dashboard.html` to web server

---

## 🔗 More Information

- [SETUP_GUIDE.md](SETUP_GUIDE.md) — Detailed setup instructions
- [README.md](README.md) — Project overview
- [BUSINESS_INSIGHTS.md](BUSINESS_INSIGHTS.md) — Business context
- [INTERVIEW_PREP.md](INTERVIEW_PREP.md) — Interview Q&A
- [sql/README.md](sql/README.md) — SQL queries explanation
- [notebooks/README.md](notebooks/README.md) — Notebook explanations

---

## ✅ Success!

Once you see "✅ COMPLETE!" in terminal, your project is ready!

Check `output/` folder for all generated files and dashboards.

**Next:** View the interactive dashboard:
```bash
open output/dashboards/dashboard.html  # Mac
xdg-open output/dashboards/dashboard.html  # Linux
start output/dashboards/dashboard.html  # Windows
```

---

Last Updated: June 2026
