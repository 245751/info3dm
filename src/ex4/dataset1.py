import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
np.random.seed(0)

def true_function(x):
    '''
    >>> true_function(np.array([0]))
    array([0.])

    '''
    return np.sin(np.pi*x*0.8)*10

def load_dataset():
    X=np.arange(-1,np.sqrt(2),0.01)
    Y=true_function(X)
    return X,Y

def load_noisy_dataset():
    X,Y=load_dataset()
    X_Coordinates=np.random.uniform(-1,1,20)
    Y_Coordinates=true_function(X_Coordinates)
    noise=np.random.normal(0,1,20)/2
    Y_Coordinates_Noisy=Y_Coordinates+noise
    data=np.array([[x,y] for x,y in zip(X_Coordinates,Y_Coordinates)])
    df=pd.DataFrame(data,columns=["観測点","真値"])
    df["観測値"]=Y_Coordinates_Noisy
    return X_Coordinates, Y_Coordinates_Noisy,df

def save_dataset(df):
    df.to_csv("src/ex4/dataset1.tsv",sep="\t",index=False)

def output_dataset():
    df=pd.read_csv("src/ex4/dataset1.tsv",sep="\t")
    return df

if __name__=="__main__":
    X=np.arange(-1,np.sqrt(2),0.01)
    Y=true_function(X)
    X_Coordinates=np.random.uniform(-1,1,20)
    noise=np.random.normal(0,1,20)/2
    Y_Coordinates=true_function(X_Coordinates)
    Y_Coordinates_Noisy=Y_Coordinates+noise
    data=np.array([[x,y] for x,y in zip(X_Coordinates,Y_Coordinates)])
    df=pd.DataFrame(data,columns=["観測点","真値"])
    df["観測値"]=Y_Coordinates_Noisy
    load_df=pd.read_csv("src/ex4/dataset1.tsv",sep="\t")
    print(load_df)
    exit()
    fig,ax=plt.subplots()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Exercise1.3 graph")
    ax.plot(X,Y,color="blue",label="sin(pi*0.8*x)*10")
    ax.plot(X_Coordinates,Y_Coordinates,".",color="black",label="真値")
    ax.scatter(X_Coordinates,Y_Coordinates_Noisy,color="red",label="観測値")
    ax.legend()
    plt.show()
    import doctest
    doctest.testmod()