import networkx as nx

#%%
def Calcular_conexiones(G):

    Secciones = nx.number_of_nodes(G)
    
    
    for i in range(Secciones):
        vecinos = [n for n in G.neighbors(str(i+1))]
        if (G.node[str(i+1)]['Barrera'] == 'No'):
            print("Sección {} conectado a : {}".format(i+1,vecinos)) 
        else:
            j = 0
            while j < len(vecinos):    
                if(G.node[vecinos[j]]['pos'][1] != 0):
                    vecinos.remove(vecinos[j])
                    j = j -1                  
                j = j + 1
            print("Sección {} conectado a : {}".format(i+1,vecinos)) 
#%%
def Calcular_Secciones(G):
    
    Secciones = nx.number_of_nodes(G)

    print("# Secciones : {}".format(Secciones))
                
#%% 
def Clasificar_Secciones(G, modo = 'normal'):

    N = nx.number_of_nodes(G)
    
    cambios = Detectar_Cambios(G)
    secundarios = []
    
    posicion_cambios = []
    
    estaciones = []
    extremos = []
    
    for i in range(len(cambios)):
        posicion_cambios.append(nx.get_node_attributes(G,'pos')[cambios[i]])
        #print("Posicion del cambio en CV_{} : {}".format(cambios[i],posicion_cambios[i]))
      
    for i in range(N):
        for j in range(len(cambios)):
            
            if nx.get_node_attributes(G,'pos')[str(i+1)][0] ==  posicion_cambios[j][0]:
                if str(i+1) in cambios:
                    continue;
                secundarios.append(str(i+1))
                G.nodes[str(i+1)]["Cambio"] = 'Normal'
       
    for i in range(N):
        vecinos = [n for n in G.neighbors(str(i+1))]
        densidad = len(vecinos)
                   
        if densidad == 1:
           extremos.append(str(i+1))         
          
        if densidad == 2:
            if  vecinos == cambios or vecinos == secundarios :
                estaciones.append(str(i+1))
    
    if modo == "test":      
        print("\r\n")
        print("Cambios : {} | {}".format(cambios,secundarios))
        print("Estaciones : {}".format(estaciones))
        print("Extremos : {}".format(extremos))
        
    return cambios,secundarios,estaciones,extremos

 #%%    
def Imprimir_estados(G):
    
    N = nx.number_of_nodes(G)
    
    print("\n")
    
    for i in range(N):
        print("CV_{}".format(i+1))
        if G.nodes[str(i+1)]["Semaforo"] == 'No':
            print("\t Semaforo: No tiene")
        else:
            print("\t Semaforo: {} aspectos".format(G.nodes[str(i+1)]["Semaforo"]))    
            print("\t Aspecto : {}".format(G.nodes[str(i+1)]["Aspecto"]))
            print("\t Direccion : {}".format(G.nodes[str(i+1)]["Direccion"]))
         
        if G.nodes[str(i+1)]["Barrera"] == 'No':
            print("\t Barrera: No tiene")
        else:
            print("\t Barrera: posición {}".format(G.nodes[str(i+1)]["Barrera"]))    
  
        if G.nodes[str(i+1)]["Cambio"] == 'No':
            print("\t Cambio: No tiene")
        else:
            print("\t Cambio: posición {}".format(G.nodes[str(i+1)]["Cambio"]))

        print("\t Ocupación : {}".format(G.nodes[str(i+1)]["Ocupado"]))
        
#%%
def Calcular_Barreras(G,modo = 'normal'):

    N = nx.number_of_nodes(G)
    
    barreras = []
    
    for i in range(N):
      
        vecinos = [n for n in G.neighbors(str(i+1))]
                
        if len(vecinos) == 4 :  
            barreras.append(str(i+1))   
            G.nodes[str(i+1)]["Barrera"] = {"Estado":"Bajo"}
    
    if modo == 'info':       
        print("Barreras : {}".format(barreras))
    if modo == 'cantidad':     
        print("# Barreras : {}".format(len(barreras)))
              
    print("# Barreras : {}".format(len(barreras)))   
                    


#%%
def Detectar_Cambios(G,modo = 'normal'):

    N = nx.number_of_nodes(G)
    
    cambios = []
    for i in range(N):
      
        vecinos = [n for n in G.neighbors(str(i+1))]
                
        if len(vecinos) == 3 :  
            cambios.append(str(i+1))   
            G.nodes[str(i+1)]["Cambio"] = 'Normal'
            
    if modo == 'info':       
        print("Cambios : {}".format(cambios))
    if modo == 'cantidad':     
        print("# Cambios : {}".format(len(cambios)))
              
    return cambios

#%%  
def Detectar_Secundarios(G):
   
    N = nx.number_of_nodes(G)
    
    posicion_cambios = []
    
    cambios = Detectar_Cambios(G)
    
    secundarios = []
     
    for i in range(len(cambios)):
        posicion_cambios.append(nx.get_node_attributes(G,'pos')[cambios[i]])
      
    for i in range(N):
        for j in range(len(cambios)):
            
            if nx.get_node_attributes(G,'pos')[str(i+1)][0] ==  posicion_cambios[j][0]:
                if str(i+1) in cambios:
                    continue;
                secundarios.append(str(i+1))
    
    return secundarios
 
#%%  
def Detectar_Extremos(G):
   
    N = nx.number_of_nodes(G)   
    
    extremos = []
     
    for i in range(N):
        vecinos = [n for n in G.neighbors(str(i+1))]
        densidad = len(vecinos)
                   
        if densidad == 1:
           extremos.append(str(i+1))         

    return extremos
#%%  
def Detectar_Estaciones(G):
   
    N = nx.number_of_nodes(G)
    
    estaciones = []
    
    cambios = Detectar_Cambios(G) 
    
    secundarios = Detectar_Secundarios(G)
     
    for i in range(N):
        vecinos = [n for n in G.neighbors(str(i+1))]
        densidad = len(vecinos)      
          
        if densidad == 2:
            if  vecinos == cambios or vecinos == secundarios :
                estaciones.append(str(i+1))
    
    return estaciones
    
#%%    
def Detectar_Semaforos(G,modo = 'normal'):
   
    N = nx.number_of_nodes(G)
    CV = list(G.nodes)
    
    cambios = Detectar_Cambios(G)   
    secundarios = Detectar_Secundarios(G)    
    extremos = Detectar_Extremos(G)  
    estaciones = Detectar_Estaciones(G)
    
    otros = set(CV) - set(cambios) - set(secundarios) - set(extremos) - set(estaciones)
    
    dos_aspectos = []
    tres_aspectos = []
      
    for i in range(N):
        if str(i+1) in cambios:
            dos_aspectos.append(str(i+1))
            tres_aspectos.append(str(i+1))
            tres_aspectos.append(str(i+1))
            G.nodes[str(i+1)]["Semaforo"] = [2,3,3]
            G.nodes[str(i+1)]["Direccion"] = ['>','>','<']
            #Grafo.nodes[str(i+1)]["Aspecto"] = ["Rojo","Rojo","Rojo"]
        if str(i+1) in secundarios:
            dos_aspectos.append(str(i+1))
            G.nodes[str(i+1)]["Semaforo"] = [2]
            #Grafo.nodes[str(i+1)]["Aspecto"] = ["Rojo"]
        if str(i+1) in otros:
             tres_aspectos.append(str(i+1))
             G.nodes[str(i+1)]["Semaforo"] = [3]
             #Grafo.nodes[str(i+1)]["Aspecto"] = ["Rojo"]
    
    if modo == "test":          
        print("# Semaforos : {} = [{} | {}]".format(len(dos_aspectos+tres_aspectos),len(dos_aspectos),len(tres_aspectos)))    
   
    return dos_aspectos,tres_aspectos

#%% 
def Calcular_Semaforos(G):

    dos_aspectos,tres_aspectos = Detectar_Semaforos(G)
    
    print("# Semaforos : {} = [{} | {}]".format(len(dos_aspectos+tres_aspectos),len(dos_aspectos),len(tres_aspectos)))    
          
          
#%%
def Calcular_proximo(G,i):    
           
    cambios,secundarios,estaciones,extremos = Clasificar_Secciones(G)
    
    anterior = []
    proximo = []
    
       
    vecinos = [n for n in G.neighbors(str(i+1))]
   
    if str(i+1) in extremos:  
        
        
        proximo = vecinos[0]
        
        print("{} >> {}".format(str(i+1),proximo))
        
    if len(vecinos) == 2:            
        
        
        anterior = vecinos[0]
        proximo = vecinos[1]
        
        print("{} << {} >> {}".format(anterior,str(i+1),proximo))

        
    if len(vecinos) == 3:            
        print("{} << {} >> {}(Normal) | {}(Reverso)".format(vecinos[0],str(i+1),vecinos[1],vecinos[2]))              
        anterior = vecinos[0]
        proximo = vecinos[1]        
    
    return anterior,proximo