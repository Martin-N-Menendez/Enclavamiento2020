import networkx as nx
import random
import matplotlib.pyplot as plt
import time 


from Imprimir import *
from Red import *
from station import *
from Analisis import *
  
    




#%% 
def Crear_atributos(N):

    atributos= {} # create an empty dictionary
    dic = {'Semaforo': 'No', 'Aspecto': 'No','Direccion': 'No','Barrera':'No', 'Ocupado':'No', 'Cambio':'No'}
    #list is our input where 'a','b','c', are keys and 1,2,3,4 are values
    for i in range(N):
        #for j in range(len(list)):
         if str(i+1) in atributos.keys():# if key is present in the list, just append the value
             atributos[str(i+1)].append(dic)
         else:
             atributos[str(i+1)] = {} # else create a empty list as value for the key
             atributos[str(i+1)] = dic # now append the value for that key
         
    return atributos  
    

#%%
def Calcular_Rutas(G):
    
    N = nx.number_of_nodes(G)
    
    estaciones = Detectar_Estaciones(G)
    
    Rutas = {}

    print("\n##### Rutas posibles #####\n")
    N_rutas = 0
    for i in range(N):      
        if Grafo.nodes[str(i+1)]["Semaforo"] != 'No':
            vecinos = [n for n in G.neighbors(str(i+1))]
            for j in range(len(vecinos)):   
                
                if vecinos[j] in estaciones:
                    nuevos_vecinos = [n for n in G.neighbors(str(vecinos[j]))]
                    suplente = list(set(nuevos_vecinos) - set([str(i+1)]))        
                    vecinos[j] = suplente[0]
     
                if G.nodes[str(vecinos[j])]["Semaforo"] != 'No':
                    
                    conexion = [str(i+1),vecinos[j]]
                    
                    N_rutas += 1
                    
                    Rutas[str(N_rutas)] = {} 
                    Rutas[str(N_rutas)] = conexion 
             
        
                    print("R_{} : {} -> {}".format(N_rutas,str(i+1),vecinos[j]))
    
    print(Rutas)
    return Rutas



#%%
def Hay_tren(G):

    N = nx.number_of_nodes(G)
    
    hay_tren = "Falso"
    
    for i in range(N):
        if G.nodes[str(i+1)]["Ocupado"] == 'ocupado' :
            hay_tren = "Verdadero"
    
    return hay_tren

#%%
def Insertar_tren(G):
    
    cambios,secundarios,estaciones,extremos = Clasificar_CVs(G)
    
    print("Insertando tren en {}".format(extremos[0]))
    
    G.nodes[extremos[0]]["Ocupado"] = 'ocupado'

#%%    
def Detectar_tren(G):

    N = nx.number_of_nodes(G)
    
    ubicacion = []    
    
    for i in range(N):
        if G.nodes[str(i+1)]["Ocupado"] == 'ocupado' :
            ubicacion.append(str(i+1))
    
    return ubicacion
    
#%%
def Avanzar_tren(G):

    if Hay_tren(G) == "Falso":
        Insertar_tren(G)
     
    #print("Avanzando ...") 
    
    ubicacion = Detectar_tren(G)[0]
    
    if int(ubicacion) < N:
        G.nodes[ubicacion]["Ocupado"] = 'libre'
        anterior,proximo = Calcular_proximo(Grafo,int(ubicacion)-1)
        G.nodes[proximo]["Ocupado"] = 'ocupado'
        
    ubicacion = Detectar_tren(G)[0]
    
    print("Tren en : {}".format(ubicacion))

    
#%%
    
Grafo = Crear_red_ferroviaria()
   
N = nx.number_of_nodes(Grafo)
atributos = Crear_atributos(N)

nx.set_node_attributes(Grafo, atributos)



for (u, v, w) in Grafo.edges(data=True):
    w['weight'] = random.randint(0, 10)


pos = nx.get_node_attributes(Grafo,'pos')


Imprimir_grafo(Grafo, pos)

Calcular_Secciones(Grafo)
Detectar_Cambios(Grafo,'cantidad')
Calcular_Barreras(Grafo)
Detectar_Semaforos(Grafo,"test")

Calcular_conexiones(Grafo)

Clasificar_Secciones(Grafo,"test")


Imprimir_estados(Grafo)

#Calcular_Rutas(Grafo)


#Imprimir_grafo(Grafo, pos)



        
#for i in range(10):
#    Calcular_proximo(Grafo,i)

#for i in range(10):
#    time.sleep(0.1)
#    Avanzar_tren(Grafo)
    #print(i)


