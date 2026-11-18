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
print()

"---------get the information from the data ----------------"

first  = df.groupby("Route")["Booking_ID"].count()
print(F"pratek route ma  : \n {first} bhayeka xan")
print()
second  =df.groupby("Bus_Type")["Total_Amount"].sum()
print(f"pratek bust type bata aayeko revenue : \n {second}")
print()

third = df.sort_values(by="Seats_Booked"  , ascending=False).head(10)
print(f"sabai bhandi seat booked garne  : \n {third}")
print()

four = df[df["Booking_Status"] == "Completed"].groupby("Route")["Total_Amount"].sum()
print(f"booking complete bhako pratek route ko total revenue is : \n {four}")
print()

five   = df.value_counts(subset="Payment_Method")
print(f"Sabai bhanda badi use bhako method : {five.idxmax()}")
print()

six = df.groupby("Route")["Fare_Per_Seat"].mean()
print(f"pratek route ko average fare : \n {six}")
print()


print(df.columns)