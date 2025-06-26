# Baseline Model

## Overview

The purpose of this stage is to establish a baseline model for the bakery sales forecasting project. A baseline model provides a simple yet informative point of comparison for evaluating the performance of more complex models.

## Feature Selection

The following features were selected based on their potential influence on sales patterns:

- Warengruppe (product group)  
- KielerWoche (binary indicator for event days)  
- DayOfWeek, Weekend, Month (temporal features)  
- TemperatureCategory, CloudCategory, WindCategory (categorized weather features)

These features capture seasonality, weather conditions, and special events that may impact sales.

## Implementation

We implemented a Linear Regression model as the baseline. The pipeline included:

- One-hot encoding for categorical features  
- Numerical features passed directly  
- Train/test split with 80% for training and 20% for testing

For comparison, we also implemented a Random Forest Regressor using the same preprocessing steps.

## Evaluation

### Linear Regression

- **Mean Squared Error**: 17,965.13  
- **R² Score**: 0.064  

The linear regression model performed poorly, indicating that the relationship between features and sales is likely non-linear.

### Random Forest Regressor

- **Mean Squared Error**: 5,736.76  
- **R² Score**: 0.729  

The random forest model significantly outperformed the baseline, capturing more complex interactions between the features.

This comparison confirms that a non-linear model like Random Forest is more appropriate for this forecasting task.

## Task

Create a Jupyter Notebook to conduct your implmentation of the baseline model.
