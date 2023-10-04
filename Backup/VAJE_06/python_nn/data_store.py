import numpy as np

def inputfunct(x):
    #return 0.25*(np.cos(2*np.pi*x*x)+2.0)*np.exp(-0.1*x)
    return 0.25*(np.sin(2*np.pi*x*x)+2.0)-0.5

def EKG(N=2000):
    data=np.loadtxt("foetal_ecg.dat")
    delta=(np.max(data[0:N,1])-np.min(data[0:N,1]))
    y_raw=(data[0:N,1]-np.min(data[0:N,1]))/delta
    
    x=np.array([[[t]] for t in data[0:N,0]])
    y=np.array([[[t]] for t in y_raw])
    return x,y,y

def logical_gates(gate="AND"):   
    x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
    if gate=="AND":
        y_train = np.array([[[0]], [[0]], [[0]], [[1]]])
    elif gate=="NAND":
        y_train = np.array([[[1]], [[1]], [[1]], [[0]]])
    elif gate=="OR":
        y_train = np.array([[[0]], [[1]], [[1]], [[1]]])
    elif gate=="NOR":
        y_train = np.array([[[1]], [[0]], [[0]], [[0]]])
    elif gate=="XOR":
        y_train = np.array([[[0]], [[1]], [[1]], [[0]]])
    elif gate=="NXOR":
        y_train = np.array([[[1]], [[0]], [[0]], [[1]]])
    return x_train,y_train, y_train

def function_1(Nsamples,xmax):
    X = np.random.sample([Nsamples])*xmax
    Y = inputfunct(X) + 0.2*np.random.normal(0, 0.2, len(X))
    Yraw=np.array([[[yy]] for yy in inputfunct(np.sort(X))])
    x_train=np.array([[[xx]] for xx in X])
    y_train=np.array([[[yy]] for yy in Y])

    #Xreal = np.arange(0.0, xmax, 0.01)
    #Xpred = np.array([[[xx]] for xx in Xreal])
    #Yreal = inputfunct(Xreal)
    return x_train, y_train, Yraw