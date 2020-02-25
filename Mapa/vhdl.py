import numpy as np
  
def crear_modulo_vhdl(secciones,tabla):

 
    print("%"*25+" Iniciando creacion de modulos "+"%"*25)    
    
    objetos = calcular_paquete(secciones)
    
    creando_paquete(secciones,objetos)
    
    creando_wrapper(secciones,objetos)
    
    creando_separador(secciones,objetos)
    
    creando_mediador(secciones,objetos)
    
    creando_red(secciones,objetos,tabla)
    
    creando_nodo(secciones,objetos)
    
    creando_cambio(secciones,objetos)
    
    
    print("%"*25+" Finalizando creacion de modulos "+"%"*25) 

#%%
def calcular_paquete(secciones):
    
    N = 0
    M = 0
    n_vias = 0
    n_semaforos = 0
    n_pans = 0
    n_cambios = 0
 
    print("Paquete > Calculando") 
    
    for i in range(len(secciones)):
        #print ("Nodo: {}".format(i+1))
        n_vias = n_vias + 1
        if secciones[i].semaforo:
            n_semaforos = n_semaforos + secciones[i].N_semaforos
        if secciones[i].barrera:
            n_pans = n_pans + 1    
        if secciones[i].cambio:
            n_cambios = n_cambios + 1
            
    N = n_vias + n_semaforos + n_pans + n_cambios
    M = n_semaforos + n_pans + n_cambios
    
    print ("Paquete > N : {} | M : {}".format(N,M))
    print ("Paquete > CVS : {} | SEM : {} | PAN : {} | MDC : {}".format(n_vias,n_semaforos,n_pans,n_cambios))
    
    return [n_vias,n_semaforos,n_pans,n_cambios]
#%%
def incluir_librerias(f,paquete = False):
    
    f.write("library IEEE;\n")
    f.write("use IEEE.std_logic_1164.all;\n")
    f.write("use IEEE.numeric_std.all;\r\n")
    if (paquete):
        f.write("--Declare the package\r\n")
        f.write("use work.my_package.all;\r\n")
#%%    
def creando_paquete(secciones,objetos):        
    
    print("Paquete > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + N_SEM + N_PAN + N_MDC
    
    NODO = "paquete_pkg"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f) # Incluir librerias
        
    paquete = "my_package"  
    f.write("\t"+"package "+paquete+" is\n")
    
    tipo = "sems_type"
    f.write("\t\t"+"type "+tipo+" is record"+"\n")
    f.write("\t\t\t"+"msb"+" : "+"std_logic_vector("+str(N_SEM)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"lsb"+" : "+"std_logic_vector("+str(N_SEM)+"-1 downto 0);"+"\n")
    f.write("\t\t"+"end record "+tipo+";\r\n")
    
    tipo = "sem_type"
    f.write("\t\t"+"type "+tipo+" is record"+"\n")
    f.write("\t\t\t"+"msb"+" : "+"std_logic;"+"\n")
    f.write("\t\t\t"+"lsb"+" : "+"std_logic;"+"\n")
    f.write("\t\t"+"end record "+tipo+";\r\n")
    
    f.write("\t\t"+"type int_array is array(0 to "+str(N_SEM)+"-1) of integer;"+"\r\n")
    
    f.write("\t"+"end "+paquete+";\n")  
    
    f.close()  # Close header file
    
    
    print("Paquete > Finalizado")
#%%    
def creando_wrapper(secciones,objetos):        
    
    print("Sistema > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "enclavamiento"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,True) # Incluir librerias
        
    wrapper = "enclavamiento"
    f.write("\t"+"entity "+wrapper+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")  
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:         
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"paquete_ok"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Paquete_i"+ " : "+" in "+"std_logic_vector("+str(N)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Paquete_o"+    " : "+" out "+"std_logic_vector("+str(M)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+wrapper+";\n")
   
    f.write("architecture Behavioral of "+wrapper+" is\r\n") 
    
    # componente separador
    separador = "separador"
    f.write("\t"+"component "+separador+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"paquete_ok"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Paquete"+    " : "+" in "+"std_logic_vector("+str(N)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"Ocupacion"+    " : "+" out "+"std_logic_vector("+str(N_CVS)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"semaforos"+ " : "+" out "+"sems_type;"+"\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras"+ " : "+" out "+"std_logic_vector("+str(N_PAN)+"-1 downto 0);"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras"+ " : "+" out "+"std_logic;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" out "+"std_logic_vector("+str(N_MDC)+"-1 downto 0)"+";\n")    
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")    
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+separador+";\r\n")
     
    # componente red
    red = "red"
    f.write("\t"+"component "+red+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
    
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    
    f.write("\t\t\t"+"Ocupacion"+    " : "+" in "+"std_logic_vector("+str(N_CVS)+"-1 downto 0)"+";\n") 
    f.write("\t\t\t"+"semaforos_i"+ " : "+" in "+"sems_type;"+"\n")
    f.write("\t\t\t"+"semaforos_o"+ " : "+" out "+"sems_type;"+"\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras_i"+ " : "+" in "+"std_logic_vector("+str(N_PAN)+"-1 downto 0);"+"\n")
        f.write("\t\t\t"+"barreras_o"+ " : "+" out "+"std_logic_vector("+str(N_PAN)+"-1 downto 0);"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras_i"+ " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"barreras_o"+ " : "+" out "+"std_logic;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t"+"Cambios_i"+ " : "+" in "+"std_logic_vector("+str(N_MDC)+"-1 downto 0)"+";\n")  
        f.write("\t\t\t"+"Cambios_o"+ " : "+" out "+"std_logic_vector("+str(N_MDC)+"-1 downto 0)"+";\n")
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios_i"+ " : "+" in "+"std_logic"+";\n")  
        f.write("\t\t\t"+"Cambios_o"+ " : "+" out "+"std_logic"+";\n")
    
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+red+";\r\n")
    
    # componente mediador
    mediador = "mediador"
    f.write("\t"+"component "+mediador+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+";\n")
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    
    f.write("\t\t\t"+"semaforos"+ " : "+" in "+"sems_type;"+"\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras"+ " : "+" in "+"std_logic_vector("+str(N_PAN)+"-1 downto 0);"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras"+ " : "+" in "+"std_logic;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" in "+"std_logic_vector("+str(N_MDC)+"-1 downto 0);"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Salida"+    " : "+" out "+"std_logic_vector("+str(M)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+mediador+";\r\n")
      
    f.write("\tSignal cv_s : std_logic_vector(N_CVS-1 downto 0);\n")    
    f.write("\tSignal sem_s_i,sem_s_o : sems_type;\n")
    if N_PAN > 1:
        f.write("\tSignal pan_s_i,pan_s_o : std_logic_vector(N_PAN-1 downto 0);\n")
    if N_PAN == 1:
        f.write("\tSignal pan_s_i,pan_s_o : std_logic;\n")
        
    if N_MDC > 1:
        f.write("\tSignal mdc_s_i,mdc_s_o : std_logic_vector(N_MDC-1 downto 0);\n")
    if N_MDC == 1:
        f.write("\tSignal mdc_s_i,mdc_s_o : std_logic;\n")
    
    f.write("\nbegin\r\n")  
       
    instanciar_separador(f,separador,objetos)
    
    instanciar_mediador(f,mediador,objetos)
    
    instanciar_red(f,"red",objetos)
    
    f.write("end Behavioral;\r\n") 
    
    f.close()  # Close header file    
    
    print("Wrapper > Finalizado")

#%%    
def creando_separador(secciones,objetos):        
    
    print("Separador > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    NODO = "separador"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,True) # Incluir librerias
        
    # componente separador
    separador = "separador"
    f.write("\t"+"entity "+separador+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")   
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    
    f.write("\t\t\t"+"Paquete"+    " : "+" in "+"std_logic_vector(N-1 downto 0);"+"\n")
    f.write("\t\t\t"+"paquete_ok"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Ocupacion"+    " : "+" out "+"std_logic_vector(N_CVS-1 downto 0);"+"\n")
    f.write("\t\t\t"+"semaforos"+ " : "+" out "+"sems_type;"+"\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras"+ " : "+" out "+"std_logic_vector(N_PAN-1 downto 0);"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras"+ " : "+" out "+"std_logic;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" out "+"std_logic_vector(N_MDC-1 downto 0)"+";\n")  
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" out "+"std_logic"+";\n")  
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+separador+";\r\n")
   
    f.write("architecture Behavioral of "+separador+" is\r\n") 
        
    f.write("\tSignal cv_s : std_logic_vector(N_CVS-1 downto 0);\n")    
    f.write("\tSignal sem_s_i,sem_s_o : sems_type;\n")
    if N_PAN > 1:
        f.write("\tSignal pan_s_i,pan_s_o : std_logic_vector(N_PAN-1 downto 0);\n")
    if N_PAN == 1:
        f.write("\tSignal pan_s_i,pan_s_o : std_logic;\n")    
    if N_MDC > 1:
        f.write("\tSignal mdc_s_i,mdc_s_o : std_logic_vector(N_MDC-1 downto 0);\n")
    if N_MDC == 1:
        f.write("\tSignal mdc_s_i,mdc_s_o : std_logic;\n")
    f.write("begin\r\n")  
    
    # Ocupacion | semaforos | Pan | Camcio  
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'Event) then\n")
    f.write("\t\t\t"+"if (Reset = '1') then\n")
    f.write("\t\t\t\t"+"Ocupacion <= \""+str("0"*N_CVS)+"\";"+"\n")
    f.write("\t\t\t\t"+"semaforos.lsb <= \""+str("0"*N_SEM)+"\";"+"\n")
    f.write("\t\t\t\t"+"semaforos.msb <= \""+str("0"*N_SEM)+"\";"+"\n") 
    if N_PAN > 1:
        f.write("\t\t\t\t"+"barreras <= \""+str("0"*N_PAN)+"\";"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t\t"+"barreras <= '0'"+";\n")    
    if N_MDC > 1:
        f.write("\t\t\t\t"+"Cambios <= \""+str("0"*N_MDC)+"\";"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t\t"+"Cambios <= '0'"+";\n")
    f.write("\t\t\t"+"else\n")
    f.write("\t\t\t\t"+"if paquete_ok = '1' then\n")
    f.write("\t\t\t\t\t"+"Ocupacion <= Paquete("+str(N_CVS)+"-1 downto 0);"+"\n")
    
    for i in range(2*N_SEM):
        if i%2:
            #print ("LSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"semaforos.lsb("+str(int((i+1)/2-1))+") <= Paquete("+str(N_CVS+i)+");"+"\n")
        else:
            #print ("MSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"semaforos.msb("+str(int(i/2))+") <= Paquete("+str(N_CVS+i)+");"+"\n")
   
    if N_PAN > 1:
        f.write("\t\t\t\t\t"+"barreras <= Paquete("+str(N_CVS+2*N_SEM+N_PAN)+"-1 downto "+str(N_CVS+2*N_SEM)+");"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t\t\t"+"barreras <= Paquete("+str(N_CVS+2*N_SEM+N_PAN)+"-1);"+"\n")
          
    if N_MDC > 1:
        f.write("\t\t\t\t\t"+"Cambios <= Paquete("+str(N_CVS+2*N_SEM+N_PAN+N_MDC)+"-1 downto "+str(N_CVS+2*N_SEM+N_PAN)+");"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t\t\t"+"Cambios <= Paquete("+str(N_CVS+2*N_SEM+N_PAN+N_MDC)+"-1);"+"\n")
    
    f.write("\t\t\t\t"+"end if;\n")    
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\r\n")    
    
    f.write("end Behavioral;\r\n") 
    
    f.close()  # Close header file    
    
    print("Separador > Finalizado")
    
#%%    
def creando_mediador(secciones,objetos):        
    
    print("Mediador > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "mediador"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,True) # Incluir librerias
        
    # componente mediador
    mediador = "mediador"
    f.write("\t"+"entity "+mediador+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
    
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")    
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic"+";\n")
    
    f.write("\t\t\t"+"semaforos"+ " : "+" in "+"sems_type"+";\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras"+ " : "+" in "+"std_logic_vector("+str(N_PAN)+"-1 downto 0)"+";\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras"+ " : "+" in "+"std_logic"+";\n")
    if N_MDC > 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" in "+"std_logic_vector("+str(N_MDC)+"-1 downto 0)"+";\n")
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios"+ " : "+" in "+"std_logic"+";\n") 
    
    f.write("\t\t\t"+"Salida"+    " : "+" out "+"std_logic_vector("+str(M)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+mediador+";\r\n") 
   
    f.write("architecture Behavioral of "+mediador+" is\r\n")      
    
    f.write("begin\r\n")  
    
#    # Ocupacion | semaforos | Pan | Camcio  
#    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'Event) then\n")
    f.write("\t\t\t"+"if (Reset = '1') then\n")
    f.write("\t\t\t\t"+"Salida <= \""+str("0"*M)+"\";"+"\n")    
    f.write("\t\t\t"+"else\n")
    #f.write("\t\t\t\t"+"Salida <= Paquete("+str(N_CVS)+"-1 downto 0);"+"\n")
    
    #f.write("\t\t\t\t"+"Salida <= \""+str("1"*M)+"\";"+"\n")
    
    for i in range(2*N_SEM):
        if i%2:
            #print ("MSB: {}".format(i+1))
            f.write("\t\t\t\t"+"Salida("+str(i)+") <= semaforos.msb("+str(int((i+1)/2-1))+");"+"\n")
        else:
            #print ("LSB: {}".format(i+1))
            f.write("\t\t\t\t"+"Salida("+str(i)+") <= semaforos.lsb("+str(int((i+1)/2))+");"+"\n")
    
    if N_PAN > 0:    
        f.write("\t\t\t\t"+"Salida ("+str(2*N_SEM+N_PAN)+"-1 downto "+str(2*N_SEM)+") <= barreras;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t\t"+"Salida ("+str(2*N_SEM+N_PAN+N_MDC)+"-1 downto "+str(2*N_SEM+N_PAN)+") <= Cambios;"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t\t"+"Salida ("+str(2*N_SEM+N_PAN)+") <= Cambios;"+"\n")    
    
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\r\n")   
         
    f.write("end Behavioral;\r\n") 
    
    f.close()  # Close header file    
    
    print("Mediador > Finalizado")
#%%   
def instanciar_separador(f,nombre,objetos):   
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    # instanciar separador
    f.write("\t"+nombre+"_i:"+nombre+" port map(\n")
    
    f.write("\t\t"+"Clock"+" => "+"Clock"+",\n")
    
    f.write("\t\t"+"Paquete"+" => "+"Paquete_i"+",\n")
    f.write("\t\t"+"paquete_ok"+" => "+"paquete_ok"+",\n")
    f.write("\t\t"+"Ocupacion => cv_s,\n")
    f.write("\t\t"+"semaforos => sem_s_i,\n")
    if N_PAN > 0:
        f.write("\t\t"+"barreras => pan_s_i,\n")
    if N_MDC > 0:    
        f.write("\t\t"+"Cambios => mdc_s_i,\n")
    f.write("\t\t"+"Reset"+" => "+"Reset"+"\n")    
    f.write("\t\t);\r\n")
        
#%%   
def instanciar_mediador(f,nombre,objetos):   
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    # instanciar mediador
    f.write("\t"+nombre+"_i:"+nombre+" port map(\n")
    
    f.write("\t\t"+"Clock"+" => "+"Clock"+",\n")
    
    
    f.write("\t\t"+"semaforos => sem_s_o,\n")
    if N_PAN > 0:
        f.write("\t\t"+"barreras => pan_s_o,\n")
    if N_MDC > 0:     
        f.write("\t\t"+"Cambios => mdc_s_o,\n")
            
    f.write("\t\t"+"Salida => Paquete_o,\n")
    f.write("\t\t"+"Reset"+" => "+"Reset"+"\n")    
    f.write("\t\t);\r\n")

#%%   
def instanciar_red(f,nombre,objetos):   
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    # instanciar red
    f.write("\t"+nombre+"_i:"+nombre+" port map(\n")
    
    f.write("\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t"+"Ocupacion => cv_s,\n")
    f.write("\t\t"+"semaforos_i => sem_s_i,\n")
    f.write("\t\t"+"semaforos_o => sem_s_o,\n")
    if N_PAN > 0:
        f.write("\t\t"+"barreras_i => pan_s_i,\n")
        f.write("\t\t"+"barreras_o => pan_s_o,\n")
    if N_MDC > 0:    
        f.write("\t\t"+"Cambios_i => mdc_s_i,\n")
        f.write("\t\t"+"Cambios_o => mdc_s_o,\n") 
    f.write("\t\t"+"Reset"+" => "+"Reset"+"\n")
    
    f.write("\t\t);\r\n")
        
 #%%    
def creando_red(secciones,objetos,tabla,test = False):        
    
    print("Redes > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "red"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,True) # Incluir librerias
        
    red = "red"
    f.write("\t"+"entity "+red+" is\n")
    f.write("\t\t"+"generic(\n")
    f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
    
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"Ocupacion"+    " : "+" in "+"std_logic_vector(N_CVS-1 downto 0)"+";\n")
    f.write("\t\t\t"+"semaforos_i"+ " : "+" in "+"sems_type"+";\n")
    f.write("\t\t\t"+"semaforos_o"+ " : "+" out "+"sems_type"+";\n")
    if N_PAN > 1:
        f.write("\t\t\t"+"barreras_i"+ " : "+" in "+"std_logic_vector(N_MDC-1 downto 0)"+";\n")
        f.write("\t\t\t"+"barreras_o"+ " : "+" out "+"std_logic_vector(N_PAN-1 downto 0)"+";\n")
    if N_PAN == 1:
        f.write("\t\t\t"+"barreras_i"+ " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"barreras_o"+ " : "+" out "+"std_logic"+";\n")   
    if N_MDC > 1:    
        f.write("\t\t\t"+"Cambios_i"+ " : "+" in "+"std_logic_vector(N_MDC-1 downto 0)"+";\n")  
        f.write("\t\t\t"+"Cambios_o"+ " : "+" out "+"std_logic_vector(N_MDC-1 downto 0)"+";\n")
    if N_MDC == 1:
        f.write("\t\t\t"+"Cambios_i"+ " : "+" in "+"std_logic"+";\n")  
        f.write("\t\t\t"+"Cambios_o"+ " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+red+";\n") 
    
    f.write("architecture Behavioral of "+red+" is\r\n") 

    sem_cant,sem_actual,sem_anterior = calcular_semaforos(secciones,objetos,tabla)
    
    #print("Cantidades : {}".format(sem_cant))
    #print("Actuales : {}".format(sem_actual))
    #print("Anteriores : {}".format(sem_anterior))
    
    # componente cambio 
    
    for i in range(N_MDC):
                    
        cambio = "cambio_"+str(i+1)
        f.write("\t"+"component "+cambio+" is\n")
        f.write("\t\t"+"generic(\n")
        f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")

        f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
        if N_PAN > 0:
            f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
        if N_MDC > 0:    
            f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
        f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
        f.write("\t\t"+");\n")
        f.write("\t\t"+"port("+"\n")
        f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
        
        f.write("\t\t\t"+"Estado_ante_i"+   " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"Estado_post_i"+   " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"Estado_desv_i"+   " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"Estado_ante_o"+   " : "+" out "+"std_logic"+";\n")
        f.write("\t\t\t"+"Estado_post_o"+   " : "+" out "+"std_logic"+";\n")
        f.write("\t\t\t"+"Estado_desv_o"+   " : "+" out "+"std_logic"+";\n")
        f.write("\t\t\t"+"Cambio_i"+    " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"Cambio_o"+    " : "+" out "+"std_logic"+";\n")
        f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
        f.write("\t\t"+");\n")
        f.write("\t"+"end component "+cambio+";\r\n")
        
    # componente nodos
     
    for i in range(N_CVS):
        #print ("Nodo : {} | {}".format(i+1,secciones[i].barrera))
            
        red = "nodo_"+str(i+1)
        f.write("\t"+"component "+red+" is\n")
        f.write("\t\t"+"generic(\n")
        f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")
        
        f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
        if N_PAN > 0:
            f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
        if N_MDC > 0:    
            f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
            f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
        f.write("\t\t"+");\n")
        f.write("\t\t"+"port("+"\n")
        f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_i"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].anterior != "" or secciones[i].desvio_inf_dir == "<" or secciones[i].desvio_sup_dir == "<" :
            f.write("\t\t\t"+"Estado_ante"+   " : "+" out "+"std_logic;"+"\n")
        if secciones[i].posterior != "" or secciones[i].desvio_inf_dir == ">" or secciones[i].desvio_sup_dir == ">":
            f.write("\t\t\t"+"Estado_post"+   " : "+" out "+"std_logic;"+"\n")
            
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t"+"Semaforo_propio_i_"+str(j+1)+   " : "+" in "+"sem_type;"+"\n")
                f.write("\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   " : "+" out "+"sem_type;"+"\n")
                
                
        # ACA, usar la lista! $$$$$       
        if str(i+1) in sem_actual:
            f.write("\t\t\t"+"Semaforo_cercano"+   " : "+" out "+"sem_type;"+"\n")
            #print ("TIENE : {}".format(i+1))
    
            
        #f.write("\t\t\t"+"Semaforo_lejano"+   " : "+" out "+"sem_type;"+"\n")
        #if secciones[i].cambio:
        #    f.write("\t\t\t"+"Cambio"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].barrera:
            f.write("\t\t\t"+"Barrera"+   " : "+" out "+"std_logic;"+"\n")
        #f.write("\t\t\t"+"entrada"+    " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_o"+    " : "+" out "+"std_logic"+"\n")
        f.write("\t\t"+");\n")
        f.write("\t"+"end component "+red+";\r\n")

    # Auxiliares
    for i in range(N_CVS):
        f.write("\tSignal conector_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal ocupacion_"+str(i+1)+" : std_logic;\n") 
        
        #if secciones[i].cambio:
        #    f.write("\tSignal desv_"+str(i+1)+" : std_logic;\n")
    
    for i in range(N_SEM):
        f.write("\tSignal sem_lsb_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal sem_msb_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal sem_lsb_o_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal sem_msb_o_"+str(i+1)+" : std_logic;\n")
        
    for i in range(N_PAN):
        f.write("\tSignal pan_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal pan_o_"+str(i+1)+" : std_logic;\n")
        
    for i in range(N_MDC):
        f.write("\tSignal mdc_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_o_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_ante_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_ante_o_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_post_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_post_o_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_desv_i_"+str(i+1)+" : std_logic;\n")
        f.write("\tSignal mdc_desv_o_"+str(i+1)+" : std_logic;\n")
     
    f.write("\tSignal cosa : std_logic;\n")
    
    # Begin    
    f.write("begin\r\n")  

    # instanciar nodos
    cambios = []
    cambios_conexion = []
    sem_index = 1
    
    # Detectar cambios
    for i in range(N_CVS):
        if secciones[i].cambio:
            cambios.append(i+1)
            cambios_conexion.append([0,0,0])
    if test:
        print ("Cambios : {}".format(cambios))
    
    for i in range(N_CVS):
        #print ("Nodos : {}".format(i+1))
        
        nombre = "nodo_"+str(i+1)
        f.write("\t"+nombre+"_i:"+nombre+" port map(\n")
        
        f.write("\t\t"+"Clock"+" => "+"Clock"+",\n")

        # Si soy un cambio
        #if secciones[i].cambio:
        vecinos = secciones[i].vecinos
        #print ("Nodo : {} de {}".format(i+1,vecinos))
        
        for j in range(len(vecinos)):
            #print ("{} es vecino de {}".format(i+1,vecinos[j]))
            
            # Si > :
            if (secciones[i].desvio_inf_dir == ">" or secciones[i].desvio_sup_dir == ">"):
                if vecinos[j] == secciones[i].posterior:
                    if test:
                        print ("[{}] > cambio_{}".format(i+1,cambios.index(i+1)+1))
                    cambios_conexion[cambios.index(i+1)][0] = i+1
                    #print ("({})".format(cambios_conexion[cambios.index(i+1)]))
                    f.write("\t\t"+"Estado_post => mdc_ante_o_"+str(cambios.index(i+1)+1)+",\n")
                    
                if secciones[i].desvio_sup != "":
                    desvio = secciones[i].desvio_sup
                if secciones[i].desvio_inf != "":
                    desvio = secciones[i].desvio_inf
                    
                if vecinos[j] == desvio and secciones[i].cambio_raiz == False:
                    if test:
                        print ("[{}] <d cambio_{}".format(cambios.index(desvio)+1,i+1))
                    cambios_conexion[cambios.index(desvio)][2] = i+1
                    #print ("({})".format(cambios_conexion[cambios.index(desvio)]))
                    f.write("\t\t"+"Estado_post => mdc_desv_o_"+str(cambios.index(desvio)+1)+",\n")
                        
            else:
                if secciones[i].posterior == vecinos[j]:
                    if secciones[vecinos[j]-1].cambio:
                        if (secciones[vecinos[j]-1].desvio_inf_dir == ">" or secciones[vecinos[j]-1].desvio_sup_dir == ">"):
                            posterior = "conector_"+str(vecinos[j])
                        if (secciones[vecinos[j]-1].desvio_inf_dir == "<" or secciones[vecinos[j]-1].desvio_sup_dir == "<"):
                            posterior = "mdc_ante_o_"+str(cambios.index(vecinos[j])+1)
                            cambios_conexion[cambios.index(vecinos[j])][1] = i+1
                            #print ("({})".format(cambios_conexion[cambios.index(vecinos[j])]))
                    else:
                        posterior = "conector_"+str(vecinos[j])
                    if test:
                        print ("[{}] > {}".format(i+1,posterior))   
                    f.write("\t\t"+"Estado_post => "+str(posterior)+",\n")
            
            # Si < :
            if (secciones[i].desvio_inf_dir == "<" or secciones[i].desvio_sup_dir == "<"):
                if vecinos[j] == secciones[i].anterior:
                    if test:
                        print ("[{}] < cambio_{}".format(i+1,cambios.index(i+1)+1))
                    f.write("\t\t"+"Estado_ante => mdc_post_o_"+str(cambios.index(i+1)+1)+",\n")
                    
                if secciones[i].desvio_sup != "":
                    desvio = secciones[i].desvio_sup
                if secciones[i].desvio_inf != "":
                    desvio = secciones[i].desvio_inf
                    
                if vecinos[j] == desvio and secciones[i].cambio_raiz == False:
                    if test:
                        print ("cambio_{} <d [{}]".format(cambios.index(desvio)+1,i+1))
                    cambios_conexion[cambios.index(desvio)][2] = i+1
                    #print ("({})".format(cambios_conexion[cambios.index(desvio)]))
                    f.write("\t\t"+"Estado_ante => mdc_desv_o_"+str(cambios.index(desvio)+1)+",\n")
            else:
                if secciones[i].anterior == vecinos[j]:
                    if secciones[vecinos[j]-1].cambio:
                        if (secciones[vecinos[j]-1].desvio_inf_dir == "<" or secciones[vecinos[j]-1].desvio_sup_dir == "<"):
                            anterior = "conector_"+str(vecinos[j])
                        if (secciones[vecinos[j]-1].desvio_inf_dir == ">" or secciones[vecinos[j]-1].desvio_sup_dir == ">"):
                            anterior = "mdc_post_o_"+str(cambios.index(vecinos[j])+1)    
                            cambios_conexion[cambios.index(vecinos[j])][1] = i+1
                            #print ("({})".format(cambios_conexion[cambios.index(vecinos[j])]))
                    else:
                        anterior = "conector_"+str(vecinos[j])
                        
                    if test:
                        print ("{} < [{}]".format(anterior,i+1))   
                    f.write("\t\t"+"Estado_ante => "+str(anterior)+",\n")
        
        #f.write("\tSignal sem_lsb_"+str(i+1)+" : std_logic;\n")
        #f.write("\tSignal sem_msb_"+str(i+1)+" : std_logic;\n")
        
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t"+"Semaforo_propio_i_"+str(j+1)+".lsb => sem_lsb_i_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_i_"+str(j+1)+".msb => sem_msb_i_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_o_"+str(j+1)+".lsb => sem_lsb_o_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_o_"+str(j+1)+".msb => sem_msb_o_"+str(sem_index)+","+"\n") 
                sem_index = sem_index + 1
                
        if str(i+1) in sem_actual:
            f.write("\t\t"+"Semaforo_cercano"+".lsb => "+"cosa"+",\n") 
            f.write("\t\t"+"Semaforo_cercano"+".msb => "+"cosa"+",\n") 
            
        f.write("\t\t"+"Estado_i => ocupacion_"+str(i+1)+",\n")
        f.write("\t\t"+"Estado_o => conector_"+str(i+1)+",\n")     
        f.write("\t\t"+"Reset"+" => "+"Reset"+"\n")    
        f.write("\t\t);\r\n")
    
    # instanciar cambios
    for i in range(N_MDC):
        #print ("Nodos : {} | {} o {}".format(i+1,secciones[i].desvio_inf,secciones[i].desvio_sup))
        # instanciar cambios
        
        nombre = "cambio_"+str(i+1)
        f.write("\t"+nombre+"_i:"+nombre+" port map(\n")
        
        f.write("\t\t"+"Clock"+" => "+"Clock"+",\n")
            
        f.write("\t\t"+"Cambio_i => mdc_i_"+str(i+1)+",\n")
        f.write("\t\t"+"Cambio_o => mdc_o_"+str(i+1)+",\n")
          
        f.write("\t\t"+"Estado_ante_i => conector_"+str(cambios_conexion[i][0])+",\n")
        f.write("\t\t"+"Estado_ante_o => mdc_ante_o_"+str(i+1)+",\n")
        f.write("\t\t"+"Estado_post_i => conector_"+str(cambios_conexion[i][1])+",\n")
        f.write("\t\t"+"Estado_post_o => mdc_post_o_"+str(i+1)+",\n")
        f.write("\t\t"+"Estado_desv_i => conector_"+str(cambios_conexion[i][2])+",\n")
        f.write("\t\t"+"Estado_desv_o => mdc_desv_o_"+str(i+1)+",\n")
        
        f.write("\t\t"+"Reset"+" => "+"Reset"+"\n")    
        f.write("\t\t);\r\n")   
            
    if N_PAN > 0:
        f.write("\t\t"+"barreras_o <= barreras_i;\n")
   
    f.write("\t\t"+"cosa <= '0';\n")
    
    for i in range(N_CVS):
        f.write("\t\t"+"ocupacion_"+str(i+1)+" <= Ocupacion("+str(i)+");\n")
    
    if N_MDC > 1:
        for i in range(N_MDC):
            f.write("\t\t"+"mdc_i_"+str(i+1)+" <= Cambios_i("+str(i)+");\n")        
            f.write("\t\t"+"Cambios_o("+str(i)+") <= mdc_o_"+str(i+1)+";\n")
    
        if N_MDC == 1:
            f.write("\t\t"+"mdc_i_"+str(i+1)+" <= Cambios_i;\n")        
            f.write("\t\t"+"Cambios_o <= mdc_o_"+str(i+1)+";\n")
            
    if N_PAN > 0: 
        for i in range(N_PAN):
            f.write("\t\t"+"pan_i_"+str(i+1)+" <= Barreras_i("+str(i)+");\n")        
            f.write("\t\t"+"Barreras_o("+str(i)+") <= pan_o_"+str(i+1)+";\n")
     
    for i in range(N_SEM):

        # ACA, usar la lista! $$$$$
        
        f.write("\t\t"+"sem_lsb_i_"+str(i+1)+" <= semaforos_i.lsb("+str(i)+");"+"\n") 
        f.write("\t\t"+"sem_msb_i_"+str(i+1)+" <= semaforos_i.msb("+str(i)+");"+"\n") 
        
        f.write("\t\t"+"semaforos_o.lsb("+str(i)+") <= sem_lsb_o_"+str(i+1)+";"+"\n") 
        f.write("\t\t"+"semaforos_o.msb("+str(i)+") <= sem_msb_o_"+str(i+1)+";"+"\n")
    
    f.write("end Behavioral;\r\n") 
    
    f.close()  # Close header file    
    
    print("Redes > Finalizado")

#%%    
def creando_nodo(secciones,objetos):        
    
    print("Nodo > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    for i in range(N_CVS):
        nodo = "nodo_"+str(i+1)
        f = open("VHDL/"+nodo+".vhd", "w")

        # Comentario inicial
        f.write("-- " + nodo + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
        incluir_librerias(f,True) # Incluir librerias
           
        # componente nodo
        
        f.write("\t"+"entity "+nodo+" is\n")
        f.write("\t\t"+"generic(\n")
        f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")     
        f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
        if N_PAN > 0:
            f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
        if N_MDC > 0:
            f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
        f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
        f.write("\t\t"+");\n")
        f.write("\t\t"+"port("+"\n")
        f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_i"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].anterior != "" or secciones[i].desvio_inf_dir == "<" or secciones[i].desvio_sup_dir == "<" :
            f.write("\t\t\t"+"Estado_ante"+   " : "+" out "+"std_logic;"+"\n")
        if secciones[i].posterior != "" or secciones[i].desvio_inf_dir == ">" or secciones[i].desvio_sup_dir == ">":
            f.write("\t\t\t"+"Estado_post"+   " : "+" out "+"std_logic;"+"\n")
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t"+"Semaforo_propio_i_"+str(j+1)+   " : "+" in "+"sem_type;"+"\n")
                f.write("\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   " : "+" out "+"sem_type;"+"\n")
        f.write("\t\t\t"+"Semaforo_cercano"+   " : "+" out "+"sem_type;"+"\n")
        f.write("\t\t\t"+"Semaforo_lejano"+   " : "+" out "+"sem_type;"+"\n")
        #if secciones[i].cambio:
        #    f.write("\t\t\t"+"Cambio"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].barrera:
            f.write("\t\t\t"+"Barrera"+   " : "+" out "+"std_logic;"+"\n")
        #f.write("\t\t\t"+"entrada"+    " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_o"+    " : "+" out "+"std_logic"+"\n")
        f.write("\t\t"+");\n")
        f.write("\t"+"end entity "+nodo+";\r\n") 
   
        f.write("architecture Behavioral of "+nodo+" is\r\n") 
           
        f.write("begin\r\n")  
        
        f.write("\t"+"process(Clock,Reset)\n")
        f.write("\t"+"begin\n")
        f.write("\t\t"+"if (Clock = '1' and Clock'Event) then\n")
        f.write("\t\t\t"+"if (Reset = '1') then\n")
        f.write("\t\t\t\t"+"Estado_o <= '0';"+"\n") 
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   ".msb <= '0';"+"\n")
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   ".lsb <= '0';"+"\n")
        f.write("\t\t\t"+"else\n")    
        f.write("\t\t\t\t"+"Estado_o <= Estado_i;"+"\n") 
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".msb <= Semaforo_propio_i_"+str(j+1)+".msb;"+"\n")
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".lsb <= Semaforo_propio_i_"+str(j+1)+".lsb;"+"\n")          
        f.write("\t\t\t"+"end if;\n")
        f.write("\t\t"+"end if;\n")
        f.write("\t"+"end process;\r\n")   
         
        f.write("end Behavioral;\r\n") 
        
        f.close()  # Close header file    
    
    print("Nodo > Finalizado")
#%%   
def creando_cambio(secciones,objetos):   
    
    print("Nodo > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    for i in range(N_MDC):
        cambio = "cambio_"+str(i+1)
        f = open("VHDL/"+cambio+".vhd", "w")

        # Comentario inicial
        f.write("-- " + cambio + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
        incluir_librerias(f,True) # Incluir librerias
           
        # componente cambio
        
        f.write("\t"+"entity "+cambio+" is\n")
        f.write("\t\t"+"generic(\n")
        f.write("\t\t\t"+"N"+" : "+"natural"+" := "+str(N)+";\n")    
        f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
        if N_PAN > 0:
            f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
        if N_MDC > 0:    
            f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
        f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")
        f.write("\t\t"+");\n")
        f.write("\t\t"+"port("+"\n")
        f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_ante_i"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_post_i"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_desv_i"+   " : "+" in "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_ante_o"+   " : "+" out "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_post_o"+   " : "+" out "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Estado_desv_o"+   " : "+" out "+"std_logic;"+"\n")
        f.write("\t\t\t"+"Cambio_i"+    " : "+" in "+"std_logic"+";\n")
        f.write("\t\t\t"+"Cambio_o"+    " : "+" out "+"std_logic"+"\n")
        f.write("\t\t"+");\n")
        f.write("\t"+"end entity "+cambio+";\r\n") 
   
        f.write("architecture Behavioral of "+cambio+" is\r\n") 
         
        
        f.write("begin\r\n")  
        
        f.write("\t"+"process(Clock,Reset)\n")
        f.write("\t"+"begin\n")
        f.write("\t\t"+"if (Clock = '1' and Clock'Event) then\n")
        f.write("\t\t\t"+"if (Reset = '1') then\n")
        f.write("\t\t\t\t"+"Estado_ante_o <= '0';"+"\n")    
        f.write("\t\t\t\t"+"Estado_post_o <= '0';"+"\n") 
        f.write("\t\t\t\t"+"Estado_desv_o <= '0';"+"\n") 
        f.write("\t\t\t\t"+"Cambio_o <= '0';"+"\n") 
        f.write("\t\t\t"+"else\n")
        f.write("\t\t\t\t"+"Cambio_o <= Cambio_i;"+"\n") 
        f.write("\t\t\t\t"+"if (Cambio_i = '0') then\n")
        
        f.write("\t\t\t\t\t"+"Estado_ante_o <= Estado_post_i;"+"\n")    
        f.write("\t\t\t\t\t"+"Estado_post_o <= Estado_ante_i;"+"\n") 
        f.write("\t\t\t\t\t"+"Estado_desv_o <= '0';"+"\n") 
        
        f.write("\t\t\t"+"else\n")
        
        f.write("\t\t\t\t\t"+"Estado_ante_o <= Estado_desv_i;"+"\n")    
        f.write("\t\t\t\t\t"+"Estado_post_o <= '0';"+"\n") 
        f.write("\t\t\t\t\t"+"Estado_desv_o <= Estado_ante_i;"+"\n") 
        
        f.write("\t\t\t\t"+"end if;\n")
        f.write("\t\t\t"+"end if;\n")
        f.write("\t\t"+"end if;\n")
        f.write("\t"+"end process;\r\n")   
         
        f.write("end Behavioral;\r\n") 
        
        f.close()  # Close header file    
    
    print("Nodo > Finalizado")
    
#%%
def calcular_semaforos(secciones,objetos,tabla):
   
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    sem_actu = 0
    sem_ante = 1
    sem_post = 2
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    print("Semaforeo > Iniciando")
    
    sem_index = -1;
    sem_lista = [];
    sem_actual = [];
    sem_anterior = [];
    sem_cant = [0]*N_SEM;

    semaforeo = np.zeros((3,N_SEM))
    
    for i in range(N_SEM):
        semaforeo[sem_actu][i] = i+1
        semaforeo[sem_ante][i] = -1
        semaforeo[sem_post][i] = -1
        
    #print("{}".format(semaforeo)) 
    print("{}".format(tabla['Secuencia'])) 
    
    for i in range(len(tabla['Secuencia'])):
        
        # Semaforos finales
        semaforo = tabla['Secuencia'][i].split('-')[-1]
        sem_actual.append(semaforo)
        
        if semaforo not in sem_lista and secciones[int(semaforo)-1].tipo == "Extremo":
            sem_lista.append(semaforo)        
            sem_index = sem_index + 1
            #print("i:{}".format(sem_index))
            sem_cant[sem_index] = 1                 
            
            
        # Semaforos inicial
        semaforo = tabla['Secuencia'][i].split('-')[0]
        sem_anterior.append(semaforo)
            
        if semaforo not in sem_lista:
            sem_lista.append(semaforo)
            sem_index = sem_index + 1
            #print("j:{} / {}".format(sem_index,len(sem_cant)))
            sem_cant[sem_index] = 1     
            
            #print("({})".format(sem_cant))
        else:   
            #print("{} in {}|{}".format(semaforo,sem_lista,sem_cant))
            sem_cant[sem_lista.index(semaforo)] = sem_cant[sem_lista.index(semaforo)] + 1
            
    while 0 in sem_cant:
      sem_cant.remove(0)   
      
        #print("Semaforo: {} Anterior: {}".format(tabla['Secuencia'][i][-1],tabla['Secuencia'][i][0])) 
    print("{}".format(sem_lista))
    print("#{}".format(sem_cant))
    print("fin:{}".format(sem_actual))
    print("ini:{}".format(sem_anterior))
    
    print("Semaforeo > Finalizado")     
    
    return sem_cant,sem_actual,sem_anterior
    