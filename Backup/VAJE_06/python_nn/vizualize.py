import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
def draw_nn(arh,ax,nn_weights):
    pos={}
    G=nx.DiGraph()
    colors={}
    sizes={}
    
    for x, size in enumerate(arh):
        for y in range(size):
            name=f'{x}-{y}'
            pos[name]=(x, y-size/2)
            
            if x==0:
                colors[name]="green"
                sizes[name]=100
            elif x==len(arh)-1:
                colors[name]="orange"
                sizes[name]=100
            else:
                colors[name]="black"
                sizes[name]=20
    for x1 in range(len(arh)-1): #Sem v x1 plasti
        arr_shape = np.array(nn_weights[x1]).shape
        s1 = arr_shape[0] if len(arr_shape) > 0 else None
        s2 = arr_shape[1] if len(arr_shape) > 1 else None
        for y1 in range(arh[x1]): #v tej plasti grem skozi vse nevrone
            ni=f'{x1}-{y1}'
            x2=x1+1 #Sem v sosednji plasti
            for y2 in range(arh[x2]): #v tej plasti grem skozi vse nevrone
                nj=f'{x2}-{y2}'
                if s2==None:
                    value=nn_weights[x1][y2]
                else:
                    value=nn_weights[x1][y1][y2]
                G.add_edge(ni,nj,weight=value)
            
    weights = []
    edge_color=[]
    for (u, v, w) in G.edges(data=True):
        if w['weight'] < 0:
            edge_color.append("blue")
        else:
            edge_color.append("red")
        weights.append(abs(w['weight']))
    nx.draw_networkx_nodes(G,
                        pos,
                        node_color=[colors[node] for node in G],
                        node_size=[sizes[node] for node in G],
                        ax=ax
                        )
    nx.draw_networkx_edges(G,
                           pos,
                           width=weights,
                           edge_color=edge_color,
                           ax=ax)
    ax.axis("off")           