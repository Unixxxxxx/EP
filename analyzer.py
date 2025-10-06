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

#Analyzer data

summary = {
    "Total Sales (₹)": [data['Total Sales'].sum()],
    "Average Sale per Region (₹)": [data.groupby('Region')['Total Sales'].mean().mean()],
    "Top Selling Product": [data.groupby('Product')['Total Sales'].sum().idxmax()],
    "Best Region": [data.groupby('Region')['Total Sales'].sum().idxmax()]
}

summary_df = pd.DataFrame(summary)
print("Sales Summary:")
print(summary_df)
