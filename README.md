# General ML Dashboard

[![madewithlove](https://img.shields.io/badge/made_with-%E2%9D%A4-red?style=for-the-badge&labelColor=orange)](https://github.com/Iro96/Basic-Machine-Learning-Project)
[![GitHub license](https://img.shields.io/github/license/Iro96/Basic-Machine-Learning-Project?style=for-the-badge)](https://github.com/Iro96/Basic-Machine-Learning-Project/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Iro96/Basic-Machine-Learning-Project?style=for-the-badge)](https://github.com/Iro96/Basic-Machine-Learning-Project/issues)

A reusable and minimal machine learning dashboard built with **Streamlit** that allows users to load a trained model, make predictions on tabular data, and visualize results.

---

## Features

- Load any `scikit-learn`-compatible model (`.pkl`)
- Upload and preview CSV data
- Generate predictions instantly
- Fully configurable with `config.yaml`
- Includes Jupyter notebook to train example model

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/general-ml-dashboard.git
cd general-ml-dashboard
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required Python packages
```
pip install -r requirements.txt
```

## Usage

### 1. Train the model
```bash
jupyter notebook notebooks/train_model.ipynb
```

### 2. Run the Streamlit App
```bash
streamlit run app/app.py
```
