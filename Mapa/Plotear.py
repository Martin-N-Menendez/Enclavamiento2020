from circles import *
from matplotlib.patches import Rectangle
from pylab import rcParams

from Estaciones import *

import matplotlib.pyplot as plt

global plt

global r

global ax 

r = 0.14

grey1 = (0.65,0.65,0.65)
#grey2 = (0.45,0.45,0.45)
grey2 = (0.9,0.9,0.9)
grey3 = (0.35,0.35,0.35)
red = (0.8,0.2,0.5)
black = (0.2,0.2,0.2)
violet = (0.6,0.0,0.5)

def dibujar_semaforo(pos_x,pos_y, b = 0.2, h = 0.2, c = 'g'):
    
    rect = Rectangle((pos_x, pos_y), b, h, color = c)
    plt.add_artist(rect)


def dibujar_barrera(pos_x,pos_y, b = 0.2, h = 0.2, c = 'g'):
    
    rect = Rectangle((pos_x, pos_y), b, h, color = c)
    plt.add_artist(rect)
    
def conectar_central(estaciones):
    
    for i in range(len(estaciones)):
        create_line(0,0,estaciones[i].pos_x,estaciones[i].pos_y)

#%%
def conectar_secciones_b(secciones,conexiones):
    
   
    for i in range(len(conexiones)):
        
        a = conexiones[i][0]
        b = conexiones[i][1]

        if ( secciones[a].tipo == "Cruce" and
             secciones[b].tipo == "Cruce" ):
            
            if secciones[a].cambio_estado == True:
                color = grey2
        else:
            color = grey1
        
        if ( secciones[b].tipo == "Cruce" and len(secciones[b].vecinos) == 3 ):
            if ( secciones[b].desvio_sup != "" ):              
                if ( secciones[b].desvio_sup_dir == '>'):
                    if ( secciones[b].posterior == secciones[a].id ):
                        if secciones[b].cambio_estado == False:
                            color = grey2
                else:
                    if ( secciones[b].anterior == secciones[a].id ):
                        if secciones[b].cambio_estado == False:
                            color = grey2
        
                
        if ( secciones[a].tipo == "Cruce" and len(secciones[a].vecinos) == 3 ):
            if ( secciones[a].desvio_sup != "" ):              
                if ( secciones[a].desvio_sup_dir == '>'):
                    if ( secciones[a].posterior == secciones[b].id ):
                        if secciones[a].cambio_estado == False:
                            color = grey2
                else:
                    if ( secciones[a].anterior == secciones[b].id ):
                        if secciones[a].cambio_estado == False:
                            color = grey2         
            
        create_line(secciones[a].pos_x, secciones[a].pos_y,
                    secciones[b].pos_x, secciones[b].pos_y,
                    c = color)
        
#%%
def conectar_secciones(secciones):
       
    for i in range(len(secciones)):
        
        for j in range(secciones[i].N_vecinos):
            #print("{}|{}".format(i+1,secciones[i].vecinos[j]))
            a = i
            b = secciones[i].vecinos[j]-1
            
            # Evitar repetidos             
            if ( a < b ):
                continue;
             
            #print("O {} {}".format(a+1,b+1))
            
            color = grey1
            tipo_a = secciones[a].tipo
            tipo_b = secciones[b].tipo
            
            if ( tipo_a == "Cruce"):
                if ( tipo_b == "Directo"):  
                    print("C-Di {} {}".format(a+1,b+1))
                    if secciones[a].cambio_estado == True:
                        color = grey2
                if ( tipo_b == "Desvio"):  
                    print("C-De {} {}".format(a+1,b+1))
                    if secciones[a].cambio_estado == False:
                        color = grey2
                
            if ( tipo_b == "Cruce"):
                if ( tipo_a == "Directo"):    
                    print("Di-C {} {}".format(a+1,b+1))
                    if secciones[b].cambio_estado == True:
                        color = grey2  
                if ( tipo_a == "Desvio"): 
                    print("De-C {} {}".format(a+1,b+1))
                    if secciones[b].cambio_estado == False:
                        color = grey2

#            if ( tipo_a == "Desvio"):
#                if ( tipo_b == "Directo"):  
#                    print("De-Di {} {}".format(a+1,b+1))
#                    if secciones[a].cambio_estado == True:
#                        color = red
#                if ( tipo_b == "Desvio"):  
#                    print("De-De {} {}".format(a+1,b+1))
#                    if secciones[a].cambio_estado == False:
#                        color = red
                
            if ( tipo_b == "Desvio"):
                if ( tipo_a == "Directo"):    
                    print("Di-De {} {}".format(a+1,b+1))
                    if secciones[b].cambio_estado == True:
                        color = grey2  
                if ( tipo_a == "Desvio"): 
                    print("De-De {} {}".format(a+1,b+1))
                    if secciones[b].cambio_estado == False:
                        color = grey2           
                        


            
            create_line(secciones[a].pos_x, secciones[a].pos_y,
                        secciones[b].pos_x, secciones[b].pos_y,
                        c = color)    

 #%%       
def dibujar_secciones(secciones,ajuste = 5):
    
    for i in range(len(secciones)):
        if(secciones[i].tipo == "Extremo"):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = violet,centro = secciones[i].ocupado, ajuste = ajuste)
        if(secciones[i].tipo == "Simple"):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'b',centro = secciones[i].ocupado, ajuste = ajuste)
        
        if(secciones[i].tipo == "Directo"):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'y',centro = secciones[i].ocupado, ajuste = ajuste)
        if(secciones[i].tipo == "Desvio"):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'r',centro = secciones[i].ocupado, ajuste = ajuste)    
        if(secciones[i].cambio == True):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'g',centro = secciones[i].ocupado, ajuste = ajuste)
        if(secciones[i].tipo == ""):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'k',centro = secciones[i].ocupado, ajuste = ajuste)     
        if(secciones[i].barrera == True):
            dibujar_seccion(secciones[i].pos_x,secciones[i].pos_y,secciones[i].id,c = 'c',centro = secciones[i].ocupado, ajuste = ajuste)
 #%%             
def dibujar_seccion(x,y,index, r=r,c='b',fc = 'w', centro = False, ajuste = 1):
    if centro == True:
        fc = black
        
    circles(x, y, r, ec=c,fc = fc, lw = 20/ajuste, zo = 100) 
    
    if int(index) > 9:
        adj_x = 0.1
        adj_y = 0.35
    else:
        adj_x = 0.05
        adj_y = 0.35

        
    plt.text(x-adj_x, y-adj_y, index , family="sans-serif", weight="bold", size = 40/ajuste)

 #%% 
def create_line(x1,y1,x2,y2,r = r, lw = 15, c = grey1):
           
#    adj = 0.05*0
    
    mid_point = None
    if abs(x1 - x2) < abs(y1 - y2):
        if y2 < y1:
            # down
            m = -1                
        else:
            # up
            m = 1 
            
        mid_point = (x2, m * abs(x1-x2) + y1)
        #print("<{} , {}>".format(round(mid_point[0],2),round(mid_point[1],2)))
    else:
        if x2 < x1:
            # left
            m = -1
        else:
            # right
            m = 1


        mid_point = (m * abs(y2 - y1) + x1, y2)
        #print("<{} , {}>".format(round(mid_point[0],2),round(mid_point[1],2)))    
        
    # draw lines
    plt.plot([x1,mid_point[0]], [y1,mid_point[1]], color = c , linewidth = lw)
    plt.plot([mid_point[0],x2], [mid_point[1],y2], color = c , linewidth = lw)

#%%
def actualizar_semaforos(x,y,sem_sentido,cantidad,estado,adj):
    
    ajuste = 0.15
    
    fuente = 40/adj
    
    m = 1
    if sem_sentido == '>':    
        if estado == 'Rojo':
            plt.text(x, y, sem_sentido , color = 'r', family="sans-serif", weight="bold", size = fuente) 
        else:
            plt.text(x, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
            
        if estado == 'Amarillo':
            plt.text(x+m*ajuste, y, sem_sentido , color = 'y', family="sans-serif", weight="bold", size = fuente)  
        else:
            plt.text(x+m*ajuste, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
        
        m = m + 1          
        if cantidad == 3:            
            if estado == 'Verde':
                plt.text(x+m*ajuste, y, sem_sentido , color = 'c', family="sans-serif", weight="bold", size = fuente)  
            else:
                plt.text(x+m*ajuste, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
    
    m = 1
    if sem_sentido == '<': 
        if cantidad == 3:            
            if estado == 'Verde':
                plt.text(x, y, sem_sentido , color = 'c', family="sans-serif", weight="bold", size = fuente)  
            else:
                plt.text(x, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
        else:
            m = 0
        if estado == 'Amarillo':
            plt.text(x+m*ajuste, y, sem_sentido , color = 'y', family="sans-serif", weight="bold", size = fuente)  
        else:
            plt.text(x+m*ajuste, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
         
        m = m + 1
        if estado == 'Rojo':
            plt.text(x+m*ajuste, y, sem_sentido , color = 'r', family="sans-serif", weight="bold", size = fuente) 
        else:
            plt.text(x+m*ajuste, y, sem_sentido , color = 'k', family="sans-serif", weight="bold", size = fuente) 
            
#%%
def imprimir_semaforos(secciones,ajuste):
     
    for i in range(len(secciones)):
        if (secciones[i].semaforo):
            for j in range(len(secciones[i].N_aspectos)):
                ajuste_x = 0
                ajuste_y = 0
                L = int(secciones[i].N_aspectos[j])
                
                x = secciones[i].pos_x
                y = secciones[i].pos_y
                
                if (secciones[i].desvio_sup != ""):
                    ajuste_x = -0.07*L
                    ajuste_y = -0.5-0.15*j
                else:
                    ajuste_x = -0.07*L
                    ajuste_y =  0.25+0.15*j
                                                 
                x = x + ajuste_x
                y = y + ajuste_y
              
                if len(secciones[i].N_aspectos) == len(secciones[i].aspecto):
                    actualizar_semaforos(x,y,secciones[i].sem_sentido[j],L,secciones[i].aspecto[j],ajuste)
                else:
                    actualizar_semaforos(x,y,secciones[i].sem_sentido[j],L,"",ajuste)
#%%
def calcular_ejes(secciones):
    
    mplt_x = 0.0
    mplt_y = 0.0
    min_x = 0.0
    min_y = 0.0
        
    for i in range(len(secciones)):
                
        if(secciones[i].pos_x > mplt_x):         
            mplt_x = secciones[i].pos_x
       
        if(secciones[i].pos_x < min_x):
            min_x = secciones[i].pos_x
       
        if(secciones[i].pos_y > mplt_y):
            mplt_y = secciones[i].pos_y
         
        if(secciones[i].pos_y < min_y):
            min_y = secciones[i].pos_y
            
        #print(i,[[min_x,mplt_x],[min_y,mplt_y]])   
        
    return [[min_x,float(mplt_x)],[min_y,mplt_y]]

#%% 
def mostrar_grafo(secciones,i = 0,j = 0, gif_mode = False):
    
    adj = 0.75 
    r = 0.14
    
    axis = [[-0.5,10.5],[-2.5,2.5]]    
    axis = calcular_ejes(secciones)
    
    #plt.figure(figsize=(16,9))
    
    ax = plt.gca()
    ax.cla() # clear things for fresh plot
    
    ax.set_xlim((axis[0][0]-3*r, axis[0][1]+3*r))
    ax.set_ylim((axis[1][0]-adj, axis[1][1]+adj))
        
    if axis[0][1] > 7:
        ajuste = 4
    else:
        ajuste = 3
    
    #plt.figure(figsize=(16,9))
    
    #cargar_secciones(archivos[i][0],archivos[i][1])
        
    dibujar_secciones(secciones,ajuste)
    conectar_secciones(secciones)     
    imprimir_semaforos(secciones,ajuste)    
     
    #plt.figure(figsize=(16,9))
    
    ax.axis('off')
    
    if gif_mode:  
        #fig = plt.gcf()
        #fig.set_size_inches(16, 9)
        #plt.figure(figsize=(16,9))
        plt.savefig('Mapas/Mapa_'+str(i)+'('+str(j)+').png',dpi = 100)
    else:
        #fig = plt.gcf()
        #fig.set_size_inches(16, 9)
        #plt.figure(figsize=(16,9))
        plt.savefig('Mapas/Mapa_'+str(i)+'.png',dpi = 100)
        
    plt.show()
    
    
    
    