#%% VHDL

FALSO = 0
VERDADERO = 1

def incluir_librerias(f):
    f.write("library IEEE;\n")
    f.write("use IEEE.std_logic_1164.all;\n")
    f.write("use IEEE.numeric_std.all;\r\n")
 
#%%
def crear_objeto_s_i(f,modulo,i):
    
    modulo.cantidad = i+1
    
    #print("cambio {} : {}".format(i+1,modulo.puertos_in))
    
    crear_objeto_s(f,modulo)
    
#%%       
def crear_objeto_s(f,modulo):
    
    if(modulo.instancia == "entidad"):
        destino = "entity"  
        profundidad = 1
    if(modulo.instancia == "componente"):
        destino = "component"
        profundidad = 2
        
        
#    if(modulo.nombre == "semaforo"):
#        print(modulo.dimension)  
#        for i in range(len(modulo.puertos_in + modulo.puertos_out)):    
#            if (modulo.dimension[i] != "1"):
#                print("NO!")
    if( modulo.cantidad == 0 ):               
        f.write("\t"*(profundidad-1)+"--"+modulo.instancia+" de "+modulo.nombre+"\n")
    
        f.write("\t"*(profundidad-1)+destino+" "+modulo.nombre+" is\n") 
    else:
        
        f.write("\t"*(profundidad-1)+"--"+modulo.instancia+"_"+str(modulo.cantidad)+" de "+modulo.nombre+"\n")
    
        f.write("\t"*(profundidad-1)+destino+" "+modulo.nombre+"_"+str(modulo.cantidad)+" is\n") 
        
    N_generico = len(modulo.generico)
    
    if (N_generico > 0):
        f.write("\t"*profundidad+"generic(\n")
        for i in range(N_generico):
            ultimo = VERDADERO if (i==N_generico-1) else FALSO
             
            f.write("\t"*(profundidad+1)+modulo.generico[i]+" : natural := "+modulo.dimension_generico[i])
            if(ultimo == FALSO):
                f.write(";\n")
            else:
                f.write("\n")
                
        f.write("\t"*profundidad+");\n")
    
    
    f.write("\t"*profundidad+"port(\n")
    
    puertos = modulo.puertos_in + modulo.puertos_out
    
    N_puertos = len(puertos)        
    
    for i in range(N_puertos):
        ultimo = VERDADERO if (i==N_puertos-1) else FALSO
        
        if (modulo.dimension[i] != "1"):
            modulo.tipos[i] = "std_logic_vector("+modulo.dimension[i]+"-1 downto 0)"
        crear_puerto(puertos[i],modulo.sentidos[i],modulo.tipos[i],f,ultimo,profundidad)
    
    f.write("\t"*profundidad+");\n")
        
    if( modulo.cantidad == 0 ):               
        f.write("\t"*(profundidad-1)+"end "+destino+" "+modulo.nombre+";\r\n") 
    else:     
        f.write("\t"*(profundidad-1)+"end "+destino+" "+modulo.nombre+"_"+str(modulo.cantidad)+";\r\n")
        
    
    
#%%       
def crear_objeto(f,nombre_i,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia):
    
    if(instancia == "entidad"):
        destino = "entity"  
        profundidad = 1
    if(instancia == "componente"):
        destino = "component"
        profundidad = 2
        
    f.write("\t"*(profundidad-1)+"--"+instancia+" de "+nombre_i+"\n")
    
    f.write("\t"*(profundidad-1)+destino+" "+nombre_i+" is\n") 
        
    N_generico = len(generico)
    
    if (N_generico > 0):
        f.write("\t"*profundidad+"generic(\n")
        for i in range(N_generico):
            ultimo = VERDADERO if (i==N_generico-1) else FALSO
             
            f.write("\t"*(profundidad+1)+generico[i]+" : natural := "+dimension_generico[i])
            if(ultimo == FALSO):
                f.write(";\n")
            else:
                f.write("\n")
                
        f.write("\t"*profundidad+");\n")
    
    
    f.write("\t"*profundidad+"port(\n")
    
    N_puertos = len(puertos)        
    
    for i in range(N_puertos):
        ultimo = VERDADERO if (i==N_puertos-1) else FALSO
        
        if (dimension[i] != "1"):
            tipos[i] = "std_logic_vector("+dimension[i]+"-1 downto 0)"
        crear_puerto(puertos[i],sentidos[i],tipos[i],f,ultimo,profundidad)
    
    f.write("\t"*profundidad+");\n")
        
    f.write("\t"*(profundidad-1)+"end "+destino+" "+nombre_i+";\r\n")
    
#%% 
def definir_entidad(f,nombre):
    f.write("entity "+nombre+" is\n")   
#%% 
def definir_componente(f,nombre):
    f.write("component "+nombre+" is\n") 
       
#%%        
def crear_puerto(nombre,sentido,tipo,f,last,profundidad):  
     
    f.write("\t"*(profundidad+1)+nombre+" : "+sentido+" "+tipo)
    if(last == FALSO):
        f.write(";\n")
    else:
        f.write("\n")