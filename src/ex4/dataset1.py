import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    '''
    >>> true_function(np.array([0]))
    array([0.])

    '''
    return np.sin(np.pi*x*0.8)*10

X=np.arange(-1,2,0.01)
Y=true_function(X)
plt.plot(X,Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Exercise1.1 graph")
plt.show()
if __name__=="__main__":
    import doctest
    doctest.testmod()