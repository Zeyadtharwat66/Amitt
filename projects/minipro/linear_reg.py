import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

class lin_reg:
    def __init__(self, path, alpha, train=0.80, rand=10):
        self.path = path
        self.alpha = alpha
        self.train = train
        self.rand = rand
        self.data = pd.read_csv(self.path)
        self.x = self.data.iloc[:, :-1]
        self.y = self.data.iloc[:, -1]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, train_size=self.train, random_state=self.rand)        
        self.model = LinearRegression()
        self.model.fit(self.x_train, self.y_train)
        plt.scatter(self.x_train, self.y_train, color='red', label='Training data')
        plt.scatter(self.x_test, self.y_test, color='green', label='Test data')        
        x_range = np.linspace(self.x_train.min(), self.x_train.max(), 100).reshape(-1, 1)
        y_range_pred = self.model.predict(x_range)
        plt.plot(x_range, y_range_pred, color='blue', label='Linear Regression')
        plt.legend()
        plt.show()
    
    def predict(self, x_new):
        y_pred = self.model.predict(x_new)
        return y_pred

    def performance(self):
        y_train_pred = self.model.predict(self.x_train)
        y_test_pred = self.model.predict(self.x_test)        
        self.mse_train = mean_squared_error(self.y_train, y_train_pred)
        self.mse_test = mean_squared_error(self.y_test, y_test_pred)
        self.r2_train = r2_score(self.y_train, y_train_pred)
        self.r2_test = r2_score(self.y_test, y_test_pred)
        