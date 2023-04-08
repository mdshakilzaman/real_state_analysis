# importing packages for testing
import pandas as pd

# reading data file
data = pd.read_csv('Real_Estate_Sales_2001-2020_GL.csv')

#printing first 5 rows
print(data.head())

#listing the columns
for col in data.columns:
    print(col)