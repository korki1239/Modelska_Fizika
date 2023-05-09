import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm.auto import tqdm
#from python_nn import *#Network,FCLayer, ActivationLayer, tanh, tanh_prime, mse, mse_prime,draw_nn, initialize_neural_net

import python_nn as python_nn



# network
rate=0.2
arh=[2,4,4,1]
xmax=1.5
epoch_max=100
Nsamples=256

x_train, y_train,y_raw = python_nn.logical_gates("OR")
#x_train, y_train,y_raw = python_nn.function_1(Nsamples,xmax)
#x_train, y_train,y_raw = python_nn.EKG(Nsamples)

print(x_train.shape,y_train.shape,y_raw.shape)

net=python_nn.initialize_neural_net(arh,len(arh))
nn_weights=python_nn.get_weights(net)

# train
loss=[]
net.use(python_nn.mse, python_nn.mse_prime)
err=net.fit(x_train, y_train, epochs=epoch_max, learning_rate=rate,show=True)
y_pred=python_nn.convert_pred_to_list(net.predict(x_train))

#plt.plot([[y[0][0] for y in y_train] for y in y_train], 'orange', label='Uporabljena funkcija')
print("\n",err)

plt.scatter(x_train[:,0,0], y_pred, label='Predikcija',color="red",s=0.5)
plt.scatter(x_train[:,0,0], y_train[:,0,0],label="train data",color="black",s=0.5)
plt.plot(np.sort(x_train[:,0,0]), y_raw[:,0,0], label="Prava funkcija",lw=1)
plt.legend()
plt.show()