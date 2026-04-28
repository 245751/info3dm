import datasets
import regression
import importlib

X,Y=datasets.load_linear_example1()
print(X)
print(Y)

model=regression.LinearRegression()
print(model.x)

model.fit(X,Y)
print(model.theta)

predict=model.predict(X)
print(predict)

score=model.score(X,Y)
print(score)