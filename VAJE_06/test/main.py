import networkx as nx
import matplotlib.pyplot as plt
arh=[2,4,8,16,32,16,8,4,2]

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
            colors[name]="blue"
            sizes[name]=20
        print(x,y,name,pos[name],colors[name],sizes[name])
    print("--------------------")
print()
for x1 in range(len(arh)-1):
    for y1 in range(arh[x1]):
        ni=f'{x1}-{y1}'
        x2=x1+1
        for y2 in range(arh[x2]):
            nj=f'{x2}-{y2}'
            G.add_edge(ni,nj)

for node in G:
    print(node,pos[node],colors[node],sizes[node])

nx.draw_networkx_nodes(G,
                       pos,
                       node_color=[colors[node] for node in G],
                       node_size=[sizes[node] for node in G]
                       )
nx.draw_networkx_edges(G, pos)
plt.axis("off")
plt.show()             