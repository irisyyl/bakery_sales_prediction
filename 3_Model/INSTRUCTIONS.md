# Model Definition and Evaluation

## Overview

In this stage, you will define, implement, and evaluate the machine learning model for your project. Your aim should be to improve upon the baseline model and try different approaches to achieve better performance.

## Guidelines

### Model Selection

We selected the **Random Forest Regressor** as our final model due to its ability to capture non-linear patterns and interactions in the data, which the linear regression model failed to do. Random Forest is robust to outliers, handles feature interactions implicitly, and generally performs well on structured tabular data like ours.

### Feature Engineering

The following features were selected based on their relevance to bakery sales:

- **Product group** (`Warengruppe`)
- **Temporal features**: `DayOfWeek`, `Weekend`, `Month`
- **Weather categories**: `TemperatureCategory`, `CloudCategory`, `WindCategory`
- **Event indicator**: `KielerWoche`
- **Seasonality**: `Season`
- **Holiday indicators**: `IsHoliday_lib`, `HolidayName`

Categorical features were one-hot encoded. Numerical features were passed through directly. Missing values in critical fields like `Umsatz` were dropped.

### Hyperparameter Tuning

We performed a grid search over the following hyperparameters:

- `n_estimators`: [50, 100]
- `max_depth`: [10, 20, None]
- `min_samples_split`: [2, 5]

Cross-validation was conducted with `cv=3` folds using the R² score as the evaluation metric.

### Implementation

The model pipeline consisted of:

- A **ColumnTransformer** to handle categorical and numerical preprocessing.
- A **RandomForestRegressor** as the final estimator.
- A **GridSearchCV** wrapper to find the best hyperparameter combination.

The dataset was split into training and testing sets with an 80/20 ratio.

### Evaluation Metrics

The model was evaluated using the following metrics:

- **MAPE (Mean Absolute Percentage Error)**: 0.1914
- **Mean Squared Error (MSE)**: 5,134.01
- **R² Score**: 0.758

These results show a measurable improvement over the baseline model. The final model captures the complexity of sales behavior significantly better than linear regression, which had an R² score of only 0.064.

## Task

Create a Jupyter Notebook to conduct your model implementation and evaluation.