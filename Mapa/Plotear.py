from circles import *
from matplotlib.patches import Rectangle

from Estaciones import *



global r

r = 0.14

grey1 = (0.65,0.65,0.65)
#grey2 = (0.45,0.45,0.45)
grey2 = (0.9,0.9,0.9)
grey3 = (0.35,0.35,0.35)
red = (0.8,0.2,0.5)
violet = (0.6,0.0,0.5)

def dibujar_semaforo(pos_x,pos_y, b = 0.2, h = 0.2, c = 'g'):
    
    rect = Rectangle((pos_x, pos_y), b, h, color = c)
    ax.add_artist(rect)


def dibujar_barrera(pos_x,pos_y, b = 0.2, h = 0.2, c = 'g'):
    
    rect = Rectangle((pos_x, pos_y), b, h, color = c)
    ax.add_artist(rect)
    
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
        fc = red
        
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
    ax.plot([x1,mid_point[0]], [y1,mid_point[1]], color = c , linewidth = lw)
    ax.plot([mid_point[0],x2], [mid_point[1],y2], color = c , linewidth = lw)

