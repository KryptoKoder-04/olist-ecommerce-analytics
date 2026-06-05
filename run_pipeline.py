#!/usr/bin/env python3
"""
Olist E-Commerce Project - Automated Pipeline Runner
Executes all notebooks in correct order and generates outputs
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*70}")
    print(f"  {text}")
    print(f"{'='*70}\n")

def check_requirements():
    """Check if all requirements are met"""
    print_header("CHECKING REQUIREMENTS")
    
    # Check Python version
    py_version = sys.version_info
    print(f"✓ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    
    # Check for required packages
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'plotly',
        'sklearn', 'jupyter', 'openpyxl'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (MISSING)")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("Run: python setup.py")
        return False
    
    # Check for data files
    print("\n✓ Checking data files...")
    required_files = [
        "data/olist_orders_dataset.csv",
        "data/olist_customers_dataset.csv",
        "data/olist_order_items_dataset.csv",
        "data/olist_products_dataset.csv",
        "data/olist_order_payments_dataset.csv",
        "data/olist_sellers_dataset.csv",
        "data/olist_geolocation_dataset.csv",
        "data/olist_order_reviews_dataset.csv",
        "data/product_category_name_translation.csv",
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing data files ({len(missing_files)}):")
        for f in missing_files:
            print(f"   - {f}")
        print("\nDownload from: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")
        return False
    
    print("✓ All data files found")
    return True

def create_directories():
    """Create output directories"""
    print_header("CREATING OUTPUT DIRECTORIES")
    
    dirs = [
        "output",
        "output/charts",
        "output/dashboards",
        "models",
        "logs"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ {dir_path}/")

def run_notebook(notebook_path, log_file):
    """Execute a single notebook using jupyter nbconvert"""
    print(f"\n→ Running {notebook_path}...")
    
    notebook_name = Path(notebook_path).stem
    output_notebook = f"output/notebooks/{notebook_name}_executed.ipynb"
    
    Path("output/notebooks").mkdir(parents=True, exist_ok=True)
    
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--ExecutePreprocessor.timeout=600",
        "--output", output_notebook,
        notebook_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print(f"  ✓ Completed successfully")
            with open(log_file, 'a') as f:
                f.write(f"✓ {notebook_name} - PASSED\n")
            return True
        else:
            print(f"  ✗ Error occurred")
            print(f"  STDERR: {result.stderr[:200]}")
            with open(log_file, 'a') as f:
                f.write(f"✗ {notebook_name} - FAILED\n")
                f.write(f"  {result.stderr[:500]}\n")
            return False
    
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout (>10 minutes)")
        with open(log_file, 'a') as f:
            f.write(f"✗ {notebook_name} - TIMEOUT\n")
        return False
    except Exception as e:
        print(f"  ✗ Exception: {e}")
        with open(log_file, 'a') as f:
            f.write(f"✗ {notebook_name} - ERROR: {e}\n")
        return False

def run_pipeline():
    """Run the complete data pipeline"""
    print_header("RUNNING DATA PIPELINE")
    
    # Notebooks in execution order
    notebooks = [
        "notebooks/Datacleaning.ipynb",
        "notebooks/Full-Analysis.ipynb",
        "notebooks/Charts_plots-1.ipynb",
        "notebooks/Charts_plots-Copy1.ipynb",
        "notebooks/DataProfiling_ DataQualityAssessment.ipynb",
        "notebooks/matplotlib-pipeline.ipynb",
        # Optional:
        # "notebooks/ML Churn Prediction.ipynb",
    ]
    
    # Create log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/run_{timestamp}.log"
    Path("logs").mkdir(exist_ok=True)
    
    with open(log_file, 'w') as f:
        f.write(f"Pipeline run started: {datetime.now()}\n")
        f.write(f"{'='*70}\n\n")
    
    results = {}
    passed = 0
    failed = 0
    
    for notebook_path in notebooks:
        if os.path.exists(notebook_path):
            success = run_notebook(notebook_path, log_file)
            notebook_name = Path(notebook_path).stem
            results[notebook_name] = success
            if success:
                passed += 1
            else:
                failed += 1
        else:
            print(f"\n✗ Not found: {notebook_path}")
            with open(log_file, 'a') as f:
                f.write(f"✗ {notebook_path} - NOT FOUND\n")
            failed += 1
    
    # Summary
    print_header("PIPELINE EXECUTION SUMMARY")
    print(f"✓ Passed: {passed}")
    print(f"✗ Failed: {failed}")
    print(f"Total: {passed + failed}")
    print(f"\nLog file: {log_file}")
    
    with open(log_file, 'a') as f:
        f.write(f"\n{'='*70}\n")
        f.write(f"Pipeline run completed: {datetime.now()}\n")
        f.write(f"Results: {passed} passed, {failed} failed\n")
    
    return failed == 0

def print_completion_message():
    """Print completion message"""
    print_header("COMPLETE!")
    print("✅ Pipeline execution finished!\n")
    print("Generated outputs:")
    print("  - data/df.csv (master dataset)")
    print("  - output/rfm_segments.csv")
    print("  - output/monthly_revenue.csv")
    print("  - output/charts/*.png (visualizations)")
    print("  - output/dashboards/*.html (interactive dashboards)")
    print("  - models/churn_model.pkl (ML model)")
    print("\nView results in:")
    print("  - output/notebooks/ (executed notebooks)")
    print("  - logs/ (execution logs)")
    print("\n" + "="*70)

def main():
    """Main execution function"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║   Olist E-Commerce Analytics - Automated Pipeline Runner      ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Requirements not met. Please run: python setup.py")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Run pipeline
    success = run_pipeline()
    
    # Print completion
    print_completion_message()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
