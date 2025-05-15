# import library
import pandas as pd # for data manipulation
import pyodide_http # for loading external files from http 
pyodide_http.patch_all() # for loading external files from http 
import matplotlib.pyplot as plt # for plottings 

# import data 
weather = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv')
kiwo = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/kiwo.csv')
sale = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv')

# merge data 
sale_weather_kiwo = sale.merge(weather, on='Datum', how='outer', suffixes = ("_sale", "_weather")) \
.merge(kiwo, on='Datum', how='outer', suffixes = ("", "_kiwo"))