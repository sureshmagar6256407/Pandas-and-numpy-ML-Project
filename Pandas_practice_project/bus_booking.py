import pandas as pd 
import  numpy as np  


df  = pd.read_csv("Pandas_practice_project/bus_booking_5000_raw.csv" , encoding="utf-8")


"--------- data analysing ------------------"
print(df.head(10))
print()
print(df.tail(10))
print()
print(df.info())
print()
print(df.describe())
print()
print(df.shape)
print()
print(df.columns)