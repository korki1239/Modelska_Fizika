import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm.auto import tqdm
#from python_nn import *#Network,FCLayer, ActivationLayer, tanh, tanh_prime, mse, mse_prime,draw_nn, initialize_neural_net

import python_nn as python_nn
# training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])


# network
rate=0.2
arh=[1,4,8,4,1]
xmax=1.5
epoch_max=100
Nsamples=1024



X = np.random.sample([Nsamples])*xmax
Y = python_nn.inputfunct(X) + 0.2*np.random.normal(0, 0.2, len(X))
x_train=np.array([[[xx]] for xx in X])
y_train=np.array([[[yy]] for yy in Y])

Xreal = np.arange(0.0, xmax, 0.01)
Xpred = np.array([[[xx]] for xx in Xreal])
Yreal = python_nn.inputfunct(Xreal)





net=python_nn.initialize_neural_net(arh,len(arh))
nn_weights=python_nn.get_weights(net)


# train
loss=[]
net.use(python_nn.mse, python_nn.mse_prime)
err=net.fit(x_train, y_train, epochs=epoch_max, learning_rate=rate,show=True)
y_pred=python_nn.convert_pred_to_list(net.predict(Xpred))

#plt.plot([[y[0][0] for y in y_train] for y in y_train], 'orange', label='Uporabljena funkcija')
print("\n",err)

plt.plot(Xreal, y_pred, label='Predikcija')
plt.scatter(x_train[:,0,0], y_train[:,0,0],label="train data",color="black")
plt.plot(Xreal, Yreal,label="Prava funkcija")
plt.legend()
plt.show()