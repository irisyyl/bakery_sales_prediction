# Model Definition and Evaluation

## Overview

In this stage, you will define, implement, and evaluate the machine learning model for your project. Your aim should be to improve upon the baseline model and try different approaches to achieve better performance.

#### Guidelines - RANDOM FOREST MODEL ####

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

###### ------------------------------ ########


#### Guidelines - LIGHT-GBM MODEL ####

### Model Selection

We chose **LightGBM** (Light Gradient Boosted Machine) for its efficiency and performance on structured tabular data. It's particularly effective with mixed feature types, handles missing values internally, and supports categorical features natively. These characteristics make it well-suited for our sales prediction task.

### Feature Engineering

Across iterations, we enhanced the dataset with date-based and event-related features:
- **LightGBM 1**: Basic date features like `dayofweek`, `month`, and `is_weekend`.
- **LightGBM 3**: Added weekday indicators (`is_monday`, `is_friday`) and tuned `learning_rate` and `num_leaves`.
- **LightGBM 4**: Introduced feature interaction (`month_weekend`) and defined categorical features (`dayofweek`, `month`).
- **LightGBM 5** (final): Added **`weekofyear`**, **`dayofyear`**, and `KielerWoche`, which captured seasonal patterns and local events. These enhancements were crucial to improving performance.

### Hyperparameter Tuning

Each iteration adjusted model complexity:
- `n_estimators` increased from 200 to 1000.
- `learning_rate` reduced from 0.05 to 0.02.
- `num_leaves` increased to allow more complex splits (from 31 to 128).
- Added `max_depth`, `min_child_samples`, `subsample`, and `colsample_bytree` for regularization.
- Introduced **early stopping** in the final model to avoid overfitting by stopping training when no improvement is observed.

### Implementation

Each model was trained **per `Warengruppe` (product group)** using the same pipeline:
- Merge external data (`wetter.csv`, `kiwo.csv`).
- Generate features.
- Train/test split.
- Train LightGBM with relevant parameters.
- Predict on test set and build submission.

The final model (LightGBM 5) used the following configuration:

```python
model = lgb.LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.02,
    num_leaves=128,
    max_depth=10,
    min_child_samples=10,
    subsample=0.85,
    colsample_bytree=0.85,
    objective="regression",
    random_state=42
)

model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    eval_metric="mape",
    categorical_feature=["dayofweek", "month", "weekofyear"],
    callbacks=[lgb.early_stopping(stopping_rounds=25)],
)
```

### Evaluation Metrics

We used Mean Absolute Percentage Error (MAPE) as our primary metric.

### Performance Improvement Overview

**LightGBM 1 – Baseline (MAPE: 0.24107)**
We started with a simple model using basic weather (Bewoelkung, Temperatur, Windgeschwindigkeit, Wettercode) and date features (dayofweek, month, is_weekend). The model used default parameters with 200 estimators. This served as a foundation for further improvements.

**LightGBM 2 – Lag Feature and Log Transformation (MAPE: 0.27033)**
In this version, we introduced a lag feature (Umsatz_lag1) and applied a log1p transformation to the target variable to reduce skew. However, the lag value could not be reliably calculated for the test set, and the log transform added complexity. As a result, performance deteriorated compared to the baseline.

**LightGBM 3 – Parameter Tuning (MAPE: 0.23236)**
Here we removed the lag and log transformations and instead focused on tuning the model. We increased the number of estimators to 300, added a learning rate of 0.05, and set num_leaves=31. These adjustments improved the model’s generalization and reduced MAPE significantly from version 2.

**LightGBM 4 – Feature Engineering and Regularization (MAPE: 0.22843)**
This version expanded the feature set by adding is_monday, is_friday, and an interaction feature month_weekend. We also set dayofweek and month as categorical features and used a more regularized model with parameters like num_leaves=64, max_depth=8, and subsampling. This led to further improvement.

**LightGBM 5 – Final Model with Seasonality and Early Stopping (MAPE: 0.18391)**
The final version included seasonal date features: weekofyear and dayofyear, which helped the model capture long-term patterns. We tuned the model further with num_leaves=128, max_depth=10, learning_rate=0.02, and n_estimators=1000. We also applied early stopping with validation to avoid overfitting. This led to the best result overall, with a significant performance gain of ~24% compared to LightGBM 4.

In summary, across iterations, we observed the following trends:

	•	LightGBM 1 served as our baseline with a MAPE of 0.24107.
	•	LightGBM 2, despite additional features, increased MAPE to 0.27033 due to poor generalization.
	•	LightGBM 3 improved the result to 0.23236 through better parameter tuning and weekday encoding.
	•	LightGBM 4 reduced the error further to 0.22843 by leveraging feature interactions and categorical encodings.
	•	LightGBM 5 achieved the best performance with a MAPE of 0.18391 by introducing deeper seasonal features and fine-tuned parameters with early stopping.

These results show a consistent improvement in the model’s predictive capability as we refined both the input features and the training strategy.

### General Conclusion

Among the three models tested—Linear Regression, Random Forest, and LightGBM—the LightGBM model clearly outperformed the others in terms of accuracy and adaptability.
	•	Linear Regression performed poorly because it assumes a linear relationship between features and sales, which is too simplistic for the complex patterns in the data.
	•	Random Forest handled non-linear interactions better and showed strong improvement, but it lacks built-in support for categorical features and is less efficient with larger datasets.
	•	LightGBM delivered the best performance because it:
	•	Handles categorical features natively
	•	Is faster and more scalable than Random Forest
	•	Supports advanced training features like early stopping and fine-tuned regularization
	•	Performs well with complex patterns and time-based features

**Conclusion:** LightGBM was the most suitable model for this task, achieving the lowest MAPE (0.18391) and offering the best balance of performance, flexibility, and efficiency.