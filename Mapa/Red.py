
import csv

import networkx as nx


from station import *

def Crear_red_ferroviaria(archivo_conexiones='conexiones.txt',archivo_posiciones='posiciones.txt'):
    # get lon, lat locations
    locations = {} # location dictionary
    for station in create_stations():
        locations[station.get_id()] = station.get_coordinates()
        
    # initialize networkx graph
    t_map = nx.Graph()
    
    # load in edges from 't_edges.txt'
    with open(archivo_conexiones) as t:
         # read in all lines 
         edges = t.readlines()
         # iterate over edges and add all nodes and edges to graph
         for line in edges:
             (inicio, fin) = tuple(line.split(','))
             # get rid of newline char at end of color string
             fin = fin.replace('\n','') 
             # add edge to graph with color attribute and time as weight
             #t_map.add_edge(source, destination, weight=float(time), color=color) 
             t_map.add_edge(inicio, fin)
    
    # load in edges from 't_edges.txt'
    with open(archivo_posiciones) as t:
         # read in all lines 
         edges = t.readlines()
         # iterate over edges and add all nodes and edges to graph
         for line in edges:
             (indice, pos_x, pos_y) = tuple(line.split(','))
             # get rid of newline char at end of color string
             pos_y = pos_y.replace('\n','') 
             # add edge to graph with color attribute and time as weight
             #t_map.add_edge(source, destination, weight=float(time), color=color) 
             t_map.add_node(indice, pos = (int(pos_x),int(pos_y)))


        
        
    # return graph
    return t_map

     