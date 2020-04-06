# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:24:17 2019

@author: 
"""

import matplotlib.pyplot as plt
import random
import pandas as pd

from Estaciones import *
from Plotear import *
from Tabla import *
from vhdl import *
from comunicacion import *

from Serial import *

secciones = []
conexiones = []

df = []

global ax 

global N_rutas
N_rutas = 0

global tabla
global archivos

tabla = {'Ruta': [],
        'Inicial': [],
        'Final': [],
        'Secuencia': [],
        'Sentido' : []
        }

archivos = [
            ['Estaciones/con_0.txt','Estaciones/pos_0.txt'],
            ['Estaciones/con_1.txt','Estaciones/pos_1.txt'],
            ['Estaciones/con_2.txt','Estaciones/pos_2.txt'],
            ['Estaciones/con_3.txt','Estaciones/pos_3.txt'],
            ['Estaciones/con_4.txt','Estaciones/pos_4.txt'],
            ['Estaciones/con_5.txt','Estaciones/pos_5.txt'],
            ['Estaciones/con_6.txt','Estaciones/pos_6.txt'],
            ['Estaciones/con_7.txt','Estaciones/pos_7.txt'],
            ['Estaciones/con_8.txt','Estaciones/pos_8.txt']
            ]
#%%
def cargar_secciones(archivo_conexiones='conexiones.txt',archivo_posiciones='posiciones.txt'):
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
             conexiones.append([int(inicio)-1,int(fin)-1])
             
    indice = 0;
    # load in edges from 't_edges.txt'
    with open(archivo_posiciones) as t:
         # read in all lines 
        edges = t.readlines()
         
         # iterate over edges and add all nodes and edges to graph
        for line in edges:
            indice = indice + 1;
                       
            (nombre, pos_x, pos_y, barrera, sentido, extremo) = tuple(line.split(','))

            # get rid of newline char at end of color string
            extremo = extremo.replace('\n','')
             
            if sentido == '-':
                sentido = '<>'

            if extremo == '*':
                 extremo = True
            else:
                extremo = False

            #if barrera == 'b':
            #    barrera = True
            #else:
            #    barrera = False
            barrera = False  ## SIN BARRERAS!
            
            secciones.append(Estaciones(str(nombre),int(indice),float(pos_x),float(pos_y),str(sentido),barrera,extremo))
#%%            
def buscar_vecinos(test = False):
    
    for i in range(len(secciones)):
        for j in range(len(conexiones)):
            if secciones[i].id-1 in conexiones[j]:
                indice_vecino = 1 - conexiones[j].index(secciones[i].id-1)
                vecino = conexiones[j][indice_vecino]+1
                if test:
                    print("{} en {} vecino {}".format(secciones[i].id-1 , conexiones[j],vecino))
                (secciones[i].vecinos).append(vecino)
                secciones[i].calcular_vecinos()
#%%
def clasificar_vecinos(test = False):
  
    for i in range(len(secciones)):
        for j in range(secciones[i].N_vecinos):
            indice_vecino = secciones[i].vecinos[j] -1
            
            x1 = secciones[i].pos_x
            x2 = secciones[indice_vecino].pos_x
            
            y1 =secciones[i].pos_y
            y2 = secciones[indice_vecino].pos_y
            
            if abs(x1 - x2) <= abs(y1 - y2):
                if y2 < y1:
                    # down
                    m = -1
                    if x1 > x2:
                        secciones[i].desvio_inf_dir = '<'
                    else:
                        secciones[i].desvio_inf_dir = '>'
                    
                    secciones[i].desvio_inf = secciones[indice_vecino].id
                                          
                    if test:
                        print("Abajo")
                        
                else:
                    # up
                    m = 1 
                    if x1 > x2:
                        secciones[i].desvio_sup_dir = '<'
                    else:
                        secciones[i].desvio_sup_dir = '>'
                    
                    secciones[i].desvio_sup = secciones[indice_vecino].id
                    
                    if test:
                        print("Arriba")
                        
            else:
                if x2 < x1:
                    # left
                    m = -1
                    secciones[i].anterior = secciones[indice_vecino].id
                    if test:
                        print("Izquierda")
                        
                else:
                    # right
                    m = 1
                    secciones[i].posterior = secciones[indice_vecino].id
                    if test:
                        print("Derecha")                       
            
            
            if test:
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("{}: [[{},{}]] ".format(secciones[i].id,secciones[i].pos_x,secciones[i].pos_y))
                
                print("{}: [[{},{}]] ".format(secciones[i].vecinos[j],secciones[indice_vecino].pos_x,secciones[indice_vecino].pos_y))
                          
                print("index: {} ".format(secciones[i].id))
                print("nombre: {} ".format(secciones[i].nombre))
                print("Vecinos <{}> : {} ".format(secciones[i].N_vecinos,secciones[i].vecinos))
                print("Anterior: {} ".format(secciones[i].anterior))
                print("Posterior: {} ".format(secciones[i].posterior))
                print("Desvio_inf: {} ".format(secciones[i].desvio_inf))
                print("Desvio_sup: {} ".format(secciones[i].desvio_sup))
#%%
def imprimir_estados():
    for i in range(len(secciones)):
        #if i == 2-1 or i == 5-1 or i == 9-1:
        secciones[i].imprimir()
#%%
def asignar_tipo():
    for i in range(len(secciones)):
        # Extremos
        if(len(secciones[i].vecinos) == 1):
            secciones[i].tipo = "Extremo"
        # Simples
        if(len(secciones[i].vecinos) == 2):
            secciones[i].tipo = "Simple"
          
        # Cruces    
        if(len(secciones[i].vecinos) == 3 or len(secciones[i].vecinos) == 4):
            secciones[i].tipo = "Cruce"
            secciones[i].cambio = True

            #if random.randint(0, 1) > 0:
            estado = True
            #else:
                #estado = False

            secciones[i].cambio_estado = estado
                
            
        # Especiales        
        for j in range(len(secciones[i].vecinos)):
            if (secciones[secciones[i].vecinos[j]-1].cambio == True):
                #print("{} tiene de vecino a {}".format(i+1,secciones[i].vecinos[j]))     
                
                if (secciones[secciones[i].id-1].anterior != ""):
                    if (secciones[secciones[i].anterior-1].cambio == True):
                        if (secciones[secciones[i].vecinos[j]-1].desvio_sup_dir == ">" or secciones[secciones[i].vecinos[j]-1].desvio_inf_dir == ">"):
                            #print("{} es el directo de {}".format(i+1,secciones[i].vecinos[j]))  
                            secciones[i].tipo = "Directo"
                
                if (secciones[secciones[i].id-1].posterior != ""):
                    if (secciones[secciones[i].posterior-1].cambio == True):
                        if (secciones[secciones[i].vecinos[j]-1].desvio_sup_dir == "<" or secciones[secciones[i].vecinos[j]-1].desvio_inf_dir == "<"):
                            #print("{} es el directo de {}".format(i+1,secciones[i].vecinos[j]))  
                            secciones[i].tipo = "Directo"
                            
                if (secciones[secciones[i].vecinos[j]-1].desvio_sup == i+1):
                    #print("{} es el desvio de {}".format(i+1,secciones[i].vecinos[j])) 
                    secciones[i].tipo = "Desvio"
                    
                if (secciones[secciones[i].vecinos[j]-1].desvio_inf == i+1):
                    #print("{} es el desvio de {}".format(i+1,secciones[i].vecinos[j])) 
                    secciones[i].tipo = "Desvio"
#%%
def cambios_herencia():

    for i in range(len(secciones)):
        if secciones[i].cambio == True:
            vecinos_totales = secciones[i].N_vecinos

            vecinos_secundarios = 0
            if secciones[i].desvio_sup != "":
                vecinos_secundarios = vecinos_secundarios + 1;
            if secciones[i].desvio_inf != "":
                vecinos_secundarios = vecinos_secundarios + 1;

            vecinos_principales = vecinos_totales - vecinos_secundarios

            if vecinos_principales > vecinos_secundarios:
                secciones[i].cambio_raiz = True
                #print("{} es un cambio raiz".format(i+1))
            else:
                secciones[i].cambio_raiz = False


#%%
def asignar_semaforos():
    for i in range(len(secciones)):
        #if(secciones[i].tipo == "Cruce" or secciones[i].tipo == "Desvio" ):
        if(secciones[i].cambio == True or secciones[i].tipo == "Desvio" ):    
            secciones[i].semaforo = True
            if (secciones[i].cambio_raiz == True):

                if(secciones[i].posterior != "" and secciones[i].anterior != "" and secciones[i].N_vecinos == 3):

                    #if (secciones[secciones[i].anterior-1].tipo != "Cruce"):
                    if (secciones[secciones[i].anterior-1].cambio == False):
                        (secciones[i].sem_sentido).append("<")
                        (secciones[i].N_aspectos).append("3")
                        #(secciones[i].aspecto).append("Rojo")
                        (secciones[i].aspecto).append(" ")

                    #if (secciones[secciones[i].posterior-1].tipo != "Cruce"):
                    if (secciones[secciones[i].posterior-1].cambio == False):    
                        (secciones[i].sem_sentido).append(">")
                        (secciones[i].N_aspectos).append("3")
                        #(secciones[i].aspecto).append("Rojo")
                        (secciones[i].aspecto).append(" ")


                if (secciones[i].desvio_sup != ""):
                    desvio = secciones[i].desvio_sup
                else:
                    desvio = ""

                while (desvio != ""):
                    #print("{} a {}".format(secciones[desvio-1].desvio_inf,desvio))
                    desvio = secciones[desvio-1].desvio_sup
                    if (secciones[i].desvio_sup_dir == ">"):
                        (secciones[i].sem_sentido).append(">")
                    else:
                        (secciones[i].sem_sentido).append("<")
                    (secciones[i].N_aspectos).append("2")
                    #(secciones[i].aspecto).append("Amarillo")
                    (secciones[i].aspecto).append(" ")

                if (secciones[i].desvio_inf != ""):
                    desvio = secciones[i].desvio_inf
                else:
                    desvio = ""

                while (desvio != ""):
                    #print("{} a {}".format(secciones[desvio-1].desvio_inf,desvio))
                    desvio = secciones[desvio-1].desvio_inf
                    if (secciones[i].desvio_inf_dir == ">"):
                        (secciones[i].sem_sentido).append(">")
                    else:
                        (secciones[i].sem_sentido).append("<")
                    (secciones[i].N_aspectos).append("2")
                    #(secciones[i].aspecto).append("Amarillo")
                    (secciones[i].aspecto).append(" ")

            else:   # Si no es raiz
                desvios = 0
                if (secciones[i].desvio_sup != ""):
                    desvios = desvios +1
                if (secciones[i].desvio_inf != ""):
                    desvios = desvios +1

                #print("{} tiene {}".format(i+1, desvios))

                if (desvios == 2):
                    if (secciones[secciones[i].desvio_sup - 1].cambio_raiz == True):
                        if (secciones[i].desvio_sup_dir == ">"):
                            (secciones[i].sem_sentido).append(">")
                        else:
                            (secciones[i].sem_sentido).append("<")
                        (secciones[i].N_aspectos).append("2")
                        #(secciones[i].aspecto).append("Amarillo")
                        (secciones[i].aspecto).append(" ")

                    if (secciones[secciones[i].desvio_inf - 1].cambio_raiz == True):
                        if (secciones[i].desvio_inf_dir == ">"):
                            (secciones[i].sem_sentido).append(">")
                        else:
                            (secciones[i].sem_sentido).append("<")
                        (secciones[i].N_aspectos).append("2")
                        #(secciones[i].aspecto).append("Amarillo")
                        (secciones[i].aspecto).append(" ")

                if (desvios == 1):
                    if (secciones[i].desvio_sup != ""):

                        if(secciones[i].desvio_sup_dir == ">"):
                            (secciones[i].sem_sentido).append(">")
                        else:
                            (secciones[i].sem_sentido).append("<")
                        (secciones[i].N_aspectos).append("2")
                        #(secciones[i].aspecto).append("Amarillo")
                        (secciones[i].aspecto).append(" ")

                    if (secciones[i].desvio_inf != ""):

                        if (secciones[i].desvio_inf_dir == ">"):
                            (secciones[i].sem_sentido).append(">")
                        else:
                            (secciones[i].sem_sentido).append("<")
                        (secciones[i].N_aspectos).append("2")
                        #(secciones[i].aspecto).append("Amarillo")
                        (secciones[i].aspecto).append(" ")

          
        if(secciones[i].tipo == "Extremo"):
            secciones[i].semaforo = True

            if (secciones[i].extremo == False):
                if(secciones[i].anterior != ""):

                    (secciones[i].sem_sentido).append(">")
                    (secciones[i].N_aspectos).append("3")
                    #(secciones[i].aspecto).append("Verde")
                    (secciones[i].aspecto).append(" ")

                if(secciones[i].posterior != ""):

                    (secciones[i].sem_sentido).append("<")
                    (secciones[i].N_aspectos).append("3")
                    #(secciones[i].aspecto).append("Verde")
                    (secciones[i].aspecto).append(" ")
            else:
                if (secciones[i].anterior != ""):
                    (secciones[i].sem_sentido).append("<")
                    (secciones[i].sem_sentido).append(">")
                    (secciones[i].N_aspectos).append("2")
                    (secciones[i].N_aspectos).append("2")
                    #(secciones[i].aspecto).append("Amarillo")
                    #(secciones[i].aspecto).append("Amarillo")
                    (secciones[i].aspecto).append(" ")
                    (secciones[i].aspecto).append(" ")

                if (secciones[i].posterior != ""):
                    (secciones[i].sem_sentido).append(">")
                    (secciones[i].sem_sentido).append("<")
                    (secciones[i].N_aspectos).append("2")
                    (secciones[i].N_aspectos).append("2")
                    #(secciones[i].aspecto).append("Amarillo")
                    #(secciones[i].aspecto).append("Amarillo")
                    (secciones[i].aspecto).append(" ")
                    (secciones[i].aspecto).append(" ")

        secciones[i].N_semaforos = len(secciones[i].N_aspectos)



#%%
def detectar_rutas(secciones, test = False):
    
    if test:
        print("#"*20)
    inicial = 0

    
    if test == True:
        imprimir = True
    else:
        imprimir = False
        
    for i in range(len(secciones)):
        inicial = i+1
               
        if (secciones[i].tipo == "Cruce" or secciones[i].tipo == "Desvio"):

            #print("Iniciales: {}".format(inicial))
            if (secciones[i].anterior != "" and (secciones[secciones[i].anterior-1].tipo == "Cruce" or secciones[secciones[i].anterior-1].tipo == "Desvio") and
                 secciones[i].posterior != "" and (secciones[secciones[i].posterior-1].tipo == "Cruce" or secciones[secciones[i].posterior-1].tipo == "Desvio")):
                continue
                
            if ('<' in secciones[i].sem_sentido and secciones[i].posterior != ""):# and secciones[secciones[i].posterior-1].tipo != "Cruce"):        
                recorrido = []
                semaforo_anterior(inicial,recorrido = recorrido, test = imprimir)
                
            if ('>' in secciones[i].sem_sentido and secciones[i].anterior != ""):# and secciones[secciones[i].anterior-1].tipo != "Cruce"):
                recorrido = []
                semaforo_siguiente(inicial,recorrido = recorrido, test = imprimir)

        if (secciones[i].tipo == "Extremo" and secciones[i].extremo == True):

            #print("Iniciales: {}".format(inicial))

            if ('<' in secciones[i].sem_sentido and secciones[i].anterior != ""):
                recorrido = []
                semaforo_anterior(inicial, recorrido=recorrido, test=imprimir)

            if ('>' in secciones[i].sem_sentido and secciones[i].posterior != ""):
                recorrido = []
                semaforo_siguiente(inicial, recorrido=recorrido, test=imprimir)
    if test:            
        print ("Rutas soportadas: {}".format(N_rutas))
#%%
def semaforo_anterior(inicial,intermedio = None, desvio = None,recorrido = [], test = False):
    
    global N_rutas
     
    if intermedio == None and desvio == None:
        recorrido = []
        
    if intermedio == None:
        inicio = secciones[inicial-1]
    else:
        inicio = secciones[intermedio-1]  
    
    if desvio != None:
        inicio = secciones[desvio-1] 
        
    if (inicio.anterior != ""):
        anterior = inicio.anterior
        recorrido.append(anterior)
        if (secciones[anterior-1].tipo == "Extremo" or 
            ((secciones[anterior-1].tipo == "Cruce" or secciones[anterior-1].tipo == "Desvio") and 
             secciones[secciones[anterior-1].posterior-1].semaforo == False)):
            
            recorrido.insert(0,inicial)
            
            if (recorrido[0] != inicial):
                recorrido.insert(0,inicial)
            
            if (recorrido[0] == recorrido[1]):
                recorrido.pop(0)
                
            camino = '-'.join(str(e) for e in recorrido)
        
            if (test == True):
                #print(camino)
                print("{} > {}".format(inicial,anterior))
            N_rutas = N_rutas + 1
            
            (tabla['Ruta']).append(N_rutas)
            (tabla['Inicial']).append(inicial)
            (tabla['Final']).append(anterior)
            (tabla['Secuencia']).append(camino)
            (tabla['Sentido']).append('<')
            
        else:    
            semaforo_anterior(inicial,anterior,recorrido = recorrido, test = test)
    
    #print("Volviendo a {}".format(inicio.id))  
    if inicio.id in recorrido:
        recorrido[recorrido.index(inicio.id)+1:] = []
    
    
        
    if (inicio.desvio_inf != "" and inicio.desvio_inf_dir == '<'): 
        if desvio != None:
            recorrido.append(desvio)
        #print("{}^{}".format(inicial,inicio.desvio_sup))
        recorrido.append(inicio.desvio_inf)   
        semaforo_anterior(inicial,desvio = inicio.desvio_inf,recorrido = recorrido, test = test)
        
    if (inicio.desvio_sup != "" and inicio.desvio_sup_dir == '<'):  
        if desvio != None:
            recorrido.append(desvio)
        #print("{}^{}".format(inicial,inicio.desvio_sup))
        recorrido.append(inicio.desvio_sup)    
        semaforo_anterior(inicial,desvio = inicio.desvio_sup,recorrido = recorrido, test = test)
#%%
def semaforo_siguiente(inicial,intermedio = None, desvio = None, recorrido = [],test = False):
    
    global N_rutas
        
    if intermedio == None and desvio == None:
        recorrido = []
        
    if intermedio == None:
        inicio = secciones[inicial-1] 
    else:
        inicio = secciones[intermedio-1]
   
    if desvio != None:
        inicio = secciones[desvio-1] 

    if (inicio.posterior != ""):
        posterior = inicio.posterior
        recorrido.append(posterior)
        if (secciones[posterior-1].tipo == "Extremo" or 
            ((secciones[posterior-1].tipo == "Cruce" or secciones[posterior-1].tipo == "Desvio") and 
             secciones[secciones[posterior-1].anterior-1].semaforo == False)):
            
            if (recorrido[0] != inicial):
                recorrido.insert(0,inicial)
            
            if (recorrido[0] == recorrido[1]):
                recorrido.pop(0)
                
            camino = '-'.join(str(e) for e in recorrido)
            
            if (test == True):        
                #print(camino)
                print("{} > {}".format(inicial,posterior))
                
            N_rutas = N_rutas + 1
                    
            (tabla['Ruta']).append(N_rutas)
            (tabla['Inicial']).append(inicial)
            (tabla['Final']).append(posterior)
            (tabla['Secuencia']).append(camino)
            (tabla['Sentido']).append('>')
           
        else:
            semaforo_siguiente(inicial,posterior,recorrido = recorrido, test = test)

    #print("Volviendo a {}".format(inicio.id))  
    if inicio.id in recorrido:
        recorrido[recorrido.index(inicio.id)+1:] = []
         
    if (inicio.desvio_inf != "" and inicio.desvio_inf_dir == '>'): 
        if desvio != None:
            recorrido.append(desvio)
        #print("{}^{}".format(inicial,inicio.desvio_sup))
        recorrido.append(inicio.desvio_inf)      
        semaforo_siguiente(inicial,desvio = inicio.desvio_inf, recorrido = recorrido, test = test)
    
    if (inicio.desvio_sup != "" and inicio.desvio_sup_dir == '>'):
        if desvio != None:
            recorrido.append(desvio)
        #print("{}^{} de {}".format(inicial,inicio.desvio_sup,inicio.id))
        recorrido.append(inicio.desvio_sup)
        semaforo_siguiente(inicial,desvio = inicio.desvio_sup, recorrido = recorrido, test = test)

#%%           
def analizar_tabla(tabla,test = False):
        
    tabla2 = {'Ruta': [],
        'Inicial': [],
        'Final': [],
        'Secuencia': [],
        'Sentido' : []
        }
    n = 0
    
    rutas = []
    
    for i in range(len(tabla['Inicial'])):    
        rutas.append([tabla['Inicial'][i],tabla['Final'][i]])
        
    #print(rutas)
      
    repetido = []

    unico = []

    indices = []
    
    for x in rutas:

    	if x not in unico:
    
            unico.append(x)
            index = rutas.index(x)
            indices.append(index)
            
            n = n +1
            tabla2['Ruta'].append(n) 
            tabla2['Inicial'].append(tabla['Inicial'][index]) 
            tabla2['Final'].append(tabla['Final'][index]) 
            tabla2['Secuencia'].append(tabla['Secuencia'][index]) 
            tabla2['Sentido'].append(tabla['Sentido'][index]) 
    	else:
    
    		if x not in repetido:  
    			repetido.append(x)             
                
#    print("$$$")          
#    print(unico)
#    print("$$$") 
#    print(repetido)
#    print("$$$") 
#    print(indices)
    
        
    #print(tabla2)
    if test:
        print ("Rutas optimizadas: {}".format(n))
    return tabla2
#%%
def generar_mapa(tabla, iniciar = True):
    v = 0.5
    
    print("@"*25+" Analizador de grafos v"+str(v)+" "+"@"*25+"\n")
    
    for i in range(len(archivos)):
            
        # Falta corregir desvios
        if i != 8:          # 8 u 2
            continue
         
        secciones.clear()
        conexiones.clear()
        
        ax = plt.gca()
        ax.cla() # clear things for fresh plot
        
        print("%"*25+" Mapa_"+str(i)+' '+"%"*25)  
            
        cargar_secciones(archivos[i][0],archivos[i][1])
        
        axis = [[-0.5,10.5],[-2.5,2.5]]
        
        axis = calcular_ejes(secciones)
        
        #print(axis)       
        
        adj = 0.75 
        ax.set_xlim((axis[0][0]-3*r, axis[0][1]+3*r))
        ax.set_ylim((axis[1][0]-adj, axis[1][1]+adj))
                
        if axis[0][1] > 7:
            ajuste = 4
        else:
            ajuste = 3
              
        buscar_vecinos()       
        clasificar_vecinos()        
        asignar_tipo()    
        cambios_herencia()
        asignar_semaforos()
        #imprimir_estados()       
        
        mostrar_grafo(secciones,i,gif_mode = False)       
        #proximo_semaforo(secciones)    
        detectar_rutas(secciones)        
        #dibujar_barrera(5.5,-1, b = 1, h = 3, c = [0.85,0.85,0.85])           
       
        #print(tabla)    
        #tabla = analizar_tabla(tabla)
        #print(tabla)      
        #(df).append(pd.DataFrame(tabla, columns = ['Ruta', 'Inicial', 'Final', 'Secuencia','Sentido'])) 
    #exportar_tablas(df)
    

    
#%% 
def conectar_terminal(secciones):
    print("UART > Conectando")    
    uart_main(secciones,conexiones)
    print("UART > Desconectado") 
    
#%%  
def main():

    generar_mapa(tabla)
    
    crear_modulo_vhdl(secciones,tabla)
    
    #conectar_terminal(secciones)
    
    #generar_mapa(tabla,False)
    #mostrar_grafo(secciones)
    
    
if __name__ == "__main__":
    main()
    
    