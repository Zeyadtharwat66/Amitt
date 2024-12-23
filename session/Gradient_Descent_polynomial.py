import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv(r"C:\Users\Lenovo\Desktop\AMIT\Salary_Data.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,1]
x_train , x_test , y_train , y_test = train_test_split(x,y,train_size=0.80,random_state=10)

poly = PolynomialFeatures(degree=50)  
X_poly_train = poly.fit_transform(x_train)
X_poly_test = poly.transform(x_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)

y_poly_pred_train = poly_model.predict(X_poly_train)
y_poly_pred_test = poly_model.predict(X_poly_test)

X_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = poly_model.predict(X_range_poly)

my_model = LinearRegression()
my_model.fit(x_train,y_train)
plt.scatter(x_train, y_train, color='red', label='Training data')
plt.scatter(x_test, y_test, color='green', label='Test data')
plt.plot(X_range, y_range_pred, color='blue', label='Polynomial Regression')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary') 
plt.legend()
plt.show()
