import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class pol_reg:
    def __init__(self,path,degree,train=0.80,rand=10):
        self.path=path
        self.degree=degree
        self.train=train
        self.rand=rand
        
        self.data=pd.read_csv(self.path)
        self.x=self.data.iloc[:, :-1]
        self.y=self.data.iloc[:, -1]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, train_size=self.train, random_state=self.rand)
        self.poly=PolynomialFeatures(degree=self.degree)
        self.X_poly_train=self.poly.fit_transform(self.x_train)
        self.X_poly_test=self.poly.transform(self.x_test)
        
        self.poly_model=LinearRegression()
        self.poly_model.fit(self.X_poly_train, self.y_train)
        self.y_poly_pred_train=self.poly_model.predict(self.X_poly_train)
        self.y_poly_pred_test=self.poly_model.predict(self.X_poly_test)
        X_range = np.linspace(self.x.min(), self.x.max(), 100).reshape(-1, 1)
        X_range_poly = self.poly.transform(X_range)
        y_range_pred = self.poly_model.predict(X_range_poly)
        
        plt.scatter(self.x_train, self.y_train, color='red', label='Training data')
        plt.scatter(self.x_test, self.y_test, color='green', label='Test data')
        plt.plot(X_range, y_range_pred, color='blue', label='Polynomial Regression')
        plt.legend()
        plt.show()
    def predict(self,x_new):
        X_new_poly = self.poly.transform(x_new)
        y_pred = self.poly_model.predict(X_new_poly)
        return y_pred