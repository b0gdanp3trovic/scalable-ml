import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import requests
import json
from sklearn.datasets import load_boston
import joblib

b_dataset = load_boston()
dataset = pd.DataFrame(b_dataset.data, columns = b_dataset.feature_names)
dataset['MEDV'] = b_dataset.target
X = pd.DataFrame(np.c_[dataset['LSTAT'], dataset['RM']], columns = ['LSTAT','RM'])
Y = dataset['MEDV']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
y_pred = regressor.predict(X_test)
joblib.dump(regressor, open('model.joblib','wb'))