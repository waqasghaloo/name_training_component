import pandas as pd
import numpy as np

# df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'d':[10,11,12]})

# print(df.pivot(index=['a','b'],columns='c'))


# print(df[1]) // Invalid Syntax

# print(df.iloc[0,1:])

# print(df[df['b']>4])

# print(df.pivot(index='a',columns='b',values=['c','d']))

#      c               d            
# b    4    5    6     4     5     6
# a                                 
# 1  7.0  NaN  NaN  10.0   NaN   NaN
# 2  NaN  8.0  NaN   NaN  11.0   NaN
# 3  NaN  NaN  9.0   NaN   NaN  12.0


# print(df.pivot(index='a',columns='b',values=['c','d']))


df = pd.DataFrame({'a':[1,1,0],'b':[1,0,1],'c':[7,8,9],'d':[10,11,12]})

# print(df,df.shape)
# pivot_df =df.pivot(index=['a','b'],columns='c')

# print(pivot_df)
# print(pivot_df.loc[(1,0)]) This way we can pass multiple index tuple to acces specific row of dataframe
# print(pivot_df.loc[(1:,0)])

indexed_df = df.set_index(['a','b'])

# print(indexed_df)
# print(indexed_df.loc[1,1])  Accessing row of multi indexed dataframe

# print(df.loc[0]['b':]) First bracket will take row indexes and second bracket will
# take column

# print(df.index) Default indexes of dataframe starting from 0 to 3 and 3 not included

# indexed_d_df=df.set_index([[0,1,2],'a']) Setting default index along with 'a' column as index
# print(indexed_d_df.loc[0,1])

# indexed_d_df = df.set_index([pd.Index([0,1,2]),'a'])
# print(indexed_d_df)

# print(df)
# print((df['a']==1) & (df['a']==1))

# print(df[(df['a']==1) & (df['a']==1)]) use bitwise operator as '&' not 'and'.

# print(df[df['c']>7]) # Returns only the rows where 

# print(df.where(df['c']>7)) # Returns complete dataframe but values only in where condition is true

# print(df['d'].map(lambda x : -1*x)) #Multiple each element with -1

# df.map(lambda x: -1*df['d']) 

# multi_index_df = pd.DataFrame({
#     'A': [1, 2, 3, 4],
#     'B': [10, 20, 30, 40],
#     'C': [100, 200, 300, 400]
# }, index=[['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]])

# print(multi_index_df)

# multi_index_df = multi_index_df.reset_index().set_index('level_0')

# print(multi_index_df)


# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value': [1, 2, 3, 4]})

# df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
#                     'value': [5, 6, 7, 8]})

df = pd.DataFrame({'continent':['a','b','a','b','c','b'],'length':[100,200,300,200,100,400],'pop':[7,8,9,2,3,4]})
# df1 = pd.DataFrame({'a':[1,1],'f':[1,0],'c':[7,8]})

# df=df.set_index('a')
# df1=df1.set_index('a')

# # print(df1)
# concaneted_df = pd.concat([df,df1],join='inner',ignore_index=True)

# print(concaneted_df)


# Common columns will be concatenated and index column could be different 
# In Outer, all columns would be concatenated

#   b  c
# a      
# 1  1  7
# 1  0  8
# 0  1  9
# 1  1  7
# 1  0  8
# 0  1  9

# Groupby way#1
# print(df.groupby('continent')['length'].agg(['sum','mean']))

# Groupby way#2 - dont use brackets for numpy functions.

# print(df.groupby('continent')[['length','pop']].agg([np.sum,np.mean]))
# print(df.groupby('continent')[['length','pop']].agg(['sum','mean']))

print(df.groupby('continent').agg({'length':{'mean':'length_mean'}}))

df.groupby('continent').agg({'length'})