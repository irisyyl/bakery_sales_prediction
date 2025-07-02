# Dataset Characteristics

## Overview

In this stage, we explored and analyzed the merged dataset that combines bakery sales, weather conditions, and special event data (Kieler Woche). This step is crucial to understand patterns, trends, and potential predictors before building any forecasting model. Using tables, visualizations, and statistical summaries, we examined key aspects of the data.

---

## Dataset Overview

- The dataset contains **10,119 rows** and **18 columns**.
- It includes daily records from multiple sources: sales data (`Umsatz`), weather data (e.g., `Temperatur`, `Bewoelkung`, `Windgeschwindigkeit`), and the Kieler Woche event flag.
- Several new features were created: weekday, weekend indicator, week number, and categorized weather variables.

---

## Missing Values

- Some important columns have missing values:
  - `Umsatz`, `Warengruppe`, and `id`: 785 missing values
  - `Bewoelkung`, `Temperatur`, `Windgeschwindigkeit`: minor gaps (16–71)
  - `Wettercode`: large number of missing values (2,538)

The dataset is mostly complete, but rows with missing sales and temperature data may need to be dropped or imputed before modeling.

---

## Feature Distributions

- **Numerical Features:**
  - `Temperatur` has a normal-like distribution, mostly between 0–20°C.
  - `Windgeschwindigkeit` is right-skewed, with most days under 20 km/h.
  - `Umsatz` is also right-skewed, with occasional high spikes.
  - `Bewoelkung` shows frequent values near full cloud cover (7–8).

- **Categorical Features:**
  - Most days are labeled as "mild" or "cold".
  - Very few records belong to the `Kieler Woche` period.

These distributions help identify common conditions and rare cases (like sales peaks or weather extremes).

---

## Correlations

- `Umsatz` has a **moderate positive correlation** with:
  - `Temperatur` (0.22): warmer days may lead to higher sales.
  - `Weekend` (0.16): weekends tend to show slightly higher sales.
- Other variables show weak or no significant correlation with sales.
- `Bewoelkung` and `Temperatur` are negatively correlated (-0.38), as expected (cloudy days tend to be colder).

The correlation matrix provides initial hints on which features might be useful in the forecasting model.

---

## Task

Create a Jupyter Notebook to conduct your analysis of the dataset characteristics.
