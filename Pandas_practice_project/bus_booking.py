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
print()

"--------- format making the correctly----------"
string_col  = df.select_dtypes (include=["object" , "string"]).columns   
for col in string_col : 
    df[col]  = df[col].str.strip().str.title()  

num_col    = df.select_dtypes(include=["number"]).columns
for col in num_col : 
    df[col]   = pd.to_numeric (df[col] , errors="coerce")  

df["Seats_Booked"]  = df["Seats_Booked"].abs()
df["Fare_Per_Seat"]  = df["Fare_Per_Seat"].abs()


"------- handling the missing value and duplicate ----------"
print(df.drop_duplicates(inplace= True))
print(df.duplicated().sum().sum())
print()


df.fillna ( 
    {
        "Route" : "Unknown" , 
        "Bus_Type" : "Unknown"   , 
        "Payment_Method" : "Unknown" ,   
        "Booking_Status" : "Unknown"
    }
,
    inplace= True
)
print(df.isnull().sum())


