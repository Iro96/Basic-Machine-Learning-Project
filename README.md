# 🧠 General ML Dashboard

A reusable and minimal machine learning dashboard built with **Streamlit** that allows users to load a trained model, make predictions on tabular data, and visualize results.

---

## 📦 Features

- 🔌 Load any `scikit-learn`-compatible model (`.pkl`)
- 📊 Upload and preview CSV data
- 🤖 Generate predictions instantly
- 🛠️ Fully configurable with `config.yaml`
- 📓 Includes Jupyter notebook to train example model

---

## 🚀 Getting Started

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

## For use this project you use these command

### 1. Train the model
```bash
jupyter notebook notebooks/train_model.ipynb
```

### 2. Run the Streamlit App
```bash
streamlit run app/app.py
```
