import dataset1
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X,Y=dataset1.load_dataset()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("予測値:",y_pred)
print("真値:",y_test)
print("スコア",model.score(X_test,y_test))