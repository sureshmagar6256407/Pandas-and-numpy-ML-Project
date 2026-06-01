import numpy   
import matplotlib.pyplot as plt 
from scipy import stats
# from scipy import stats
# speed  = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x    = numpy.mean(speed)
# print(x)

# y   = numpy.median(speed)
# print(f"the speed of  median is {y}")

# z  = stats.mode(speed)
# print(f"the speed of mode is {z}")





# #low standard deviation
# import  numpy
# speed = [86,87,88,86,87,85,86] 
# x  = numpy.std(speed)
# print(x)

# #high standard deviation
# import numpy
# speed = [32,111,138,28,59,77,97]
# y = numpy.std(speed)
# print(y)





#VARIENCE
# import numpy
# speed = [32,111,138,28,59,77,97]
# x = numpy.var(speed)
# print(x)





#PERCENTILES
# ages= [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# x = numpy.percentile(ages,90)
# print(x)




# #DATA DISTRIBUTION  
# x  = numpy .random.uniform(0.0 , 5.0, 250)  
# plt.hist(x,5)  
# plt.show()
# print(x)

# y = numpy.random.uniform(0.0, 5.0 , 100000)  
# plt.hist(y,5)  
# plt.show()


#NORMAL DISTRIBUTION
# x = numpy.random.normal(5.0,1.0,100000)
# plt.hist(x,100)
# plt.show()


# #Scatter plot   
# x = numpy.random.normal(5.0 ,1.0 ,1000)
# y  = numpy.random.normal(10.0,2.0,1000)  
# plt.scatter(x,y)
# plt.show()



# LINEAR REGRESSION
# 1. Class define gareko
"""
class LinearRegressionModel:
    def __init__(self, x_data, y_data):
        self.x = x_data
        self.y = y_data
        # Model train garera coefficients calculate gareko
        self.slope, self.intercept, self.r, self.p, self.std_err = stats.linregress(self.x, self.y)

    def myfunc(self, x_val):
        # Timro original function jasle line calculate garchha
        return self.slope * x_val + self.intercept

    def run_analysis(self):
        # 1. Model line list banako map use garera
        mymodel = list(map(self.myfunc, self.x))
        
        # 2. Results print gareko
        print("--- Linear Regression Results ---")
        print(f"Slope: {self.slope:.4f}")
        print(f"Intercept: {self.intercept:.4f}")
        print(f"R-Value (Correlation): {self.r:.4f}")
        print(f"R-Squared (Accuracy): {self.r**2:.4f}")
        
        # 3. Graph plot gareko
        plt.scatter(self.x, self.y, color='blue', label='Data Points')
        plt.plot(self.x, mymodel, color='red', label='Regression Line')
        plt.xlabel('X Data')
        plt.ylabel('Y Data')
        plt.title('Linear Regression Model')
        plt.legend()
        plt.show()

    def predict_new(self, new_x):
        # Pachi naya function ka rakhera run garna ko lagi prediction method
        return self.slope * new_x + self.intercept

def first_analysis() : 
    # Timle diyeko actual data
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
    
    # 1. Object create gareko (Data pass garera)
    my_model_object = LinearRegressionModel(x, y)
    
    # 2. Train bhako model ko graph ra results run gareko
    my_model_object.run_analysis()
    
    # 3. Naya function/code run garna paryo bhane yesari value pass garne
    # Udaharan ko lagi: X ko value 10 huda Y कति hunchha run gareko
    naya_value = 10
    prediction = my_model_object.predict_new(naya_value)
    print(f"\n[Prediction Result] If X = {naya_value}, Predicted Y = {prediction:.2f}")
first_analysis()
"""

""""""
import matplotlib.pyplot as plt 
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope , inetercept,r ,p,std_err = stats.linregress(x,y)
def myfunc(x) : 
    return slope * x +inetercept  
mymodel  = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()
