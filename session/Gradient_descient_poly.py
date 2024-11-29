import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
data=pd.read_csv(r"C:\D\Amitt\session\Salary_Data.csv")
x=data.iloc[:,:-1]
y=data.iloc[:,1]
X_train , X_test , y_train , y_test = train_test_split(x,y,train_size=0.8,random_state = 10)

poly = PolynomialFeatures(degree=15)  
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)

y_poly_pred_train = poly_model.predict(X_poly_train)
y_poly_pred_test = poly_model.predict(X_poly_test)

X_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = poly_model.predict(X_range_poly)

plt.scatter(X_train, y_train, color='red', label='Training data')
plt.scatter(X_test, y_test, color='green', label='Test data')
plt.plot(X_range, y_range_pred, color='blue', label='Polynomial Regression')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()