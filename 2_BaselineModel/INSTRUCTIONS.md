# Baseline Model

## Overview

The purpose of this stage is to establish a baseline model for the bakery sales forecasting project. A baseline model provides a simple yet informative point of comparison for evaluating the performance of more complex models.

## Feature Selection

The following features were selected based on their potential influence on sales patterns:

- **Warengruppe** (product group)  
- **KielerWoche** (binary indicator for event days)  
- **DayOfWeek**, **Weekend**, **Month** (temporal features)  
- **TemperatureCategory**, **CloudCategory**, **WindCategory** (categorized weather features)  
- **IsHoliday_lib**, **Season** (categorical and binary features reflecting holidays and seasons)

These features capture seasonality, weather conditions, and special events that may impact sales.

## Implementation

Two baseline models were implemented:

1. **Linear Regression** with direct numerical features:  
   - `Temperatur`, `Bewoelkung`, `Windgeschwindigkeit`, `Weekend`, `KielerWoche`

2. **Random Forest Regressor** using a preprocessing pipeline:  
   - One-hot encoding for categorical features  
   - Numerical features passed directly  
   - Train/test split with 80% training and 20% testing

## Evaluation

### Linear Regression

- **Mean Squared Error**: 17,950.51  
- **R² Score**: 0.064  

The linear regression model performed poorly, indicating that the relationship between features and sales is likely non-linear.

### Random Forest Regressor

- **MAPE**: 0.2030  
- **Mean Squared Error**: 5,579.66  
- **R² Score**: 0.737  

The random forest model significantly outperformed linear regression, capturing more complex interactions between the features. This suggests that non-linear models are more appropriate for this forecasting task.
