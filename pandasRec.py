import pandas as pd
import numpy as np
df=pd.read_csv("evDB.csv")
print("The dataframe is:")
print(df)

'''rangeCol = df['Range']
print("The column is:")
print(rangeCol)
'''

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