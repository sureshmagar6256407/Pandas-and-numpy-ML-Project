import pandas as pd
import numpy as np

np.random.seed(42)

n = 50

data = {
    "Engine_Size": np.random.uniform(1.0, 4.5, n),   # liters
    "Horsepower": np.random.randint(70, 300, n),
    "Age": np.random.randint(1, 15, n),
    "Mileage": np.random.randint(10000, 200000, n),
    "Brand_Value": np.random.randint(1, 5, n)  # 1=low brand, 5=high brand
}

df = pd.DataFrame(data)

# Price formula (realistic logic)
df["Price"] = (
    df["Engine_Size"] * 500000 +
    df["Horsepower"] * 10000 -
    df["Age"] * 80000 -
    df["Mileage"] * 5 +
    df["Brand_Value"] * 300000
)

# averagePrice 
averagePrice  = np.mean(df["Price"]) 
print(f"the average price is : {averagePrice}")
print()

#top 5 most expensive car  df.nlargest(value,name)
top5 = df.sort_values("Price",ascending=False).head(5) 
print(f"top 5 expensive car is :\n {top5}")
print()

# Age > 10 भएका कारहरूको average price निकाल।
AgeGreaterThan10  = df[df["Age"] > 10]["Price"].mean()
print(f"The car age > 10 average  price are : \n {AgeGreaterThan10}")

