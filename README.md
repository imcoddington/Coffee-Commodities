# Bayesian Lasso for Coffee Commodity Price Prediction

This repository accompanies the paper *“The Bayesian Lasso for Variable Selection and Prediction in Coffee Commodity Price Regression”* by Isabella Coddington and Alex Koutromanos. We apply the Bayesian Lasso to model and forecast ICE Arabica Coffee futures prices using technical and fundamental indicators. The model enables variable selection and shrinkage in a high-dimensional, collinear setting.

## 📈 Project Overview

Commodity price prediction is challenging due to:

- High dimensionality  
- Correlated predictors  
- Ambiguous indicator relevance  

The Bayesian Lasso addresses these challenges by offering:

- Automatic variable selection through shrinkage  
- Interpretability via posterior credible intervals  
- Probabilistic predictions with uncertainty quantification  

## 🧠 Model Summary

The Bayesian Lasso is formulated as a hierarchical model with:

- **Gaussian likelihood**:  
  $$
  y_t \mid \mu, \boldsymbol{\beta}, \sigma^2 \sim \mathcal{N}(\mu + X_t^\top \boldsymbol{\beta}, \sigma^2)
  $$

- **Laplace prior** on coefficients (expressed as a scale mixture of normals)  
- **Jeffreys priors** on noise variance $\sigma^2$ and global shrinkage $\lambda$  

Inference is performed via Gibbs sampling with closed-form full conditional distributions for:

- Intercept $\mu$  
- Coefficients $\boldsymbol{\beta}$  
- Noise variance $\sigma^2$  
- Local shrinkage scales $\tau_j^2$  
- Global shrinkage $\lambda$  

## 📊 Data

The dataset contains **1,202 daily observations** from **July 2020 to March 2025**, including:

- **Price variables**: Open, High, Low, Close  
- **Technical indicators**: MACD, Ichimoku, Bollinger Bands, Stochastic Oscillator  
- **Fundamental indicators**: Coffee inventories, exports, and import data from ICE, CECAFE, CONAB, and Chinese Customs  

Details of the indicator calculations and sources can be found in **Appendices B and C** of the paper.

## 🚀 Results

| Metric | Value |
|--------|--------|
| RMSE   | 2.76   |
| MAE    | 1.94   |
| R²     | 0.998  |

- **Predictive accuracy** is very high.
- Only **MACD** and **MACD Signal** had 95% credible intervals excluding 0.
- Posterior predictive intervals are tight and well-calibrated.
- The model significantly shrinks irrelevant/collinear predictors.

## 📂 Files

- `Coddington_Koutromanos_Final.pdf`: Final report with methods, derivations, and results.
- `Data_work.ipynb`: Jupyter notebook implementing the full Bayesian Lasso pipeline.
- `requirements.txt` *(optional)*: Add dependencies for reproducibility (e.g. `numpy`, `scipy`, `matplotlib`, `pandas`, `seaborn`, `pymc`, etc.)

## 📦 Installation

```bash
git clone https://github.com/imcoddington/Coffee-Commodities.git
cd Coffee-Commodities
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
