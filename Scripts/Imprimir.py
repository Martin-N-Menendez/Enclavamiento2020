# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:19:56 2019

@author: jinnkay
"""

import networkx as nx
import matplotlib.pyplot as plt

#%%
def Imprimir_grafo(G, pos):
    #labels = nx.get_edge_attributes(G, 'weight')
    
    N = nx.number_of_nodes(G)
    
    color_map = []
    
    
    
    for i in range(N):
        if G.nodes[str(i+1)]["Aspecto"] != 'No':
            if G.nodes[str(i+1)]["Aspecto"][0] == 'Rojo':
                color_map.append('red')
            else: color_map.append('grey')
            
        else: color_map.append('grey')    
        #if str(i+1) == "5":
        #    color_map.append('blue')
        #else: color_map.append('grey')    
    
    #print(color_map)    
    #nx.draw(G,node_color = color_map,with_labels = True)


    nx.draw_networkx_nodes(G, pos, node_size=500, node_color = color_map)
    # edges
    nx.draw_networkx_edges(G, pos, width=5)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    #labels = nx.get_edge_attributes(G, 'weight')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()