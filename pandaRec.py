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
print(rangeItem[['Brand', 'Model','Range']])

'''
#filtering based on range greater than 300 and price less than 
rangeItem = df[df['Range'] > 300]
print(rangeItem)
'''
