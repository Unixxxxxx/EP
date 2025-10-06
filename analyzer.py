import pandas as pd

#Load Excel data
data = pd.read_excel("sales_data.xlsx")

print("Original Data")
print(data.head())


#Clean Data
data.dropna(inplace=True)
data['Total Sales'] = data['Units Sold'] * data['Unit Price']

print("Cleaned Data With Totle Sales:")
print(data.head())
