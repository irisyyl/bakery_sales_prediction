# Sales Forecasting for a Bakery Branch

## Repository Link

https://github.com/irisyyl/bakery_sales_prediction

## Description

This project focuses on sales forecasting for a bakery branch, utilizing historical sales data spanning from July 1, 2013, to July 30, 2018, to inform inventory and staffing decisions. We aim to predict future sales for six specific product categories: Bread, Rolls, Croissants, Confectionery, Cakes, and Seasonal Bread. Our methodology integrates statistical and machine learning techniques, beginning with a baseline linear regression model to identify fundamental trends, and progressing to a sophisticated neural network designed to discern more nuanced patterns and enhance forecast precision. The initiative encompasses data preparation, crafting bar charts with confidence intervals for visualization, and fine-tuning models to assess their performance on test data from August 1, 2018, to July 30, 2019, using the Mean Absolute Percentage Error (MAPE) metric for each product category.

### Task Type

Regression

### Results Summary

-   **Best Model:** lightGBM 5
-   **Evaluation Metric:** MAPE
-   **Overall MAPE:** 18.39%
-   **Result by Category** (Warengruppe):
    -   **Bread** (1): 0.2108%
    -   **Rolls** (2): 0.1324%
    -   **Croissant** (3): 0.1869%
    -   **Confectionery** (4): 0.2190%
    -   **Cake** (5): 0.1457%
    -   **Seasonal Bread** (6): 0.3206%

## Documentation

1.  [**Data Import and Preparation**](0_DataPreparation/01_merge_data.ipynb)
3.  [**Dataset Characteristics (Barcharts)**](1_DatasetCharacteristics/Bakery_Sales_Dataset_Characteristics.ipynb)
4.  [**Baseline Model - linear regression**](2_BaselineModel/baseline_model_linear_regression.ipynb)
5.  [**Baseline Model - random forest**](2_BaselineModel/baseline_model_random_forest.ipynb)
6.  [**Model Definition and Evaluation**](3_Model/final_model_lightbm_v5.ipynb)
6.  [**Presentation**](4_Presentation/README.md)

## Cover Image

![](CoverImage/slides_cover_image.png)
