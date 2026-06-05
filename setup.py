#!/usr/bin/env python3
"""
Olist E-Commerce Project - Setup Script
Installs dependencies and creates required directories
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def install_packages():
    """Install required Python packages"""
    print_header("STEP 1: Installing Python Packages")
    
    packages = [
        "pandas==2.2.0",
        "numpy==1.26.3",
        "matplotlib==3.8.2",
        "seaborn==0.13.0",
        "plotly==5.18.0",
        "scikit-learn==1.3.2",
        "jupyter==1.0.0",
        "ipython==8.18.1",
        "openpyxl==3.11.0",
    ]
    
    print("Installing packages (this may take a few minutes)...")
    print()
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", 
            "pip", "setuptools", "wheel"
        ])
        
        for package in packages:
            print(f"  Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package
            ])
        
        print("\n✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing packages: {e}")
        return False

def create_directories():
    """Create required project directories"""
    print_header("STEP 2: Creating Project Directories")
    
    dirs = [
        "data",
        "output",
        "output/charts",
        "output/dashboards",
        "models",
        "logs"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Created: {dir_path}/")
    
    print("\n✅ All directories created!")

def check_data_files():
    """Check if raw data files exist"""
    print_header("STEP 3: Checking for Raw Data Files")
    
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
    
    missing = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✓ Found: {file_path}")
        else:
            print(f"  ✗ Missing: {file_path}")
            missing.append(file_path)
    
    if missing:
        print(f"\n⚠️  {len(missing)} data files missing!")
        print("\nTo download data:")
        print("  1. Go to: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")
        print("  2. Click 'Download'")
        print("  3. Extract ZIP to 'data/' folder")
        print("\nOr use Kaggle CLI:")
        print("  $ pip install kaggle")
        print("  $ kaggle datasets download -d olistbr/brazilian-ecommerce")
        print("  $ unzip brazilian-ecommerce.zip -d data/")
        return False
    else:
        print("\n✅ All data files found!")
        return True

def print_next_steps(data_ready):
    """Print next steps for user"""
    print_header("SETUP COMPLETE!")
    
    print("✅ Environment is ready!\n")
    
    if not data_ready:
        print("⚠️  You still need to download raw data files.")
        print("\nAfter downloading data, run:")
        print("  $ jupyter notebook")
        print("\nThen open notebooks in this order:")
    else:
        print("✅ All data files present!\n")
        print("To run the project:")
        print("  $ jupyter notebook")
        print("\nThen open and run notebooks in this order:")
    
    print("\n  1. Datacleaning.ipynb")
    print("  2. Full-Analysis.ipynb")
    print("  3. Charts_plots-1.ipynb")
    print("  4. Charts_plots-Copy1.ipynb")
    print("  5. DataProfiling_ DataQualityAssessment.ipynb")
    print("  6. matplotlib-pipeline.ipynb")
    print("  7. ML Churn Prediction.ipynb (optional)")
    print("\n" + "="*60)

def main():
    """Main setup function"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║    Olist E-Commerce Analytics Project - Setup Script      ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    # Install packages
    if not install_packages():
        print("\n❌ Setup failed. Please fix package installation errors.")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Check for data files
    data_ready = check_data_files()
    
    # Print next steps
    print_next_steps(data_ready)
    
    print("\nFor help, see SETUP_GUIDE.md")

if __name__ == "__main__":
    main()
