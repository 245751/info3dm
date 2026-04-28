import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(0)

def true_function(x):
    '''
    >>> true_function(np.array([0]))
    array([0.])

    '''
    return np.sin(np.pi*x*0.8)*10

X=np.arange(-1,2,0.01)
Y=true_function(X)

X_Coordinates=np.random.uniform(-1,1,20)
Y_Coordinates=true_function(X_Coordinates)
data=np.array([[x,y] for x,y in zip(X_Coordinates,Y_Coordinates)])
df=pd.DataFrame(data,columns=["観測点","真値"])
fig,ax=plt.subplots()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Exercise1.2 graph")
ax.plot(X,Y)
ax.plot(X_Coordinates,Y_Coordinates,".")
plt.show()
if __name__=="__main__":
    import doctest
    doctest.testmod()