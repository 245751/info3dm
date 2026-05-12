import dataset1
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X,Y=dataset1.load_dataset()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
model=LinearRegression()