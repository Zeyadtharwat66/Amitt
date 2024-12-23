import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv(r'C:\\D\\Amitt\\projects\\ML1\\housing.csv')
Q1 = data['MEDV'].quantile(0.25)
Q3 = data['MEDV'].quantile(0.75)
IQR = Q3 - Q1
upper = Q3 + 1.5 * IQR
lower = Q1 - 1.5 * IQR
data['MEDV'] = data['MEDV'].clip(lower, upper)
prices = data['MEDV']
features = data.drop('MEDV', axis=1)
features['RM'] = features['RM'].astype(int)
features['LSTAT'] = pd.cut(features['LSTAT'], bins=[-np.inf, features['LSTAT'].quantile(0.25), features['LSTAT'].quantile(0.5), features['LSTAT'].quantile(0.75), np.inf], labels=['low', 'medium', 'high', 'extreme'])
features['PTRATIO'] = pd.cut(features['PTRATIO'], bins=[-np.inf, features['PTRATIO'].quantile(0.25), features['PTRATIO'].quantile(0.5), features['PTRATIO'].quantile(0.75), np.inf], labels=['low', 'medium', 'high', 'extreme'])
features = pd.get_dummies(features, columns=['LSTAT', 'PTRATIO'], drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state=42)
regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X_train, y_train)
def predict_new_data(rooms_number, pop, ratio):
    input_features = {'RM': rooms_number, 'LSTAT_' + pop: 1, 'PTRATIO_' + ratio: 1}
    input_df = pd.DataFrame([input_features])
    input_df = input_df.reindex(columns=features.columns, fill_value=0)
    prediction = regressor.predict(input_df)
    return prediction[0]
