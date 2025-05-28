# 🧠 Myntra Trend-Demand Forecasting

A real-time AI-based forecasting solution to predict fast fashion demand accurately and enable dynamic production and procurement decisions.

---
## 👥 Team A.O
- **Arshia Moudgil**   
- **Ojasvi Padhiar**

---

## 🔍 Solution Overview

We leverage **real-time data** and **machine learning models (LSTM & SARIMAX)** to forecast trending fashion attributes like **colors** and **themes**. This enables better demand prediction and smarter inventory management.

---

## 📊 Datasets

- Real-time fashion trend datasets (e.g. colors and themes)
- Augmented with **synthetic data** to boost model generalization

---
## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras** – for LSTM
- **statsmodels** – for SARIMAX
- **pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Gemini AI** – for auto-generated textual insights

---
## 🧱 Project Architecture

### 1. Data Preparation
- Encode categorical variables
- Normalize numerical values
- Time Series Decomposition
- Generate synthetic data
- Sequence generation for LSTM
- Train/Test split

### 2. Model Building
- **LSTM**: Sequential model trained on historical sequences
- **SARIMAX**: Traditional time-series model for seasonality + trend

### 3. Evaluation & Forecasting
- MSE calculated for both models
- Combine predictions from both models
- Forecast future trends
- Generate insights using Gemini

---
