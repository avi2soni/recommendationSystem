import pandas as pd

df=pd.read_csv("evDB.csv")
print("The dataframe is:")
print(df)

#filtering based on range greater than 300
rangeItem = df[df['Range'] > 300]
print(rangeItem['Range'])
print(rangeItem[['Brand', 'Model', 'Range']])

#filtering based on range greater than 300 and price less than $50,000
rangeItem = df[(df['Range'] > 300) & (df['Price After Credit'] < 50000)]
print(rangeItem[['Brand', 'Model', 'Range', 'Price After Credit']])

#filtering based on battery size
rangeItem = df[df['Battery Size'] == 98.8]
print(rangeItem[['Brand', 'Model', 'Battery Size']])

#filtering based on range greater than 300 and price less than $50,000 and type sedan
# rangeItem = df[(df['Range'] > 300) & (df['Price After Credit'] < 50000) & (df['Type'] == 'Sedan')]
# print(rangeItem[['Brand', 'Model', 'Range', 'Price After Credit', 'Type']])
# print(rangeItem)


#what is your desired range, price, and vehicle type?
range = input("Please enter the minimum range for the desired vehicle: ")
price = input("Please enter the price for the desired vehicle: ")
type = input("Please enter the type for the desired vehicle: ")
rangeItem = df[(df['Range'] > int(range)) & (df['Price After Credit'] < int(price)) & (df['Type'] == type)]
print(rangeItem[['Brand', 'Model', 'Range', 'Price After Credit', 'Type']])
print(rangeItem)


