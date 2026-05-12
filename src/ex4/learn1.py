import dataset1
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
from sklearn.linear_model import LinearRegression

X,Y=dataset1.load_dataset()
model=LinearRegression()