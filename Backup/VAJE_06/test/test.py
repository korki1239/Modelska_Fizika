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
arh=[1,2,4,8,4,2,1]
xmax=1.5
epoch_max=100
Nsamples=256



X = np.random.sample([Nsamples])*xmax
Y = python_nn.inputfunct(X) + 0.2*np.random.normal(0, 0.2, len(X))
x_train=np.array([[[xx]] for xx in X])
y_train=np.array([[[yy]] for yy in Y])

Xreal = np.arange(0.0, xmax, 0.01)
Xpred = np.array([[[xx]] for xx in Xreal])
Yreal = python_nn.inputfunct(Xreal)





primeri=([1,2,1],[1,4,1],[1,8,1],[1,16,1],[1,32,1],[1,64,1],
         [1,2,2,1],[1,4,4,1],[1,8,8,1],[1,16,16,1],[1,32,32,1],[1,64,64,1],
         [1,2,4,2,1],[1,4,8,4,1],[1,8,16,8,1],[1,16,32,16,1],[1,32,64,32,1],[1,64,128,64,1])
#primeri=([[1,2,4,8,4,2,1]])
for arh in primeri:

    n_layer=len(arh)

    net=python_nn.initialize_neural_net(arh,n_layer)
    nn_weights=python_nn.get_weights(net)


    # train
    loss=[]
    net.use(python_nn.mse, python_nn.mse_prime)
    err=net.fit(x_train, y_train, epochs=0, learning_rate=rate)
    y_pred=python_nn.convert_pred_to_list(net.predict(Xpred))
    
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(12, 4),dpi=150)
    python_nn.draw_nn(arh, ax1, nn_weights)


    # Define the plotting function
    ax2.scatter(X, Y, label='Podatki za učenje')
    ax2.plot(Xreal, Yreal, 'orange', label='Uporabljena funkcija')
    ax2.set_ylim(min(Y), max(Y))
    ax2.set_title("Število epoh: 0")
    line, = ax2.plot(Xreal, y_pred, 'r', label='Napovedana funkcija')
    ax2.legend()

    # plot on ax1 and ax2 as before

    # plot loss vs epoch on ax3
    ax3.set_xlabel('Epoch')
    ax3.set_ylabel('Loss')
    ax3.set_xlim(0,epoch_max)
    ax3.set_ylim(0,0.1)
    line3, = ax3.plot([],[], lw=2)
    
    
    plt.draw()
    
    

    def update(epoch,ax,ax1):
        # Train the network for one epoch
        ax1.cla()
        nn_weights=python_nn.get_weights(net)
        python_nn.draw_nn(arh, ax1, nn_weights)
        net.use(python_nn.mse, python_nn.mse_prime)
        err=net.fit(x_train, y_train, epochs=1+epoch, learning_rate=rate)
        loss.append(err)
        xloss=[ee for ee in range(epoch+1)]
        y_pred=python_nn.convert_pred_to_list(net.predict(Xpred))
        mse2=np.sum(np.array([(y_pred[k]-Yreal[k])**2 for k in range(len(y_pred))]))/len(y_pred)
        line.set_ydata(y_pred)
        ax.set_title(f"Število epoh: {1+epoch}, Vzorcev: {len(X)}, MSE:{mse2:.4f}")
        line3.set_data(xloss, loss)
        fig.canvas.draw_idle()
        return line,

    # Create the animation
    plt.tight_layout()
    ani = FuncAnimation(fig, update, frames=tqdm(range(1,epoch_max)), fargs=(ax2,ax1,))
    plt.show()
    output_file = f"Layer_size_{'_'.join(map(str, arh))}.gif"
    ani.save(output_file, writer='pillow')