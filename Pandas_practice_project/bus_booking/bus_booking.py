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
df.drop_duplicates(inplace= True)
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

third = ( 
    df.groupby("Customer_ID")["Seats_Booked"].sum().sort_values(ascending=False).head(10)
)
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

seven  = df.sort_values(by="Delay_Minutes" , ascending= False).head(10)
print(f"Sabai bhanda dherai delay  booking bhako : \n {seven}")
print()

eight  = df.loc[df["Booking_Status"].isin(["Cancelled","Refunded"])]
compare  =eight.groupby("Booking_Status")["Booking_ID"].agg(["count"])
print(f"compare between the cancelled and refunded : \n {compare}")
print()

df["Booking_Date"]  = pd.to_datetime(df["Booking_Date"] ,errors="coerce")
nine  = df.groupby ( df["Booking_Date"].dt.month_name())["Total_Amount"].sum()
print(f"pratek mahina ko total revenue booking : \n {nine}")
print()

ten = df.groupby("Customer_ID")["Total_Amount"].sum().sort_values(ascending=False).head(10)
print(f"सबैभन्दा धेरै खर्च गर्ने Top 10 customers:\n{ten}")
print()

eleven  = df.groupby("Bus_Type")["Delay_Minutes"].mean()
print(f"bus type ko average delay minutes : \n {eleven}")
print()

twelve = df.loc[df["Discount_Percent"] >= 10 , "Total_Amount"].sum()
print(f"discount amount >= 10 Total Amount : {twelve} ")
print()


df["Booking_Date"] = pd.to_datetime(df["Booking_Date"], errors="coerce")
df["Travel_Date"] = pd.to_datetime(df["Travel_Date"], errors="coerce")

df["Booking_Difference"] = (
    df["Travel_Date"] - df["Booking_Date"]
).dt.days

average_days = df["Booking_Difference"].mean()

print(f"Average booking difference: {average_days:.2f} days")
print()


completed = (
    df[df["Booking_Status"] == "Completed"]
    .groupby("Route")["Booking_ID"]
    .count()
)

total = df.groupby("Route")["Booking_ID"].count()

completed_percentage = (completed / total * 100).round(2)

print(completed_percentage)
print()



daily_bookings = (
    df.groupby("Booking_Date")["Booking_ID"]
    .count()
    .sort_values(ascending=False)
)

print("Top 5 booking dates:")
print(daily_bookings.head(5))

print("Highest booking date:")
print(daily_bookings.idxmax())
print()


invalid_discount = df.loc[
    (df["Discount_Percent"] < 0) |
    (df["Discount_Percent"] > 100)
]

print(invalid_discount)



