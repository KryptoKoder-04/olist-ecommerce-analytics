@echo off
REM ========================================
REM Olist E-Commerce Project Setup Script
REM Windows Batch Version
REM ========================================

echo.
echo [1/3] Installing Python packages...
echo.

python -m pip install --upgrade pip setuptools wheel

python -m pip install ^
    pandas==2.2.0 ^
    numpy==1.26.3 ^
    matplotlib==3.8.2 ^
    seaborn==0.13.0 ^
    plotly==5.18.0 ^
    scikit-learn==1.3.2 ^
    jupyter==1.0.0 ^
    ipython==8.18.1 ^
    openpyxl==3.11.0

echo.
echo [2/3] Creating project directories...
echo.

if not exist "data" mkdir data
if not exist "output" mkdir output
if not exist "output\charts" mkdir output\charts
if not exist "models" mkdir models

echo.
echo [3/3] Setup complete!
echo.
echo Next steps:
echo 1. Download raw CSV data from Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
echo 2. Extract CSV files to 'data' folder
echo 3. Run: jupyter notebook
echo 4. Open and run notebooks in order:
echo    - Datacleaning.ipynb
echo    - Full-Analysis.ipynb
echo    - Charts_plots-1.ipynb
echo    - etc.
echo.
pause
