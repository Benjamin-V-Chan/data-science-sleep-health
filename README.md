# data-science-sleep-health

# Project Overview
This project analyzes sleep health and lifestyle factors using data science and machine learning techniques. It includes data preprocessing, exploratory data analysis (EDA), predictive modeling, and visualization.

# Folder Structure
```
project-root/
├── data/               # Contains raw and processed datasets
│   ├── Sleep_health_and_lifestyle_dataset.csv  # Raw dataset
│   ├── processed_sleep_data.csv                # Preprocessed dataset
├── scripts/            # Contains data processing and analysis scripts
│   ├── 01_preprocess.py # Data preprocessing
│   ├── 02_eda.py       # Exploratory Data Analysis
│   ├── 03_model.py     # Model training and evaluation
│   ├── 04_visualize.py # Data visualization
├── outputs/            # Stores generated reports, models, and plots
│   ├── classification_report.txt
│   ├── sleep_disorder_model.pkl
│   ├── *.png (visualization images)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

## 2. Run Preprocessing:
Processes the raw dataset, handles missing values, encodes categorical variables, and normalizes numerical values.
```bash
python scripts/01_preprocess.py
```

## 3. Perform Exploratory Data Analysis:
Generates summary statistics, histograms, and a correlation heatmap.
```bash
python scripts/02_eda.py
```

## 4. Train and Evaluate Model:
Trains a machine learning model to predict sleep disorders and outputs classification metrics.
```bash
python scripts/03_model.py
```

## 5. Generate Visualizations:
Creates key visualizations related to sleep and lifestyle factors.
```bash
python scripts/04_visualize.py
```

# Requirements
- Python 3.8+
- Required libraries listed in `requirements.txt`

# Acknowledgments
**Dataset Name:** Sleep Health and Lifestyle Dataset  
**Dataset Author:** Laksika Tharmalingam  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)