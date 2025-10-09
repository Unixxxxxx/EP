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

# Step 4: Export Results
with pd.ExcelWriter("sales_report.xlsx") as writer:
    data.to_excel(writer, sheet_name="Cleaned Data", index=False)
    summary_df.to_excel(writer, sheet_name="Summary Report", index=False)

print("\n Analysis Complete! Report saved as 'sales_report.xlsx'.")
