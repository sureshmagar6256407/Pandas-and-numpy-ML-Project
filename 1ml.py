from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import mean_squared_error,r2_score  
import pandas as pd 
import joblib as jlb


#data from csv file
df = pd.read_csv("Cleaned_Employee_Data1.csv")
#fill the data 
df.fillna(
    {"Projects_Completed":df["Projects_Completed"].mean()}, 
    inplace=True
)



#selecting features and target variable 
X= df[["Experience_Years","Projects_Completed","yearsinCompany","Performance_Score"]]
y= df["Salary"] 


#splitting data into training and testing sets  
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)  

#train model  
model  =LinearRegression()
model.fit(X_train,y_train)

#predicting on test set 
y_pred = model.predict(X_test)
print("Predicted Salary:",y_pred)
print("Actual Salary:",y_test)

#evaluating model performance 
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print("Mean Squared Error:",mse)
print("R-squared Score:",r2)

#save the model  
jlb.dump(model,"employee_salary_model1.pkl")