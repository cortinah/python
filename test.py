import sys
print(sys.executable)

import pandas as pd


df=pd.DataFrame({'test': [1,2,3,4],"names": ['a','b','c','d']})
df.describe()

type(df)
df['names']

GDP_df = pd.DataFrame({'Country ID': ['USA', 'CHN' , 'IND', 'ARE', 'CAN', 'MEX'], 
                       'Country':['United States', 'China', 'India', 'United Arab Emirates', 'Canada', 'Mexico'], 
                       'GDP Per Capita [$]':[69375, 11891, 2116, 43538, 52791, 9967], 
                       'Global Rank':[5, 64, 150, 24, 15, 72]})


print("hello")
