# Data Preparation

This is a description for preparing data for course project bakery sales prediction. Here is the outline and approach for data preparation step. 

# Project backbone 

Outline: 

1. import 3 project data from course GitHub [Intro to DS and ML](https://github.com/opencampus-sh/einfuehrung-in-data-science-und-ml.git)
    - `kiwo.csv` (dates of Kieler Woche from 2012 to 2019)
    - `umsatzdaten_gekuerzt.csv` (sales table with id, dates, bakery types from 2013 to 2017) 
    - `wetter.csv` (weather data from 2012 to 2019)

2. Merge 3 datasets into 1 dataframe. 

3. Data transformation. 

    - **Date**: 
        * categorized `"datum"` into year, month, week, day
        * removed rows with missing dates

    - **Weather**: 
        * categorize temperature into "very cold", "cold", "mild", "warm", "hot"
        * categorize cloud cover into "clear", "partly cloudy", "cloudy", "overcast"
        * categorize wind speed into "light", "moderate", "strong", "very strong"

    - **Holiday**: 
        * add labels for public holidays in Schleswig-Hoslstein 

    - **Seasonality**: 
        * categorize seasons based on date and temperature
            Primary criteria (month-based):
            - Winter: months 12, 1, 2
            - Spring: months 3, 4, 5  
            - Summer: months 6, 7, 8
            - Autumn: months 9, 10, 11
            
            Backup criteria (temperature-based):
            - Winter: temp ≤ 5°C
            - Spring: temp 5-12°C
            - Summer: temp 12-18°C
            - Autumn: temp > 18°C

4. Split time-series data into training, validation and test set based on date: 
    - training set from 01.07.2013 to 31.07.2017,
    - validation set from 01.08.2017 to 31.07.2018, and
    - test set from 01.08.2018 to 31.07.2019.

# Updates 

> Keep this section Up-to-date

[ ] Data transformation: 
    [x] special events, e.g. Kieler Woche
    [x] holidays, seasons (based on dates and temperature)
    [ ] product change that leads to sales change? E.g. Introduction of new bakery type. 