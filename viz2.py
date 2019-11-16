import pandas as pd
import numpy as np
from sklearn.datasets import load_boston

boston_housing = load_boston()
columns_names = boston_housing.feature_names
y = boston_housing.target
X = boston_housing.data

# print(f'sklearn dataset X shape: {X.shape}')
# print(f'sklearn dataset y shape: {y.shape}')
#
# # What's inside this sklearn loaded dataset
# print(f'keys: {boston_housing.keys()}')
# print(f'data: {boston_housing.data}')
# print(f'target: {boston_housing.target}')
# print(f'feature_names: {boston_housing.feature_names}')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

# # Training a Linear Regression model with fit()
# from sklearn.linear_model import LinearRegression
# lm = LinearRegression()
# lm.fit(X_train, y_train)
#
# # Output of the training is a model: a + b*X0 + c*X1 + d*X2 ...
# print(f"Intercept: {lm.intercept_}\n")
# print(f"Coeficients: {lm.coef_}\n")
# print(f"Named Coeficients: {pd.DataFrame(lm.coef_, columns_names)}")


# Training a Linear Regression model with fit()
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train, y_train)

# Output of the training is a model: a + b*X0 + c*X1 + d*X2 ...
print(f"Intercept per class: {lr.intercept_}\n")
print(f"Coeficients per class: {lr.coef_}\n")

print(f"Available classes: {lr.classes_}\n")
print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], columns_names)}\n")
print(f"Named Coeficients for class 2: {pd.DataFrame(lr.coef_[1], columns_names)}\n")
print(f"Named Coeficients for class 3: {pd.DataFrame(lr.coef_[2], columns_names)}\n")

print(f"Number of iterations generating model: {lr.n_iter_}")