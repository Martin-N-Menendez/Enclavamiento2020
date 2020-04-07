import numpy as np
import math

from Plotear import *


def crear_modulo_vhdl(secciones,tabla):

    print("%"*25+" Iniciando creacion de modulos "+"%"*25)    
    
    #mostrar_grafo(Mapa.secciones,10,True)
    
    objetos = calcular_paquete(secciones,True)
    
    creando_paquete(secciones,objetos,False)
    
    creando_global(secciones,objetos,False)
    
    creando_uart_control(secciones,objetos,False) 
    
    creando_uart(secciones,objetos,False)
    
    creando_uart_baud_gen(secciones,objetos,False)
    
    creando_uart_tx(secciones,objetos,False)
    
    creando_uart_rx(secciones,objetos,False)
    
    creando_fifo(secciones,objetos,False)
    
    creando_sistema(secciones,objetos,False)
    
    creando_detector(secciones,objetos,False)
    
    creando_enclavamiento(secciones,objetos,False)
    
    creando_separador(secciones,objetos,False)
    
    creando_mediador(secciones,objetos,False)
    
    creando_red(secciones,objetos,tabla,False)
    
    creando_nodo(secciones,objetos,tabla,False)
    
    creando_cambio(secciones,objetos,False)
    
    creando_registro(secciones,objetos,False)
    
    creando_selector(secciones,objetos,False)
    
    print("%"*25+" Finalizando creacion de modulos "+"%"*25) 

#%%
def calcular_paquete(secciones,test = False):
    
    N = 0
    M = 0
    n_vias = 0
    n_semaforos = 0
    n_pans = 0
    n_cambios = 0
 
    if test:
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
            
    N = n_vias + 2*n_semaforos + n_pans + n_cambios
    M = 2*n_semaforos + n_pans + n_cambios
    
    if test:
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
def creando_paquete(secciones,objetos,test = False):        
    
    if test:
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
    
    if test:
        print("Paquete > Finalizado")
#%%    
def creando_enclavamiento(secciones,objetos,test = False):        
    
    if test:
        print("Enclavamiento > Creando") 
    
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic;"+"\n")
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic;"+"\n")
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic;"+"\n")
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
    
    f.write("\t\t\t"+"N_SEM"+" : "+"natural"+" := "+str(N_SEM)+";\n")
    if N_PAN > 0:
        f.write("\t\t\t"+"N_PAN"+" : "+"natural"+" := "+str(N_PAN)+";\n")
    if N_MDC > 0:    
        f.write("\t\t\t"+"N_MDC"+" : "+"natural"+" := "+str(N_MDC)+";\n")
    f.write("\t\t\t"+"N_CVS"+" : "+"natural"+" := "+str(N_CVS)+"\n")    
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic;"+"\n")
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
    f.write("\tSignal procesar_sep_enc, procesar_enc_med : std_logic;\n")
    
    f.write("\nbegin\r\n")  
       
    instanciar_separador(f,separador,objetos)
    
    instanciar_mediador(f,mediador,objetos)
    
    instanciar_red(f,"red",objetos)
    
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Enclavamiento > Finalizado")

#%%    
def creando_separador(secciones,objetos,test = False):        
    
    if test:
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic;"+"\n")
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
    f.write("\t\t\t\t"+"procesado <= '0';"+"\n")    
    f.write("\t\t\t"+"else\n")
    f.write("\t\t\t\t"+"procesado <= procesar;"+"\n") 
    f.write("\t\t\t\t"+"if procesar = '1' then\n")
    
    for i in range(N_CVS):
        f.write("\t\t\t\t\t"+"Ocupacion("+str(i)+") <= Paquete("+str(N-i-1)+");"+"\n")
    
    for i in range(2*N_SEM):
        if i%2:
            #print ("LSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"semaforos.lsb("+str(int((i+1)/2-1))+") <= Paquete("+str(N-1-N_CVS-i)+");"+"\n")
        else:
            #print ("MSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"semaforos.msb("+str(int(i/2))+") <= Paquete("+str(N-1-N_CVS-i)+");"+"\n")
   
    if N_PAN > 1:
        f.write("\t\t\t\t\t"+"barreras <= Paquete("+str(N_CVS+2*N_SEM+N_PAN)+"-1 downto "+str(N_CVS+2*N_SEM)+");"+"\n")
    if N_PAN == 1:
        f.write("\t\t\t\t\t"+"barreras <= Paquete("+str(N_CVS+2*N_SEM+N_PAN)+"-1);"+"\n")
          
    if N_MDC > 1:
        f.write("\t\t\t\t\t"+"Cambios <= Paquete("+str(N-(N_CVS+2*N_SEM+N_PAN+N_MDC))+" downto "+str(N-(N_CVS+2*N_SEM+N_PAN))+");"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t\t\t"+"Cambios <= Paquete("+str(N-(N_CVS+2*N_SEM+N_PAN+N_MDC))+");"+"\n")
    
    f.write("\t\t\t\t"+"end if;\n")    
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\r\n")    
    
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Separador > Finalizado")
    
#%%    
def creando_mediador(secciones,objetos,test = False):        
    
    if test:
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic"+";\n")
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
    f.write("\t\t\t\t"+"Salida <= (others => '0');"+"\n")  
    f.write("\t\t\t\t"+"procesado <= '0';"+"\n")   
    f.write("\t\t\t"+"else\n")
    #f.write("\t\t\t\t"+"Salida <= Paquete("+str(N_CVS)+"-1 downto 0);"+"\n")
    
    #f.write("\t\t\t\t"+"Salida <= \""+str("1"*M)+"\";"+"\n")
    
    f.write("\t\t\t\t"+"procesado <= procesar;"+"\n")
    f.write("\t\t\t\t"+"if (procesar = '1') then\n")
    for i in range(2*N_SEM):
        if i%2:
            #print ("MSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"Salida("+str(i)+") <= semaforos.lsb("+str(int((i+1)/2-1))+");"+"\n")
        else:
            #print ("LSB: {}".format(i+1))
            f.write("\t\t\t\t\t"+"Salida("+str(i)+") <= semaforos.msb("+str(int((i+1)/2))+");"+"\n")
    
    if N_PAN > 0:    
        f.write("\t\t\t\t\t"+"Salida("+str(2*N_SEM+N_PAN)+"-1 downto "+str(2*N_SEM)+") <= barreras;"+"\n")
    if N_MDC > 1:
        f.write("\t\t\t\t\t"+"Salida("+str(2*N_SEM+N_PAN+N_MDC)+"-1 downto "+str(2*N_SEM+N_PAN)+") <= Cambios;"+"\n")
    if N_MDC == 1:
        f.write("\t\t\t\t\t"+"Salida("+str(2*N_SEM+N_PAN)+") <= Cambios;"+"\n")    
    
    f.write("\t\t\t\t"+"end if;\n")
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\r\n")   
         
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
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
    f.write("\t\t"+"procesar"+" => "+"procesar"+",\n")
    f.write("\t\t"+"procesado"+" => "+"procesar_sep_enc"+",\n")
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
    f.write("\t\t"+"procesar"+" => "+"procesar_enc_med"+",\n")
    f.write("\t\t"+"procesado"+" => "+"procesado"+",\n")
    
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
    f.write("\t\t"+"procesar"+" => "+"procesar_sep_enc"+",\n")
    f.write("\t\t"+"procesado"+" => "+"procesar_enc_med"+",\n")
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
    
    if test:
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
    f.write("\t\t\t"+"procesar"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"procesado"+   " : "+" out "+"std_logic"+";\n")
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

    sem_cant,sem_actual,sem_anterior,sem_cambio = calcular_semaforos(secciones,objetos,tabla)
    
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
        if secciones[i].tipo == "Cruce" or secciones[i].tipo == "Desvio":
            f.write("\t\t\t"+"Cambio_i"+   " : "+" in "+"std_logic;"+"\n") 
        f.write("\t\t\t"+"Estado_i"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].anterior != "" or secciones[i].desvio_inf_dir == "<" or secciones[i].desvio_sup_dir == "<" :
            f.write("\t\t\t"+"Estado_ante"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].posterior != "" or secciones[i].desvio_inf_dir == ">" or secciones[i].desvio_sup_dir == ">":
            f.write("\t\t\t"+"Estado_post"+   " : "+" in "+"std_logic;"+"\n")
            
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t"+"Semaforo_propio_i_"+str(j+1)+   " : "+" in "+"sem_type;"+"\n")
                f.write("\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   " : "+" out "+"sem_type;"+"\n")
        
        for k in range(len(sem_anterior)):
                #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
                if str(i+1) == sem_anterior[k]:
                    f.write("\t\t\t"+"Semaforo_cercano_"+str(sem_actual[k])+"_i"+" : "+" in "+"sem_type"+";\n")        
                    
        for j in range(len(sem_anterior)):
                #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
                if str(i+1) == sem_anterior[j]:
                    if int(sem_actual[j]) not in secciones[i].vecinos:
                        f.write("\t\t\t"+"Estado_lejano_"+str(sem_actual[j])+"_i"+" : "+" in "+"std_logic;"+"\n")            
                        
            
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
                if vecinos[j] == secciones[i].posterior :
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
                    cambios_conexion[cambios.index(i+1)][0] = i+1    
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
   
    
    #for i in range(N_CVS):
        
        #print ( cambios_conexion )
        
        for j in range(N_MDC):
            if i+1 == cambios_conexion[j][0] or i+1 == cambios_conexion[j][2]:
                mdc_index = j+1
                if test:
                    print("{} tiene el cambio_{}".format(i+1,mdc_index))
                f.write("\t\t"+"Cambio_i"+   " => "+" mdc_i_"+str(mdc_index)+","+"\n")              
        
        
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t"+"Semaforo_propio_i_"+str(j+1)+".lsb => sem_lsb_i_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_i_"+str(j+1)+".msb => sem_msb_i_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_o_"+str(j+1)+".lsb => sem_lsb_o_"+str(sem_index)+","+"\n") 
                f.write("\t\t"+"Semaforo_propio_o_"+str(j+1)+".msb => sem_msb_o_"+str(sem_index)+","+"\n") 
                sem_index = sem_index + 1
                
     
        
        for k in range(len(sem_anterior)):
            #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
            if str(i+1) == sem_anterior[k]:
                f.write("\t\t"+"Semaforo_cercano_"+str(sem_actual[k])+"_i.lsb => "+"sem_lsb_o_"+str(sem_actual[k])+","+"\n")    
                f.write("\t\t"+"Semaforo_cercano_"+str(sem_actual[k])+"_i.msb => "+"sem_msb_o_"+str(sem_actual[k])+","+"\n")   
                
                
        for k in range(len(sem_anterior)):
            #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
            if str(i+1) == sem_anterior[k]:
                if int(sem_actual[k]) not in secciones[i].vecinos:
                    f.write("\t\t"+"Estado_lejano_"+str(sem_actual[k])+"_i"+" => "+" conector_"+str(sem_actual[k])+",\n")        
            
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
        
        if test:
            print ("Nodos : {} | {} o {} | {}".format(i+1,secciones[i].desvio_inf,secciones[i].desvio_sup,cambios_conexion))
        
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
        f.write("\t\t"+"mdc_i_1 <= Cambios_i;\n")        
        f.write("\t\t"+"Cambios_o <= mdc_o_1;\n")
            
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
    
    
    
    
    
    f.write("\t\t"+"procesado <= procesar;\n")
    
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Redes > Finalizado")

#%%    
def creando_nodo(secciones,objetos,tabla,test = False):        
    
    if test:
        print("Nodo > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    sem_cant,sem_actual,sem_anterior,sem_cambio = calcular_semaforos(secciones,objetos,tabla)
    
    if test:
        print("Cantidades : {}".format(sem_cant))
        print("Actuales : {}".format(sem_actual))
        print("Anteriores : {}".format(sem_anterior))
    
    #for j in range(len(sem_anterior)): 
        #print("a {} le importa {}".format(sem_anterior[j],sem_actual[j]))
    
    print("Actuales : {}".format(sem_actual))
    print("Anteriores : {}".format(sem_anterior))
        
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
        if secciones[i].tipo == "Cruce" or secciones[i].tipo == "Desvio":
            f.write("\t\t\t"+"Cambio_i"+   " : "+" in "+"std_logic;"+"\n")    
        f.write("\t\t\t"+"Estado_i"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].anterior != "" or secciones[i].desvio_inf_dir == "<" or secciones[i].desvio_sup_dir == "<" :
            f.write("\t\t\t"+"Estado_ante"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].posterior != "" or secciones[i].desvio_inf_dir == ">" or secciones[i].desvio_sup_dir == ">":
            f.write("\t\t\t"+"Estado_post"+   " : "+" in "+"std_logic;"+"\n")
        if secciones[i].semaforo:
            for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t"+"Semaforo_propio_i_"+str(j+1)+   " : "+" in "+"sem_type;"+"\n")
                f.write("\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   " : "+" out "+"sem_type;"+"\n")
                
                
        for j in range(len(sem_anterior)):
                #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
                if str(i+1) == sem_anterior[j]:
                    f.write("\t\t\t"+"Semaforo_cercano_"+str(sem_actual[j])+"_i"+" : "+" in "+"sem_type;"+"\n")
                    
        for j in range(len(sem_anterior)):
                #print(" esta {} en {}?".format(i+1,sem_anterior[j]))
                if str(i+1) == sem_anterior[j]:
                    if int(sem_actual[j]) not in secciones[i].vecinos:
                        f.write("\t\t\t"+"Estado_lejano_"+str(sem_actual[j])+"_i"+" : "+" in "+"std_logic;"+"\n")
                    
        #f.write("\t\t\t"+"Semaforo_cercano"+   " : "+" out "+"sem_type;"+"\n")
        #f.write("\t\t\t"+"Semaforo_lejano"+   " : "+" out "+"sem_type;"+"\n")
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
        
        f.write("\t"+"Estado_o <= Estado_i;"+"\r\n") 
        
        
        
        if secciones[i].semaforo:            
         
            for j in range(secciones[i].N_semaforos):
        
                f.write("\t"+"Semaforo_"+str(j+1)+" : process(Clock,Reset)\n")
                f.write("\t"+"begin\n")
                f.write("\t\t"+"if (Clock = '1' and Clock'Event) then\n")
                f.write("\t\t\t"+"if (Reset = '1') then\n")
                #f.write("\t\t\t\t"+"Estado_o <= '0';"+"\n") 
                #if secciones[i].semaforo:
                #    for j in range(secciones[i].N_semaforos):
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   ".msb <= '0';"+"\n")
                f.write("\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+   ".lsb <= '0';"+"\n")
                f.write("\t\t\t"+"else\n")    
            
                
                if secciones[i].sem_sentido[j] == '<':
                    vecino = "Estado_ante"
                    
                    if secciones[i].anterior or secciones[i].desvio_sup or secciones[i].desvio_inf:
                        vecino_existe = True
                    else:
                        vecino_existe = False
                    
                if secciones[i].sem_sentido[j] == '>':
                    vecino = "Estado_post" 
                    if secciones[i].posterior:
                        vecino_existe = True                                  
                    else:
                        vecino_existe = False  
                
                #f.write("\t\t\t\t"+"--"+"Semaforo_"+str(j+1)+"\n") 
                f.write("\t\t\t\t"+""+"if ( Estado_i = '0' ) then"+"\n") 
                f.write("\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                f.write("\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                f.write("\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n") 
                           
                print("N {} | Sem {} | {} {} | {} {}".format(i+1,j+1,secciones[i].sem_sentido[j],secciones[i].N_aspectos[j],vecino,vecino_existe))
                
                
                if (str(i+1) in sem_anterior or str(i+1) in sem_actual):
                    f.write("\t\t\t\t"+""+"else"+"\n")
                    #print("{} : {}".format(sem_actual[j],secciones[i].vecinos))
                    if int(sem_actual[j]) in secciones[i].vecinos:
                        #print("A")
                        if vecino_existe:
                            f.write("\t\t\t\t\t"+""+"if (Cambio_i = '0') then"+" --Normal"+"\n") 
                            
                            f.write("\t\t\t\t\t\t"+""+"if "+str(vecino)+" = '0' then"+"\n") 
                            f.write("\t\t\t\t\t\t\t"+"--"+"estado = AMARILLO"+"\n") 
                            f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --AMARILLO"+"\n")
                            f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --AMARILLO"+"\n") 
                            
                            f.write("\t\t\t\t\t\t"+""+"else"+"\n") 
                            
                            f.write("\t\t\t\t\t\t\t"+"--"+"Si Color = AMARILLO"+"\n") 
                            f.write("\t\t\t\t\t\t\t"+""+"if (Semaforo_cercano_"+str(sem_actual[j])+"_i.msb = '1'"+" and  "+"Semaforo_cercano_"+str(sem_actual[j])+"_i.lsb = '0') then"+"\n")    
                            
                            f.write("\t\t\t\t\t\t\t\t"+"--"+"estado = VERDE"+"\n") 
                            f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --VERDE"+"\n")
                            f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '1'; --VERDE"+"\n") 
                            
                            f.write("\t\t\t\t\t\t\t"+""+"else"+"\n") 
                            f.write("\t\t\t\t\t\t\t\t"+"--"+"estado = VERDE"+"\n") 
                            f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --VERDE"+"\n")
                            f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '1'; --VERDE"+"\n") 
                            
                            f.write("\t\t\t\t\t\t\t"+""+"end if;"+"\n")         
                            f.write("\t\t\t\t\t\t"+""+"end if;"+"\n")  
                            
                            f.write("\t\t\t\t\t"+""+"else"+"\n") 
                                
                            f.write("\t\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                            f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                            f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n")
                            
                            f.write("\t\t\t\t\t"+""+"end if;"+"\n")
                            
                        else:
                            f.write("\t\t\t\t\t"+"--"+"estado = VERDE"+"\n") 
                            f.write("\t\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --VERDE"+"\n")
                            f.write("\t\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".lsb <= '1'; --VERDE"+"\n") 
                            
                            
                #f.write("\t\t\t\t\t"+"--"+"else"+"\n") 
                         
                    if int(sem_actual[j]) not in secciones[i].vecinos:
                        #print("B")
                        if vecino_existe:
                            if secciones[i].N_aspectos[j] == '3':
                                f.write("\t\t\t\t\t"+""+"if (Cambio_i = '0') then"+" --Normal"+"\n") 
                                
                                
                                f.write("\t\t\t\t\t\t"+""+"if "+str(vecino)+" = '0' then"+"\n") 
                                f.write("\t\t\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n") 
                                
                                f.write("\t\t\t\t\t\t"+""+"else"+"\n") 
                                
                                f.write("\t\t\t\t\t\t\t"+"--"+"Si OTRO = OCUPADO"+"\n") 
                                f.write("\t\t\t\t\t\t\t"+""+"if (Estado_lejano_"+str(sem_actual[j])+"_i = '0') then"+"\n")    
                                
                                f.write("\t\t\t\t\t\t\t\t"+"--"+"estado = AMARILLO"+"\n") 
                                f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --AMARILLO"+"\n")
                                f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --AMARILLO"+"\n") 
                            
                                f.write("\t\t\t\t\t\t\t"+""+"else"+"\n") 
                                f.write("\t\t\t\t\t\t\t\t"+"--"+"estado = VERDE"+"\n") 
                                f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --VERDE"+"\n")
                                f.write("\t\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '1'; --VERDE"+"\n") 
                                
                                f.write("\t\t\t\t\t\t\t"+""+"end if;"+"\n")         
                                f.write("\t\t\t\t\t\t"+""+"end if;"+"\n") 
                                
                                f.write("\t\t\t\t\t"+""+"else"+"\n") 
                                
                                f.write("\t\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                                f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                                f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n")
                                
                                f.write("\t\t\t\t\t"+""+"end if;"+"\n")
                                
                            if secciones[i].N_aspectos[j] == '2':
                                f.write("\t\t\t\t\t"+""+"if (Cambio_i = '1') then"+" --Reverso"+"\n")  
                                
                                f.write("\t\t\t\t\t\t"+""+"if "+str(vecino)+" = '0' then"+"\n") 
                                
                                f.write("\t\t\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n")
                                
                                f.write("\t\t\t\t\t\t"+""+"else"+"\n") 
                                
                                f.write("\t\t\t\t\t\t\t"+"--"+"estado = AMARILLO"+"\n") 
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --AMARILLO"+"\n")
                                f.write("\t\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --AMARILLO"+"\n")                       
                                
                                f.write("\t\t\t\t\t\t"+""+"end if;"+"\n")  
                                
                                f.write("\t\t\t\t\t"+""+"else"+"\n") 
                                
                                f.write("\t\t\t\t\t\t"+"--"+"estado = ROJO"+"\n") 
                                f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".msb <= '0'; --ROJO"+"\n")
                                f.write("\t\t\t\t\t\t"+""+"Semaforo_propio_o_"+str(j+1)+".lsb <= '0'; --ROJO"+"\n")
                                
                                f.write("\t\t\t\t\t"+""+"end if;"+"\n")  
                        else:
                            f.write("\t\t\t\t\t"+"--"+"estado = VERDE"+"\n") 
                            f.write("\t\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".msb <= '1'; --VERDE"+"\n")
                            f.write("\t\t\t\t\t"+"Semaforo_propio_o_"+str(j+1)+".lsb <= '1'; --VERDE"+"\n") 
                           
                        
                        
                #f.write("\t\t\t\t\t"+"end if;"+"\n") 
                f.write("\t\t\t\t"+""+"end if;"+"\n")
                f.write("\t\t\t"+"end if;\n")
                f.write("\t\t"+"end if;\n")
                f.write("\t"+"end process;\r\n")
          #print("a {} le importa {}".format(sem_anterior[j],sem_actual[j]))
            
             
        
           
         
        f.write("end Behavioral;") 
        
        f.close()  # Close header file    
    
    if test:
        print("Nodo > Finalizado")
#%%   
def creando_cambio(secciones,objetos,test = False):   
    
    if test:
        print("Cambios > Creando") 
    
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
        #f.write("\t\t\t"+"if (Reset = '1') then\n")
        #f.write("\t\t\t\t"+"Estado_ante_o <= '0';"+"\n")    
        #f.write("\t\t\t\t"+"Estado_post_o <= '0';"+"\n") 
        #f.write("\t\t\t\t"+"Estado_desv_o <= '0';"+"\n") 
        #f.write("\t\t\t\t"+"Cambio_o <= '0';"+"\n") 
        #f.write("\t\t\t"+"else\n")
        f.write("\t\t\t"+"Cambio_o <= Cambio_i;"+"\n") 
        f.write("\t\t\t"+"if (Cambio_i = '0') then\n")
        
        f.write("\t\t\t\t"+"Estado_ante_o <= Estado_post_i;"+"\n")    
        f.write("\t\t\t\t"+"Estado_post_o <= Estado_ante_i;"+"\n") 
        f.write("\t\t\t\t"+"Estado_desv_o <= '0';"+"\n") 
        
        f.write("\t\t\t"+"else\n")
        
        f.write("\t\t\t\t"+"Estado_ante_o <= Estado_desv_i;"+"\n")    
        f.write("\t\t\t\t"+"Estado_post_o <= '0';"+"\n") 
        f.write("\t\t\t\t"+"Estado_desv_o <= Estado_ante_i;"+"\n") 
        
        f.write("\t\t\t"+"end if;\n")
        #f.write("\t\t\t"+"end if;\n")
        f.write("\t\t"+"end if;\n")
        f.write("\t"+"end process;\r\n")   
         
        f.write("end Behavioral;") 
        
        f.close()  # Close header file    
    
    if test:
        print("Cambios > Finalizado")
    
#%%
def calcular_semaforos(secciones,objetos,tabla,test = False):
   
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    sem_actu = 0
    sem_ante = 1
    sem_post = 2
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    if test:
        print("Semaforeo > Iniciando")
        print("")
    
    sem_index = -1;
    sem_lista = [];
    sem_actual = [];
    sem_anterior = [];
    sem_cant = [0]*N_SEM;
    sem_cambio = [];
    
    semaforeo = np.zeros((3,N_SEM))
    
    for i in range(N_SEM):
        semaforeo[sem_actu][i] = i+1
        semaforeo[sem_ante][i] = -1
        semaforeo[sem_post][i] = -1
        
    #print("{}".format(semaforeo)) 
    if test:
        print("{}".format(tabla['Secuencia'])) 
    
    for i in range(len(tabla['Secuencia'])):
        
        # Semaforos finales
        semaforo_final = tabla['Secuencia'][i].split('-')[-1]
        sem_actual.append(semaforo_final)
        
        if semaforo_final not in sem_lista and secciones[int(semaforo_final)-1].tipo == "Extremo":
            sem_lista.append(semaforo_final)        
            sem_index = sem_index + 1
            #print("i:{}".format(sem_index))
            sem_cant[sem_index] = 1                 
            
            
        # Semaforos inicial
        semaforo_inicial = tabla['Secuencia'][i].split('-')[0]
        sem_anterior.append(semaforo_inicial)
            
        if semaforo_inicial not in sem_lista:
            sem_lista.append(semaforo_inicial)
            sem_index = sem_index + 1
            #print("j:{} / {}".format(sem_index,len(sem_cant)))
            sem_cant[sem_index] = 1     
            
            #print("({})".format(sem_cant))
        else:   
            #print("{} in {}|{}".format(semaforo,sem_lista,sem_cant))
            sem_cant[sem_lista.index(semaforo_inicial)] = sem_cant[sem_lista.index(semaforo_inicial)] + 1
         
        # Busco cambios en el medio
        intermedios = tabla['Secuencia'][i].split('-')[1:-1]
        #print(intermedios)
        
        if intermedios == []:
            sem_cambio.append('T')
        else:
            #print(secciones[int(intermedios[0])-1].tipo)
            if secciones[int(intermedios[0])-1].tipo == "Directo":
                sem_cambio.append('N')    
            if secciones[int(intermedios[0])-1].tipo == "Desvio":
                sem_cambio.append('R') 
            if secciones[int(intermedios[0])-1].tipo == "Cruce":
                if secciones[int(semaforo_inicial)-1].tipo == "Desvio" or secciones[int(semaforo_final)-1].tipo == "Desvio":
                    sem_cambio.append('R')     
                
    while 0 in sem_cant:
      sem_cant.remove(0)   
      
        #print("Semaforo: {} Anterior: {}".format(tabla['Secuencia'][i][-1],tabla['Secuencia'][i][0])) 
    if test:    
        print("{}".format(sem_lista))
        print("#{}".format(sem_cant))
        print("ini:{}".format(sem_anterior))
        print("fin:{}".format(sem_actual))
        print("cmb:{}".format(sem_cambio))
        
    if test:    
        print("")
        print("Semaforeo > Finalizado")     
    
    return sem_cant,sem_actual,sem_anterior,sem_cambio
 
#%%    
def creando_sistema(secciones,objetos,test = False):        
    
    if test:
        print("Sistema > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "Sistema"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad sistema
    sistema = "sistema"
    f.write("\t"+"entity "+sistema+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"r_data"+   " : "+" in "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"r_disponible"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"leer"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"escribir"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"switch1"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"switch2"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"reset_uart"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"N"+   " : "+" in "+"integer"+";\n")
    f.write("\t\t\t"+"leds"+   " : "+" out "+"std_logic_vector(4-1 downto 0)"+";\n")
    f.write("\t\t\t"+"led_rgb_1"+   " : "+" out "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"led_rgb_2"+   " : "+" out "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"w_data"+   " : "+" out "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+sistema+";\r\n") 
   
    f.write("architecture Behavioral of "+sistema+" is\r\n")            

    # componente detector
    detector = "detector"
    f.write("\t"+"component "+detector+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"r_data"+   " : "+" in "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"r_disponible"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"led_rgb_1"+    " : "+" out "+"std_logic_vector(3-1 downto 0)"+";\n") 
    f.write("\t\t\t"+"led_rgb_2"+ " : "+" out "+"std_logic_vector(3-1 downto 0);"+"\n")
    f.write("\t\t\t"+"paquete"+ " : "+" out "+"std_logic_vector("+str(N)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"procesar"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"N"+ " : "+" in "+"integer;"+"\n")
    f.write("\t\t\t"+"wr_uart"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"w_data"+ " : "+" out "+"std_logic_vector(8-1 downto 0);"+"\n")    
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+detector+";\r\n")
    
    # componente enclavamiento
    enclavamiento = "enclavamiento"
    f.write("\t"+"component "+enclavamiento+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesar"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Paquete_i"+ " : "+" in "+"std_logic_vector("+str(N)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"Paquete_o"+ " : "+" out "+"std_logic_vector("+str(M)+"-1 downto 0);"+"\n")    
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+enclavamiento+";\r\n")
    
    # componente selector
    selector = "selector"
    f.write("\t"+"component "+selector+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"switch"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"leds"+ " : "+" out "+"std_logic_vector(2-1 downto 0);"+"\n")
    f.write("\t\t\t"+"wr_uart_1"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"wr_uart_2"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"wr_uart_3"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"w_data_1"+ " : "+" in "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"w_data_2"+ " : "+" in "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"w_data_3"+ " : "+" out "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+selector+";\r\n")
    
    # componente registro
    registro = "registro"
    f.write("\t"+"component "+registro+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesar"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"procesado"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"paquete_i"+ " : "+" in "+"std_logic_vector("+str(M)+"-1 downto 0);"+"\n")
    f.write("\t\t\t"+"w_data"+ " : "+" out "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"wr_uart"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+registro+";\r\n")
    
    f.write("\t"+"Signal paquete_i_s : std_logic_vector("+str(N)+"-1 downto 0);\n")
    f.write("\t"+"Signal paquete_o_s : std_logic_vector("+str(M)+"-1 downto 0);\n")
    
    f.write("\t"+"Signal w_data_1,w_data_2,w_data_3 : std_logic_vector(8-1 downto 0);\n")
    f.write("\t"+"Signal wr_uart_1_s,wr_uart_2_s : std_logic;\n")
    f.write("\t"+"Signal pro_enc_reg,pro_det_enc,pro_reg_det : std_logic;\n\r")
    
    
    f.write("begin\r\n")
    
    f.write("\t"+detector+"_i : "+detector+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"Reset"+",\n")
    f.write("\t\t\t"+"r_data"+" => "+"r_data"+",\n")
    f.write("\t\t\t"+"r_disponible"+" => "+"r_disponible"+",\n")
    f.write("\t\t\t"+"led_rgb_1"+" => "+"led_rgb_1"+",\n")
    f.write("\t\t\t"+"led_rgb_2"+" => "+"led_rgb_2"+",\n")
    f.write("\t\t\t"+"N"+" => "+"N"+",\n")
    f.write("\t\t\t"+"wr_uart"+" => "+"wr_uart_1_s"+",\n")
    f.write("\t\t\t"+"procesar"+" => "+"pro_reg_det"+",\n")
    f.write("\t\t\t"+"procesado"+" => "+"pro_det_enc"+",\n")
    f.write("\t\t\t"+"paquete"+" => "+"paquete_i_s"+",\n")
    f.write("\t\t\t"+"w_data"+" => "+"w_data_1"+"\n")
    f.write("\t\t"+");"+"\r\n")
    
    f.write("\t"+enclavamiento+"_i : "+enclavamiento+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"Reset"+",\n")
    f.write("\t\t\t"+"procesar"+" => "+"pro_det_enc"+",\n")
    f.write("\t\t\t"+"procesado"+" => "+"pro_enc_reg"+",\n")
    f.write("\t\t\t"+"Paquete_i"+" => "+"paquete_i_s"+",\n")
    f.write("\t\t\t"+"Paquete_o"+" => "+"paquete_o_s"+"\n")
    f.write("\t\t"+");"+"\r\n")
    
    f.write("\t"+registro+"_i : "+registro+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"Reset"+",\n")
    f.write("\t\t\t"+"procesar"+" => "+"pro_enc_reg"+",\n")
    f.write("\t\t\t"+"procesado"+" => "+"pro_reg_det"+",\n")
    f.write("\t\t\t"+"paquete_i"+" => "+"paquete_o_s"+",\n")
    f.write("\t\t\t"+"w_data"+" => "+"w_data_2"+",\n")
    f.write("\t\t\t"+"wr_uart"+" => "+"wr_uart_2_s"+"\n")
    f.write("\t\t"+");"+"\r\n")
    
    f.write("\t"+selector+"_i : "+selector+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"Reset"+",\n")
    f.write("\t\t\t"+"switch"+" => "+"switch1"+",\n")
    f.write("\t\t\t"+"wr_uart_1"+" => "+"wr_uart_1_s"+",\n")
    f.write("\t\t\t"+"wr_uart_2"+" => "+"wr_uart_2_s"+",\n")
    f.write("\t\t\t"+"wr_uart_3"+" => "+"escribir"+",\n")
    f.write("\t\t\t"+"w_data_1"+" => "+"w_data_1"+",\n")
    f.write("\t\t\t"+"w_data_2"+" => "+"w_data_2"+",\n")
    f.write("\t\t\t"+"w_data_3"+" => "+"w_data_3"+"\n")
    f.write("\t\t"+");"+"\r\n")
    
    f.write("\t\t"+"w_data <= w_data_3;"+"\r\n")
     
    f.write("\t\t"+"process(Clock)"+"\n")
    f.write("\t\t"+"begin"+"\n")
    f.write("\t\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")               
    f.write("\t\t\t\t"+"if switch2 = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"leds <= std_logic_vector(to_unsigned(N,4));"+"\n")                
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"leds(3) <= paquete_i_s(3);"+"\n")
    f.write("\t\t\t\t\t"+"leds(2) <= paquete_i_s(2);"+"\n")
    f.write("\t\t\t\t\t"+"leds(1) <= paquete_i_s(1);"+"\n") 
    f.write("\t\t\t\t\t"+"leds(0) <= paquete_i_s(0);"+"\n")  
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end process;"+"\r\n") 
        
    f.write("\t\t"+"process(Clock)"+"\n")
    f.write("\t\t"+"variable contador: integer := 0;"+"\n")
    f.write("\t\t"+"begin"+"\n")
    f.write("\t\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")               
    f.write("\t\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"reset_uart <= '0';"+"\n")                
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"contador := contador + 1;"+"\n")
    f.write("\t\t\t\t\t"+"if contador = 10*125E6 then"+"\n")
    f.write("\t\t\t\t\t\t"+"contador := 0;"+"\n") 
    f.write("\t\t\t\t\t\t"+"reset_uart <= '1';"+"\n")  
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"reset_uart <= '0';"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end process;"+"\r\n") 
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Sistema > Finalizado")
    
#%%    
def creando_global(secciones,objetos,test = False):        
    
    if test:
        print("Global > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "global"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad sistema
    wrapper = "global"
    f.write("\t"+"entity "+wrapper+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+" : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"uart_rxd_i"+" : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"uart_txd_o"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"leds"+   " : "+" out "+"std_logic_vector(4-1 downto 0)"+";\n")
    f.write("\t\t\t"+"rgb_1"+   " : "+" out "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"rgb_2"+   " : "+" out "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"switch1"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"switch2"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+wrapper+";\r\n") 
   
    f.write("architecture Behavioral of "+wrapper+" is\r\n")            

    # componente uart_control
    uart_control = "uart_control"
    f.write("\t"+"component "+uart_control+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"N"+   " : "+" out "+"integer"+";\n")
    f.write("\t\t\t"+"escribir"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"vacio_in"+    " : "+" in "+"std_logic"+";\n") 
    f.write("\t\t\t"+"rd_uart"+ " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"wr_uart"+ " : "+" out "+"std_logic"+";\n")  
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+uart_control+";\r\n")
    
    # componente sistema
    sistema = "sistema"
    f.write("\t"+"component "+sistema+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+   " : "+" in "+"std_logic;"+"\n")
    
    f.write("\t\t\t"+"reset_uart"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"r_disponible"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"leer"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"escribir"+ " : "+" out "+"std_logic;"+"\n")
    f.write("\t\t\t"+"r_data"+ " : "+" in "+"std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"switch1"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"switch2"+ " : "+" in "+"std_logic;"+"\n")
    f.write("\t\t\t"+"N"+ " : "+" in "+"integer;"+"\n")
    f.write("\t\t\t"+"leds"+ " : "+" out "+"std_logic_vector(4-1 downto 0);"+"\n")
    f.write("\t\t\t"+"led_rgb_1"+ " : "+" out "+"std_logic_vector(3-1 downto 0);"+"\n")
    f.write("\t\t\t"+"led_rgb_2"+ " : "+" out "+"std_logic_vector(3-1 downto 0);"+"\n")
    f.write("\t\t\t"+"w_data"+ " : "+" out "+"std_logic_vector(8-1 downto 0);"+"\n")
   
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end component "+sistema+";\r\n")
    
    f.write("\t"+"Signal w_data_signal, r_dataSignal: std_logic_vector(7 downto 0);\n")
    f.write("\t"+"Signal rd_uart_signal, wr_uart_signal: std_logic;\n")  
    f.write("\t"+"Signal emptySignal,empty_s,tx_empty_s,switch_s,reset_s,reset_uart: std_logic;\n")
    f.write("\t"+"Signal led_s : std_logic_vector(4-1 downto 0);\n")
    f.write("\t"+"Signal led_rgb_1,led_rgb_2 : std_logic_vector(3-1 downto 0);\n\r")
    f.write("\t"+"Signal N_s : integer;\n")
    f.write("\t"+"Signal leer_s,escribir_s : std_logic;\n")
    
    f.write("begin\r\n")
    
    f.write("\t"+"uart_inst : entity work.uart"+"\n")
    
    f.write("\t\t"+"generic map("+"\n")
    f.write("\t\t\t"+"DVSR      => 407,	-- baud rate divisor DVSR = 125M / (16 * baud rate) baud rate = 19200"+"\n")
    f.write("\t\t\t"+"DVSR_BIT  => 9,   --  bits of DVSR"+"\n")
    f.write("\t\t\t"+"FIFO_W_RX	=> "+str(int(round(np.log2(N)))+1)+", 	--  addr bits of FIFO words in FIFO=2^FIFO_W "+"\n")
    f.write("\t\t\t"+"FIFO_W_TX	=> "+str(int(round(np.log2(M)))+1)+" 	--  addr bits of FIFO words in FIFO=2^FIFO_W "+"\n")			
    f.write("\t\t"+")"+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"clk 		=> Clock,"+"\n")
    f.write("\t\t\t"+"reset 		=> Reset,"+"\n")
    f.write("\t\t\t"+"rd_uart 	=> rd_uart_signal,"+"\n")
    f.write("\t\t\t"+"wr_uart 	=> wr_uart_signal,"+"\n")
    f.write("\t\t\t"+"rx 			=> uart_rxd_i,"+"\n")
    f.write("\t\t\t"+"w_data 		=> w_data_signal,"+"\n")
    f.write("\t\t\t"+"rx_empty	=> emptySignal,"+"\n")
    f.write("\t\t\t"+"r_data  	=> r_dataSignal,"+"\n")
    f.write("\t\t\t"+"tx  		=> uart_txd_o"+"\n")	   
    f.write("\t\t"+");"+"\n")
       
    f.write("\t"+uart_control+"_i : "+uart_control+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"reset_uart"+",\n")
    f.write("\t\t\t"+"N"+" => "+"N_s"+",\n")
    f.write("\t\t\t"+"escribir"+" => "+"escribir_s"+",\n")
    f.write("\t\t\t"+"vacio_in"+" => "+"emptySignal"+",\n")
    f.write("\t\t\t"+"rd_uart"+" => "+"rd_uart_signal"+",\n")
    f.write("\t\t\t"+"wr_uart"+" => "+"wr_uart_signal"+"\n")
    f.write("\t\t"+");"+"\r\n")
    
    f.write("\t"+sistema+"_i : "+sistema+"\n")
    f.write("\t\t"+"port map("+"\n")
    f.write("\t\t\t"+"Clock"+" => "+"Clock"+",\n")
    f.write("\t\t\t"+"Reset"+" => "+"Reset"+",\n")
    f.write("\t\t\t"+"reset_uart"+" => "+"reset_s"+",\n")
    f.write("\t\t\t"+"r_disponible"+" => "+"rd_uart_signal"+",\n")
    f.write("\t\t\t"+"leer"+" => "+"leer_s"+",\n")
    f.write("\t\t\t"+"escribir"+" => "+"escribir_s"+",\n")
    f.write("\t\t\t"+"r_data"+" => "+"r_dataSignal"+",\n")
    f.write("\t\t\t"+"switch1"+" => "+"switch1"+",\n")
    f.write("\t\t\t"+"switch2"+" => "+"switch2"+",\n")
    f.write("\t\t\t"+"N"+" => "+"N_s"+",\n")
    f.write("\t\t\t"+"leds"+" => "+"led_s"+",\n")
    f.write("\t\t\t"+"led_rgb_1"+" => "+"led_rgb_1"+",\n")
    f.write("\t\t\t"+"led_rgb_2"+" => "+"led_rgb_2"+",\n")
    f.write("\t\t\t"+"w_data"+" => "+"w_data_signal"+"\n")
    f.write("\t\t"+");"+"\r\n")  
    
    
    f.write("\t"+"rgb_1 <= led_rgb_1;"+"\n")
    f.write("\t"+"rgb_2 <= led_rgb_2;"+"\n")
    f.write("\t"+"leds <= led_s;"+"\n")
    f.write("\t"+"reset_uart <= Reset or reset_s;"+"\r\n") 
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Global > Finalizado")
        
#%%    
def creando_uart_control(secciones,objetos,test = False):        
    
    if test:
        print("Uart_control > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "uart_control"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad sistema
    uart_control = "uart_control"
    f.write("\t"+"entity "+uart_control+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+" : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"N"+" : "+" out "+"integer"+";\n")
    f.write("\t\t\t"+"escribir"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"vacio_in"+   " : "+" in "+"std_logic"+";\n")
    f.write("\t\t\t"+"rd_uart"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"wr_uart"+   " : "+" out "+"std_logic"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+" in "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+uart_control+";\r\n") 
   
    f.write("architecture Behavioral of "+uart_control+" is\r\n")            
    
    f.write("begin\r\n")
       
    f.write("\t"+"lectura : process(Clock)"+"\n")
    f.write("\t\t"+"variable contador_i: integer := 0;"+"\n")
    f.write("\t\t"+"variable L : integer := 0;"+"\n")
    f.write("\t"+"begin"+"\n")   
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"L := 0;"+"\n") 
    f.write("\t\t\t\t"+"rd_uart <= '0';"+"\n")
    f.write("\t\t\t"+"elsif vacio_in = '0' then   -- Tiene datos"+"\n")
    f.write("\t\t\t\t"+"contador_i := contador_i + 1;"+"\n")                          
    f.write("\t\t\t\t"+"if contador_i = 125E3 then    -- Cuento 100 mseg"+"\n")
    f.write("\t\t\t\t\t"+"contador_i := 0;"+"\n")
    f.write("\t\t\t\t\t"+"rd_uart <= '1';     -- Pido el dato"+"\n")
    f.write("\t\t\t\t\t"+"L := L + 1;"+"\n")
    f.write("\t\t\t\t"+"else"+"\n")                    
    f.write("\t\t\t\t\t"+"rd_uart <= '0';"+"\n");
    f.write("\t\t\t\t"+"end if;"+"\n")                     
    f.write("\t\t\t"+"else                    -- No tiene datos"+"\n")
    f.write("\t\t\t\t"+"N <= L;"+"\n")
    f.write("\t\t\t\t"+"rd_uart <= '0';"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"escritura : process(Clock)"+"\n")
    f.write("\t\t"+"variable contador_j: integer := 0;"+"\n")
    f.write("\t"+"begin"+"\n")   
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"wr_uart <= '0';"+"\n")
    f.write("\t\t\t"+"else"+"\n")                    
    f.write("\t\t\t\t"+"wr_uart <= escribir;"+"\n");
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n") 
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Uart_control > Finalizado")  
    
#%%    
def creando_detector(secciones,objetos,test = False):        
    
    if test:
        print("Detector > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "detector"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad sistema
    detector = "detector"
    f.write("\t"+"entity "+detector+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"r_data"+" : "+"in"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"r_disponible"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"led_rgb_1"+" : "+"out"+" "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"led_rgb_2"+" : "+"out"+" "+"std_logic_vector(3-1 downto 0)"+";\n")
    f.write("\t\t\t"+"paquete"+" : "+"out"+" "+"std_logic_vector("+str(N)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"procesar"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"procesado"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"N"+" : "+"in"+" "+"integer"+";\n")
    f.write("\t\t\t"+"wr_uart"+   " : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"w_data"+" : "+"out"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+"in"+" "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+detector+";\r\n") 
   
    f.write("architecture Behavioral of "+detector+" is\r\n")            
    
    
    f.write("\t"+"type estados_t is (inicio,lectura,final,error);"+"\n") 
    f.write("\t"+"signal estado, estado_siguiente : estados_t;"+"\n") 
  
    f.write("\t"+"shared variable contador : integer range 0 to "+str(round(N*1.5))+" := 0;"+"\n")
    
    f.write("\t"+"signal paquete_aux : std_logic_vector("+str(N)+"-1 downto 0);"+"\n")   
    f.write("\t"+"signal nuevo : std_logic;"+"\n")
    f.write("\t"+"signal largo_ok,tags_ok : std_logic;"+"\n")
    f.write("\t"+"signal tags_izq,tags_der : std_logic;"+"\n")
    
    f.write("\t"+"constant tag_inicial : std_logic_vector(8-1 downto 0) := \"00111100\"; -- r_data = '<'"+"\n")
    f.write("\t"+"constant tag_final : std_logic_vector(8-1 downto 0) := \"00111110\"; -- r_data = '>'"+"\n")
    f.write("\t"+"constant char_0 : std_logic_vector(8-1 downto 0) := \"00110000\"; -- r_data = '0'"+"\n")
    f.write("\t"+"constant char_1 : std_logic_vector(8-1 downto 0) := \"00110001\"; -- r_data = '1' "+"\r\n")

    f.write("begin\r\n")
       
    f.write("\t"+"cambio_estados : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")   
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"estado <= inicio;"+"\n") 
    f.write("\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t"+"if procesar = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"estado <= inicio;"+"\n")   
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"estado <= estado_siguiente;"+"\n")  
    f.write("\t\t\t\t"+"end if;"+"\n")                      
    f.write("\t\t\t"+"end if;"+"\n")  
    f.write("\t\t"+"end if;"+"\n")   
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"incrementar_contador : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"contador := 0;"+"\n") 
    f.write("\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t"+"if r_disponible = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"if estado = lectura then"+"\n")
    f.write("\t\t\t\t\t\t"+"if contador < "+str(N+2)+" then"+"\n") 
    f.write("\t\t\t\t\t\t\t"+"contador := contador + 1;"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")  
    f.write("\t\t\t\t"+"if contador > "+str(N)+" and contador < "+str(N+2)+" then"+"\n") 
    f.write("\t\t\t\t\t"+"contador := contador + 1;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")   
    f.write("\t\t\t\t"+"if estado = final or estado = error then"+"\n")
    f.write("\t\t\t\t\t"+"contador := 0;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n") 
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"empaquetado : process(Clock)"+"\n") 
    f.write("\t"+"begin"+"\n") 
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"paquete_aux <= (others => '0');"+"\n")
    f.write("\t\t\t\t"+"nuevo <= '0';"+"\n")
    f.write("\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t"+"if estado = lectura then"+"\n")
    f.write("\t\t\t\t\t"+"if r_disponible = '1' then"+"\n")
    f.write("\t\t\t\t\t\t"+"if contador < "+str(N+1)+" then"+"\n")
    f.write("\t\t\t\t\t\t\t"+"if r_data = char_0 then"+"\n")
    f.write("\t\t\t\t\t\t\t\t"+"paquete_aux("+str(N)+"-contador) <= '0';"+"\n")
    f.write("\t\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t\t\t"+"if r_data = char_1 then"+"\n")
    f.write("\t\t\t\t\t\t\t\t"+"paquete_aux("+str(N)+"-contador) <= '1';"+"\n")
    f.write("\t\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t\t"+"nuevo <= '1';"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")        
    f.write("\t\t\t\t\t\t"+"nuevo <= '0';"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"estados : process(Clock,estado)"+"\n")      
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")          
    f.write("\t\t\t\t"+"estado_siguiente <= inicio;"+"\n")
    f.write("\t\t\t\t"+"tags_izq <= '0';"+"\n") 
    f.write("\t\t\t\t"+"tags_der <= '0';"+"\n")
    f.write("\t\t\t"+"else"+"\n")          
    f.write("\t\t\t\t"+"estado_siguiente <= estado;"+"\n")   
    f.write("\t\t\t\t"+"-- LED4 = RGB2 | LED5 => RGB1"+"\n")
    f.write("\t\t\t\t"+"-- BGR -> 001 = R | 010 = G | 100 = B"+"\n")
    f.write("\t\t\t\t"+"case(estado) is"+"\n")                                             
    f.write("\t\t\t\t\t"+"when inicio =>"+"\n")            
    f.write("\t\t\t\t\t\t"+"tags_izq <= '0';"+"\n") 
    f.write("\t\t\t\t\t\t"+"if r_data = tag_inicial then -- r_data = '<'"+"\n")
    f.write("\t\t\t\t\t\t\t"+"tags_izq <= '1';"+"\n")
    f.write("\t\t\t\t\t\t\t"+"tags_der <= '0';"+"\n")
    f.write("\t\t\t\t\t\t\t"+"estado_siguiente <= lectura;"+"\n")                    
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")               
    f.write("\t\t\t\t\t"+"when lectura =>"+"\n") 
    f.write("\t\t\t\t\t\t"+"if contador = "+str(N+2)+" then -- "+str(N)+" (asi entran "+str(N)+")"+"\n")
    f.write("\t\t\t\t\t\t\t"+"if r_data = tag_final then --  r_data = '>'"+"\n")
    f.write("\t\t\t\t\t\t\t\t"+"tags_der <= '1';"+"\n")               
    f.write("\t\t\t\t\t\t\t\t"+"estado_siguiente <= final;"+"\n")
    f.write("\t\t\t\t\t\t\t"+"else"+"\n") 
    f.write("\t\t\t\t\t\t\t\t"+"tags_der <= '0';"+"\n")    
    f.write("\t\t\t\t\t\t\t\t"+"estado_siguiente <= error;"+"\n")                       
    f.write("\t\t\t\t\t\t\t"+"end if;"+"\n")                      
    f.write("\t\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t\t"+"tags_der <= '0';"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n") 
    f.write("\t\t\t\t\t"+"when final =>"+"\n")  
    f.write("\t\t\t\t\t\t"+"if procesar = '1' then"+"\n")
    f.write("\t\t\t\t\t\t\t"+"estado_siguiente <= inicio;"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")          
    f.write("\t\t\t\t\t"+"when error =>"+"\n") 
    f.write("\t\t\t\t\t\t"+"tags_izq <= '0';"+"\n")
    f.write("\t\t\t\t\t\t"+"tags_der <= '0';"+"\n")
    f.write("\t\t\t\t\t\t"+"estado_siguiente <= inicio;"+"\n")                                       
    f.write("\t\t\t\t\t"+"when others => null;"+"\n")
    f.write("\t\t\t\t"+"end case;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
     
    f.write("\t"+"paquete_listo : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"procesado <= '0';"+"\n") 
    f.write("\t\t\t"+"else"+"\n")  
    f.write("\t\t\t\t"+"if estado = final then"+"\n")          
    f.write("\t\t\t\t\t"+"procesado <= largo_ok and tags_ok;"+"\n")                                 
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"procesado <= '0';"+"\n")   
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")  
    
    f.write("\t"+"analizar_tags : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"tags_ok <= '0';"+"\n") 
    f.write("\t\t\t\t"+"led_rgb_1 <= \"001\"; -- rojo"+"\n")
    f.write("\t\t\t"+"else"+"\n")  
    f.write("\t\t\t\t"+"tags_ok <= tags_izq and tags_der;"+"\n")
    f.write("\t\t\t\t"+"if tags_ok = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"led_rgb_1 <= \"010\"; -- verde"+"\n")
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"led_rgb_1 <= \"001\"; -- rojo"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")               
    f.write("\t\t\t\t"+"if estado = lectura then"+"\n")
    f.write("\t\t\t\t\t"+"led_rgb_1 <= \"001\"; -- rojo"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"analizar_largo : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"largo_ok <= '0';"+"\n") 
    f.write("\t\t\t\t"+"led_rgb_2 <= \"001\"; -- rojo"+"\n") 
    f.write("\t\t\t"+"else"+"\n")  
    f.write("\t\t\t\t"+"if N = "+str(N+2)+" then"+"\n")
    f.write("\t\t\t\t\t"+"largo_ok <= '1';"+"\n") 
    f.write("\t\t\t\t\t"+"led_rgb_2 <= \"010\"; -- verde"+"\n") 
    f.write("\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t"+"largo_ok <= '0';"+"\n")
    f.write("\t\t\t\t\t"+"led_rgb_2 <= \"001\"; -- rojo"+"\n")  
    f.write("\t\t\t\t"+"end if;"+"\n")                
    f.write("\t\t\t\t"+"if estado = lectura then"+"\n")
    f.write("\t\t\t\t\t"+"led_rgb_2 <= \"001\"; -- rojo"+"\n")
    f.write("\t\t\t\t"+"end if;   "+"\n")           
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"paquete_valido : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"paquete <= (others => '0');"+"\n") 
    f.write("\t\t\t"+"else"+"\n")                      
    f.write("\t\t\t\t"+"if estado = final and largo_ok = '1' and tags_ok = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"paquete <= paquete_aux;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")                        
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")   
    
    f.write("\t"+"w_data <= r_data;"+"\n")
    f.write("\t"+"wr_uart <= r_disponible;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Detector > Finalizado")     
    
#%%    
def creando_registro(secciones,objetos,test = False):        
    
    if test:
        print("Registro > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC 
    
    NODO = "registro"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad registro
    registro = "registro"
    f.write("\t"+"entity "+registro+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"procesar"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"procesado"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"paquete_i"+" : "+"in"+" "+"std_logic_vector("+str(M)+"-1 downto 0)"+";\n")
    f.write("\t\t\t"+"w_data"+" : "+"out"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"wr_uart"+   " : "+"out"+" "+"std_logic"+"; -- \"char_disp\"\n")
    f.write("\t\t\t"+"Reset"+   " : "+"in"+" "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+registro+";\r\n") 
   
    f.write("architecture Behavioral of "+registro+" is\r\n")            
     
    f.write("\t"+"type estados_t is (REINICIO,CICLO_1,CICLO_2);"+"\n") 
    f.write("\t"+"signal estado, estado_siguiente : estados_t;"+"\n") 
    f.write("\t"+"signal mux_out_s,ena_s,rst_s,reg_aux : std_logic;"+"\n") 
    f.write("\t"+"signal mux_s : std_logic_vector("+str(math.ceil(np.log2(M+1)))+"-1 downto 0);"+"\r\n")  ### TODO:
  
    f.write("begin\r\n")
       
    f.write("\t"+"contador : process(Clock)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"mux_s <= \""+str("0"*math.ceil(np.log2(M+1)))+"\";"+"\n")               ### TODO:
    f.write("\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t"+"if (ena_s = '1') then"+"\n")        
    f.write("\t\t\t\t\t"+"if (mux_s /= \""+"{0:b}".format(M)+"\") then"+"\n")     ### TODO:
    f.write("\t\t\t\t\t\t"+"if (estado = CICLO_1 or estado = CICLO_2) then"+"\n")
    f.write("\t\t\t\t\t\t\t"+"mux_s <= std_logic_vector(to_unsigned(to_integer(unsigned(mux_s)) + 1 , "+str(math.ceil(np.log2(M+1)))+"));"+"\n")     ### TODO:     
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"if (procesar = '0') then"+"\n")
    f.write("\t\t\t\t\t"+"mux_s <= \""+str("0"*math.ceil(np.log2(M+1)))+"\";"+"\n")             ### TODO:
    f.write("\t\t\t\t"+"end if;"+"\n")             
    f.write("\t\t\t"+"end if;"+"\n") 
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
    
    f.write("\t"+"multiplexor : process(paquete_i,mux_s)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"case mux_s is"+"\n")
    
    for i in range(M):
        f.write("\t\t\t"+"when \""+str(bin(i))[2:].zfill(math.ceil(np.log2(M+1)))+"\" => mux_out_s <= paquete_i("+str(i)+");"+"\n")
        
    f.write("\t\t\t"+"when others => mux_out_s <= '0';"+"\n")
    f.write("\t\t"+"end case;"+"\n")     
    f.write("\t"+"end process;"+"\r\n")   
                  
    f.write("\t"+"w_data <= \"00110001\" when mux_out_s = '1' else \"00110000\";"+"\r\n")

    f.write("\t"+"FSM_reset : process(Clock)"+"\n") 
    f.write("\t"+"begin"+"\n") 
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n") 
    f.write("\t\t\t"+"if Reset = '1' then"+"\n") 
    f.write("\t\t\t\t"+"estado <= REINICIO;"+"\n")           
    f.write("\t\t\t"+"else"+"\n")                  
    f.write("\t\t\t\t"+"if (procesar = '1') then"+"\n")           
    f.write("\t\t\t\t\t"+"estado <= estado_siguiente;"+"\n") 
    f.write("\t\t\t\t"+"else"+"\n") 
    f.write("\t\t\t\t\t"+"estado <= REINICIO;"+"\n") 
    f.write("\t\t\t\t"+"end if;"+"\n") 
    f.write("\t\t\t"+"end if;"+"\n")  
    f.write("\t\t"+"end if;"+"\n") 
    f.write("\t"+"end process;"+"\r\n") 
    
    f.write("\t"+"FSM : process(procesar,estado,mux_s)"+"\n") 
    f.write("\t"+"begin"+"\n") 
    f.write("\t\t"+"estado_siguiente <= estado;"+"\n")    
    f.write("\t\t"+"case estado is"+"\n") 
    f.write("\t\t\t"+"when REINICIO =>"+"\n") 
    f.write("\t\t\t\t"+"wr_uart <= '0';"+"\n") 
    f.write("\t\t\t\t"+"rst_s <= '1';"+"\n") 
    f.write("\t\t\t\t"+"ena_s <= '0';"+"\n") 
    f.write("\t\t\t\t"+"procesado <= '0';"+"\n") 
    f.write("\t\t\t\t"+"reg_aux <= '0';"+"\n")  
    f.write("\t\t\t\t"+"if (procesar = '1' and mux_s /= \""+"{0:b}".format(M)+"\" ) then"+"\n") 
    f.write("\t\t\t\t\t"+"estado_siguiente <= CICLO_1;"+"\n") 
    f.write("\t\t\t\t"+"end if;"+"\n") 
    f.write("\t\t\t"+"when CICLO_1 =>"+"\n") 
    f.write("\t\t\t\t"+"wr_uart <= '0';"+"\n") 
    f.write("\t\t\t\t"+"rst_s <= '0';"+"\n") 
    f.write("\t\t\t\t"+"ena_s <= '0';"+"\n") 
    f.write("\t\t\t\t"+"--procesado <= '0';"+"\n")                
    f.write("\t\t\t\t"+"estado_siguiente <= CICLO_2;"+"\n")              
    f.write("\t\t\t"+"when CICLO_2 =>"+"\n") 
    f.write("\t\t\t\t"+"wr_uart <= '1';"+"\n") 
    f.write("\t\t\t\t"+"rst_s <= '0';"+"\n") 
    f.write("\t\t\t\t"+"ena_s <= '1';"+"\n")               
    f.write("\t\t\t\t"+"procesado <= '0';"+"\n") 
    f.write("\t\t\t\t"+"reg_aux <= '0';"+"\n")          
    f.write("\t\t\t\t"+"if mux_s = \""+"{0:b}".format(M-1)+"\" then"+"\n") 
    f.write("\t\t\t\t\t"+"procesado <= '1';"+"\n") 
    f.write("\t\t\t\t\t"+"reg_aux <= '1';"+"\n") 
    f.write("\t\t\t\t\t"+"estado_siguiente <= REINICIO;"+"\n")            
    f.write("\t\t\t\t"+"else"+"\n") 
    f.write("\t\t\t\t\t"+"estado_siguiente <= CICLO_1;"+"\n") 
    f.write("\t\t\t\t"+"end if;"+"\n") 
    f.write("\t\t\t"+"when others => null;"+"\n") 
    f.write("\t\t"+"end case;"+"\n") 
    f.write("\t"+"end process;"+"\r\n") 
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Registro > Finalizado")

#%%    
def creando_selector(secciones,objetos,test = False):        
    
    if test:
        print("Selector > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "selector"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad selector
    selector = "selector"
    f.write("\t"+"entity "+selector+" is\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"Clock"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"switch"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"leds"+" : "+"out"+" "+"std_logic_vector(2-1 downto 0)"+";\n")
    f.write("\t\t\t"+"wr_uart_1"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"wr_uart_2"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"wr_uart_3"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"w_data_1"+" : "+"in"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"w_data_2"+" : "+"in"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"w_data_3"+" : "+"out"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"Reset"+   " : "+"in"+" "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+selector+";\r\n") 
   
    f.write("architecture Behavioral of "+selector+" is\r\n")            
     
    f.write("\t"+"signal disp_aux : std_logic_vector(8-1 downto 0);"+"\r\n") 
  
    f.write("begin\r\n")
       
    f.write("\t"+"switches : process(Clock)"+"\n")   
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (Clock = '1' and Clock'event) then"+"\n")
    f.write("\t\t\t"+"if Reset = '1' then"+"\n")
    f.write("\t\t\t\t"+"w_data_3 <= \"00000000\";"+"\n")
    f.write("\t\t\t\t"+"wr_uart_3 <= '0';"+"\n")
    f.write("\t\t\t"+"else"+"\n") 
    f.write("\t\t\t\t"+"if switch = '1' then"+"\n")                                    
    f.write("\t\t\t\t\t"+"disp_aux <= w_data_2;"+"\n")                  
    f.write("\t\t\t\t\t"+"w_data_3 <= disp_aux;"+"\n")                               
    f.write("\t\t\t\t\t"+"wr_uart_3 <= wr_uart_2;"+"\n")                            
    f.write("\t\t\t\t\t"+"--leds <= \"10\";"+"\n")
    f.write("\t\t\t\t"+"else"+"\n")         
    f.write("\t\t\t\t\t"+"disp_aux <= w_data_1;"+"\n")                   
    f.write("\t\t\t\t\t"+"w_data_3 <= disp_aux;"+"\n")                               
    f.write("\t\t\t\t\t"+"wr_uart_3 <= wr_uart_1;"+"\n")
    f.write("\t\t\t\t\t"+"--leds <= \"01\";"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("Selector > Finalizado")    

#%%    
def creando_fifo(secciones,objetos,test = False):        
    
    if test:
        print("FIFO > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "fifo"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad fifo
    fifo = "fifo"
    f.write("\t"+"entity "+fifo+" is\n")
    f.write("\t\t"+"generic("+"\n")
    f.write("\t\t\t"+"B"+" : "+"natural"+" := "+"8; -- number of bits"+";\n")
    f.write("\t\t\t"+"W"+" : "+"natural"+" := "+"4  -- number of address bits"+";\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"clk, reset"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"rd, wr"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"w_data"+" : "+"in"+" "+"std_logic_vector(B-1 downto 0)"+";\n")
    f.write("\t\t\t"+"empty, full"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"r_data"+   " : "+"out"+" "+"std_logic_vector(B-1 downto 0)"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+fifo+";\r\n") 
   
    f.write("architecture Behavioral of "+fifo+" is\r\n")            
       
    f.write("\t"+"type reg_file_type is array (2**W-1 downto 0) of std_logic_vector(B-1 downto 0);"+"\n") 
    f.write("\t"+"signal array_reg: reg_file_type;"+"\n")
    f.write("\t"+"signal w_ptr_reg, w_ptr_next, w_ptr_succ: std_logic_vector(W-1 downto 0);"+"\n")
    f.write("\t"+"signal r_ptr_reg, r_ptr_next, r_ptr_succ: std_logic_vector(W-1 downto 0);"+"\n")
    f.write("\t"+"signal full_reg, empty_reg, full_next, empty_next: std_logic;"+"\n")
    f.write("\t"+"signal wr_op: std_logic_vector (1 downto 0);"+"\n")
    f.write("\t"+"signal wr_en: std_logic;"+"\r\n")
    
    f.write("begin\r\n")
       
    f.write("\t"+"----------------"+"\n")
    f.write("\t"+"-- register file"+"\n")
    f.write("\t"+"----------------"+"\n")
    f.write("\t"+"process(clk, reset)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (reset = '1') then"+"\n")
    f.write("\t\t\t"+"array_reg <= (others => (others => '0'));"+"\n")
    f.write("\t\t"+"elsif (clk'event and clk = '1') then"+"\n")
    f.write("\t\t\t"+"if wr_en = '1' then"+"\n")
    f.write("\t\t\t\t"+"array_reg(to_integer(unsigned(w_ptr_reg))) <= w_data;"+"\n")
    f.write("\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end process;"+"\r\n")
	
    f.write("\t"+"-- read port"+"\n")
    f.write("\t"+"r_data <= array_reg(to_integer(unsigned(r_ptr_reg)));"+"\r\n")
	
    f.write("\t"+"-- write enabled only when FIFO is not full"+"\n")
    f.write("\t"+"wr_en <= wr and (not full_reg);"+"\r\n")
         
    f.write("\t"+"--"+"\n")
    f.write("\t"+"-- fifo control logic"+"\n")
    f.write("\t"+"--"+"\n")
    f.write("\t"+"-- register for read and write pointers"+"\n")
    f.write("\t"+"process(clk, reset)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (reset = '1') then"+"\n")
    f.write("\t\t\t"+"w_ptr_reg <= ( others => '0');"+"\n")
    f.write("\t\t\t"+"r_ptr_reg <= ( others => '0');"+"\n")
    f.write("\t\t\t"+"full_reg <= '0';"+"\n")
    f.write("\t\t\t"+"empty_reg <= '1';"+"\n")
    f.write("\t\t"+"elsif (clk'event and clk = '1') then	"+"\n")
    f.write("\t\t\t"+"w_ptr_reg <= w_ptr_next;"+"\n")
    f.write("\t\t\t"+"r_ptr_reg <= r_ptr_next;"+"\n")
    f.write("\t\t\t"+"full_reg <= full_next;"+"\n")
    f.write("\t\t\t"+"empty_reg <= empty_next;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")

    f.write("\t"+"-- successive pointer values"+"\n")
    f.write("\t"+"w_ptr_succ <= std_logic_vector(unsigned(w_ptr_reg) + 1);"+"\n")
    f.write("\t"+"r_ptr_succ <= std_logic_vector(unsigned(r_ptr_reg) + 1);"+"\r\n")

    f.write("\t"+"-- next-state logic for read and write pointers"+"\n")
    f.write("\t"+"wr_op <= wr & rd;"+"\r\n")
	
    f.write("\t"+"process (w_ptr_reg, w_ptr_succ, r_ptr_reg, r_ptr_succ ,wr_op, empty_reg, full_reg)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"w_ptr_next <= w_ptr_reg;"+"\n")
    f.write("\t\t"+"r_ptr_next <= r_ptr_reg;"+"\n")
    f.write("\t\t"+"full_next <= full_reg;"+"\n")
    f.write("\t\t"+"empty_next <= empty_reg;"+"\n")	
    f.write("\t\t"+"case wr_op is"+"\n")
    f.write("\t\t\t"+"when \"00\" => -- no op"+"\n")
    f.write("\t\t\t"+"when \"01\" => -- read"+"\n")
    f.write("\t\t\t\t"+"if (empty_reg /= '1') then -- not empty"+"\n")
    f.write("\t\t\t\t\t"+"r_ptr_next <= r_ptr_succ;"+"\n")
    f.write("\t\t\t\t\t"+"full_next <= '0';"+"\n")
    f.write("\t\t\t\t\t"+"if (r_ptr_succ=w_ptr_reg) then"+"\n")
    f.write("\t\t\t\t\t\t"+"empty_next <= '1';"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when \"10\" => -- write"+"\n")
    f.write("\t\t\t\t"+"if (full_reg /= '1') then -- not full"+"\n")
    f.write("\t\t\t\t\t"+"w_ptr_next <= w_ptr_succ;"+"\n")
    f.write("\t\t\t\t\t"+"empty_next <= '0';"+"\n")
    f.write("\t\t\t\t\t"+"if (w_ptr_succ = r_ptr_reg) then"+"\n")
    f.write("\t\t\t\t\t\t"+"full_next <= '1';"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when others => -- write / read;"+"\n")
    f.write("\t\t\t\t"+"w_ptr_next <= w_ptr_succ;"+"\n")
    f.write("\t\t\t\t"+"r_ptr_next <= r_ptr_succ;"+"\n")
    f.write("\t\t"+"end case;"+"\n")
    f.write("\t"+"end process;"+"\r\n")

    f.write("\t"+"-- output"+"\n")
    f.write("\t"+"full <= full_reg;"+"\n")
    f.write("\t"+"empty <= empty_reg;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("FIFO > Finalizado")

#%%    
def creando_uart_rx(secciones,objetos,test = False):        
    
    if test:
        print("UART_rx > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "uart_rx"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad uart_rx
    uart_rx = "uart_rx"
    f.write("\t"+"entity "+uart_rx+" is\n")
    f.write("\t\t"+"generic("+"\n")
    f.write("\t\t\t"+"DBIT"+" : "+"integer"+" := "+"8; -- # data bits"+";\n")
    f.write("\t\t\t"+"SB_TICK"+" : "+"integer"+" := "+"16 -- # ticks for stop bits"+";\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"clk, reset"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"rx"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"s_tick"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"rx_done_tick"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"d_out"+   " : "+"out"+" "+"std_logic_vector(8-1 downto 0)"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+uart_rx+";\r\n") 
   
    f.write("architecture Behavioral of "+uart_rx+" is\r\n")            
       
    f.write("\t"+"type state_type is (idle, start, data, stop);"+"\n")
    f.write("\t"+"signal state_reg, state_next: state_type;"+"\n")
    f.write("\t"+"signal s_reg, s_next: unsigned(3 downto 0);"+"\n")
    f.write("\t"+"signal n_reg, n_next: unsigned(2 downto 0);"+"\n")
    f.write("\t"+"signal b_reg, b_next: std_logic_vector(8-1 downto 0);"+"\r\n")
    
    f.write("begin\r\n")
       
    f.write("\t"+"-- FSMD state & data registers"+"\n")
    f.write("\t"+"process(clk, reset)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if reset = '1' then"+"\n")
    f.write("\t\t\t"+"state_reg <= idle;"+"\n")
    f.write("\t\t\t"+"s_reg <= (others => '0');"+"\n")
    f.write("\t\t\t"+"n_reg <= (others => '0');"+"\n")
    f.write("\t\t\t"+"b_reg <= (others => '0');"+"\n")
    f.write("\t\t"+"elsif (clk'event and clk = '1') then"+"\n")
    f.write("\t\t\t"+"state_reg <= state_next;"+"\n")
    f.write("\t\t\t"+"s_reg <= s_next;"+"\n")
    f.write("\t\t\t"+"n_reg <= n_next;"+"\n")
    f.write("\t\t\t"+"b_reg <= b_next;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
	
    f.write("\t"+"-- next_state logic & data path functional units/routing"+"\n")
    f.write("\t"+"process(state_reg, s_reg, n_reg, b_reg, s_tick, rx)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"state_next <= state_reg;"+"\n")
    f.write("\t\t"+"s_next <= s_reg;"+"\n")
    f.write("\t\t"+"n_next <= n_reg;"+"\n")
    f.write("\t\t"+"b_next <= b_reg;"+"\n")
    f.write("\t\t"+"rx_done_tick <= '0';"+"\n")
    f.write("\t\t"+"case state_reg is"+"\n")
    f.write("\t\t\t"+"when idle =>"+"\n")
    f.write("\t\t\t\t"+"if rx = '0' then"+"\n")
    f.write("\t\t\t\t\t"+"state_next <= start;"+"\n")
    f.write("\t\t\t\t\t"+"s_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when start =>"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = 8-1 then"+"\n")
    f.write("\t\t\t\t\t\t"+"state_next <= data;"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t\t"+"n_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when data =>"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = 15 then"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t\t"+"b_next <= rx & b_reg(8-1 downto 1);"+"\n")
    f.write("\t\t\t\t\t\t"+"if n_reg = (DBIT-1) then"+"\n")
    f.write("\t\t\t\t\t\t\t"+"state_next <= stop;"+"\n")
    f.write("\t\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t\t"+"n_next <= n_reg + 1;"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when stop =>"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = (SB_TICK-1) then"+"\n")
    f.write("\t\t\t\t\t\t"+"state_next <= idle;"+"\n")
    f.write("\t\t\t\t\t\t"+"rx_done_tick <= '1';"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end case;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
	
    f.write("\t"+"d_out <= b_reg;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("UART_rx > Finalizado")
 
#%%    
def creando_uart_tx(secciones,objetos,test = False):        
    
    if test:
        print("UART_tx > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "uart_tx"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad uart_tx
    uart_tx = "uart_tx"
    f.write("\t"+"entity "+uart_tx+" is\n")
    f.write("\t\t"+"generic("+"\n")
    f.write("\t\t\t"+"DBIT"+" : "+"integer"+" := "+"8; -- # data bits"+";\n")
    f.write("\t\t\t"+"SB_TICK"+" : "+"integer"+" := "+"16 -- # ticks for stop bits"+";\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"clk, reset"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"tx_start"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"s_tick"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"d_in"+" : "+"in"+" "+"std_logic_vector(8-1 downto 0)"+";\n")
    f.write("\t\t\t"+"tx_done_tick"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"tx"+   " : "+"out"+" "+"std_logic"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+uart_tx+";\r\n") 
   
    f.write("architecture Behavioral of "+uart_tx+" is\r\n")            
       
    f.write("\t"+"type state_type is (idle, start, data, stop);"+"\n")
    f.write("\t"+"signal state_reg, state_next: state_type;"+"\n")
    f.write("\t"+"signal s_reg, s_next: unsigned(3 downto 0);"+"\n")
    f.write("\t"+"signal n_reg, n_next: unsigned(2 downto 0);"+"\n")
    f.write("\t"+"signal b_reg, b_next: std_logic_vector(7 downto 0);"+"\n")
    f.write("\t"+"signal tx_reg, tx_next: std_logic;"+"\r\n")
       
    f.write("begin\r\n")
       
    f.write("\t"+"-- FSMD state & data registers"+"\n")
    f.write("\t"+"process(clk, reset)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if reset = '1' then"+"\n")
    f.write("\t\t\t"+"state_reg <= idle;"+"\n")
    f.write("\t\t\t"+"s_reg <= (others => '0');"+"\n")
    f.write("\t\t\t"+"n_reg <= (others => '0');"+"\n")
    f.write("\t\t\t"+"b_reg <= (others => '0');"+"\n")
    f.write("\t\t\t"+"tx_reg <= '1';"+"\n")
    f.write("\t\t"+"elsif rising_edge(clk) then"+"\n")
    f.write("\t\t\t"+"state_reg <= state_next;"+"\n")
    f.write("\t\t\t"+"s_reg <= s_next;"+"\n")
    f.write("\t\t\t"+"n_reg <= n_next;"+"\n")
    f.write("\t\t\t"+"b_reg <= b_next;"+"\n")
    f.write("\t\t\t"+"tx_reg <= tx_next;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
	
    f.write("\t"+"-- next-state logic & datapath functional units/routing"+"\n")
    f.write("\t"+"process(state_reg, s_reg, n_reg, b_reg, s_tick, tx_reg, tx_start, d_in)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"state_next <= state_reg;"+"\n")
    f.write("\t\t"+"s_next <= s_reg;"+"\n")
    f.write("\t\t"+"n_next <= n_reg;"+"\n")
    f.write("\t\t"+"b_next <= b_reg;"+"\n")
    f.write("\t\t"+"tx_next <= tx_reg;"+"\n")
    f.write("\t\t"+"tx_done_tick <= '0';"+"\n")
    f.write("\t\t"+"case state_reg is"+"\n")
    f.write("\t\t\t"+"when idle =>"+"\n")
    f.write("\t\t\t\t"+"tx_next <= '1';"+"\n")
    f.write("\t\t\t\t"+"if tx_start = '1' then"+"\n")
    f.write("\t\t\t\t\t"+"state_next <= start;"+"\n")
    f.write("\t\t\t\t\t"+"s_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t"+"b_next <= d_in;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when start =>"+"\n")
    f.write("\t\t\t\t"+"tx_next <= '0';"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = 15 then"+"\n")
    f.write("\t\t\t\t\t\t"+"state_next <= data;"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t\t"+"n_next <= (others => '0');"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when data =>"+"\n")
    f.write("\t\t\t\t"+"tx_next <= b_reg(0);"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = 15 then"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= (others => '0') ;"+"\n")
    f.write("\t\t\t\t\t\t"+"b_next <= '0' & b_reg(8-1 downto 1);"+"\n")
    f.write("\t\t\t\t\t\t"+"if n_reg = (DBIT - 1) then"+"\n")
    f.write("\t\t\t\t\t\t\t"+"state_next <= stop;"+"\n")
    f.write("\t\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t\t"+"n_next <= n_reg + 1 ;"+"\n")
    f.write("\t\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t"+"when stop =>"+"\n")
    f.write("\t\t\t\t"+"tx_next <= '1';"+"\n")
    f.write("\t\t\t\t"+"if (s_tick = '1') then"+"\n")
    f.write("\t\t\t\t\t"+"if s_reg = (SB_TICK - 1) then"+"\n")
    f.write("\t\t\t\t\t\t"+"state_next <= idle;"+"\n")
    f.write("\t\t\t\t\t\t"+"tx_done_tick <= '1';"+"\n")
    f.write("\t\t\t\t\t"+"else"+"\n")
    f.write("\t\t\t\t\t\t"+"s_next <= s_reg + 1;"+"\n")
    f.write("\t\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t\t\t"+"end if;"+"\n")
    f.write("\t\t"+"end case;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
	
    f.write("\t"+"tx <= tx_reg;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("UART_tx > Finalizado")  
    
#%%    
def creando_uart_baud_gen(secciones,objetos,test = False):        
    
    if test:
        print("UART_baud_gen > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "uart_baud_gen"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad uart_baud_gen
    uart_baud_gen = "uart_baud_gen"
    f.write("\t"+"entity "+uart_baud_gen+" is\n")
    f.write("\t\t"+"generic("+"\n")
    f.write("\t\t\t"+"N"+" : "+"integer"+" := "+"4; -- number of bits"+";\n")
    f.write("\t\t\t"+"M"+" : "+"integer"+" := "+"10 -- mod-M"+";\n")
    f.write("\t\t"+");\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"clk, reset"+" : "+"in"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"max_tick"+" : "+"out"+" "+"std_logic"+";\n")
    f.write("\t\t\t"+"q"+   " : "+"out"+" "+"std_logic_vector(N-1 downto 0)"+"\n")
    f.write("\t\t"+");\n")
    f.write("\t"+"end entity "+uart_baud_gen+";\r\n") 
   
    f.write("architecture Behavioral of "+uart_baud_gen+" is\r\n")            
       
    f.write("\t"+"signal r_reg : unsigned(N-1 downto 0);"+"\n")
    f.write("\t"+"signal r_next : unsigned(N-1 downto 0);"+"\r\n")
       
    f.write("begin\r\n")
       
    f.write("\t"+"-- register"+"\n")
    f.write("\t"+"process(clk, reset)"+"\n")
    f.write("\t"+"begin"+"\n")
    f.write("\t\t"+"if (reset='1') then"+"\n")
    f.write("\t\t\t"+"r_reg <= (others => '0');"+"\n")
    f.write("\t\t"+"elsif rising_edge(clk) then"+"\n")
    f.write("\t\t\t"+"r_reg <= r_next;"+"\n")
    f.write("\t\t"+"end if;"+"\n")
    f.write("\t"+"end process;"+"\r\n")
	
    f.write("\t"+"-- next-state logic"+"\n")
    f.write("\t"+"r_next <= (others => '0') when r_reg=(M-1) else r_reg + 1;"+"\r\n")
	
    f.write("\t"+"-- output logic"+"\n")
    f.write("\t"+"q <= std_logic_vector(r_reg);"+"\n")
    f.write("\t"+"max_tick <= '1' when r_reg=(M-1) else '0';"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("UART_baud_gen > Finalizado")
      
#%%    
def creando_uart(secciones,objetos,test = False):        
    
    if test:
        print("UART > Creando") 
    
    N_CVS = objetos[0]
    N_SEM = objetos[1]
    N_PAN = objetos[2]
    N_MDC = objetos[3]
    
    N = N_CVS + 2*N_SEM + N_PAN + N_MDC
    
    M = 2*N_SEM + N_PAN + N_MDC
    
    NODO = "uart"
    f = open("VHDL/"+NODO+".vhd", "w")

    # Comentario inicial
    f.write("-- " + NODO + ".vhdl : Achivo VHDL generado automaticamente\r\n")      
    
    incluir_librerias(f,False) # Incluir librerias
        
    # entidad uart
    uart = "uart"
    f.write("\t"+"entity "+uart+" is\n")
    f.write("\t\t"+"generic("+"\n")
    f.write("\t\t\t"+"-- 19200 baud, 8 data bits, 1 stop bit, 2^2 FIFO"+"\n")
    f.write("\t\t\t"+"DBIT: integer := 8; -- # data bits"+"\n")
    f.write("\t\t\t"+"SB_TICK: integer := 16;	-- # ticks for stop bits, 16/24/32 -- for 1/1.5/2 stop bits"+"\n")									
    f.write("\t\t\t"+"DVSR: integer := 407; 	-- baud rate divisor -- DVSR = 125M / (16 * baud rate)"+"\n")								
    f.write("\t\t\t"+"DVSR_BIT: integer := 9; 	-- # bits of DVSR"+"\n")
    f.write("\t\t\t"+"FIFO_W_TX: integer := 4; 	-- # addr bits of FIFO_TX # words in FIFO=2^FIFO_W"+"\n")
    f.write("\t\t\t"+"FIFO_W_RX: integer := 4 	-- # addr bits of FIFO_TX # words in FIFO=2^FIFO_W"+"\n")
    f.write("\t\t"+");"+"\n")
    f.write("\t\t"+"port("+"\n")
    f.write("\t\t\t"+"clk, reset : in std_logic;"+"\n")
    f.write("\t\t\t"+"rd_uart, wr_uart : in std_logic;"+"\n")
    f.write("\t\t\t"+"rx : in std_logic;"+"\n")
    f.write("\t\t\t"+"w_data : in std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t\t\t"+"tx_full, rx_empty : out std_logic;"+"\n")
    f.write("\t\t\t"+"r_data : out std_logic_vector(8-1 downto 0) ;"+"\n")
    f.write("\t\t\t"+"tx : out std_logic"+"\n")
    f.write("\t\t"+");"+"\n")
    f.write("\t"+"end entity "+uart+";\r\n") 
   
    f.write("architecture Behavioral of "+uart+" is\r\n")            
       
    f.write("\t"+"signal rx_done_tick : std_logic;"+"\n")
    f.write("\t"+"signal tick : std_logic;"+"\n")
    f.write("\t"+"signal tx_fifo_out : std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t"+"signal rx_data_out : std_logic_vector(8-1 downto 0);"+"\n")
    f.write("\t"+"signal tx_empty, tx_fifo_not_empty : std_logic;"+"\n")
    f.write("\t"+"signal tx_done_tick : std_logic;"+"\r\n")
       
    f.write("begin\r\n")
       
    f.write("\t"+"baud_gen_unit: entity work.uart_baud_gen(Behavioral)"+"\n")
    f.write("\t\t"+"generic map(M => DVSR, N => DVSR_BIT)"+"\n")
    f.write("\t\t"+"port map(clk => clk, reset => reset,"+"\n")
    f.write("\t\t\t\t"+"q => open, max_tick => tick);"+"\r\n")
	
    f.write("\t"+"uart_rx_unit: entity work.uart_rx(Behavioral)"+"\n")
    f.write("\t\t"+"generic map(DBIT=>DBIT, SB_TICK=>SB_TICK)"+"\n")
    f.write("\t\t"+"port map(clk=>clk, reset=>reset, rx=>rx,"+"\n")
    f.write("\t\t\t\t"+"s_tick=>tick, rx_done_tick=>rx_done_tick,"+"\n")
    f.write("\t\t\t\t"+"d_out => rx_data_out);"+"\r\n")
				 
    f.write("\t"+"fifo_rx_unit: entity work.fifo(Behavioral)"+"\n")
    f.write("\t\t"+"generic map(B => DBIT, W => FIFO_W_RX)"+"\n")
    f.write("\t\t"+"port map(clk => clk, reset => reset, rd => rd_uart,"+"\n")
    f.write("\t\t\t\t"+"wr => rx_done_tick, w_data => rx_data_out,"+"\n")
    f.write("\t\t\t\t"+"empty => rx_empty, full => open, r_data => r_data);"+"\r\n")
				 
    f.write("\t"+"fifo_tx_unit: entity work.fifo(Behavioral)"+"\n")
    f.write("\t\t"+"generic map(B => DBIT, W => FIFO_W_TX)"+"\n")
    f.write("\t\t"+"port map(clk => clk, reset => reset, rd => tx_done_tick,"+"\n")
    f.write("\t\t\t\t"+"wr=>wr_uart, w_data=>w_data, empty => tx_empty,"+"\n")
    f.write("\t\t\t\t"+"full=>tx_full, r_data=>tx_fifo_out);"+"\r\n")
				 
    f.write("\t"+"uart_tx_unit: entity work.uart_tx(Behavioral)"+"\n")
    f.write("\t\t"+"generic map(DBIT=>DBIT, SB_TICK=>SB_TICK)"+"\n")
    f.write("\t\t"+"port map(clk=>clk, reset=>reset,"+"\n")
    f.write("\t\t\t\t"+"tx_start => tx_fifo_not_empty,"+"\n")
    f.write("\t\t\t\t"+"s_tick => tick, d_in => tx_fifo_out,"+"\n")
    f.write("\t\t\t\t"+"tx_done_tick => tx_done_tick, tx => tx);"+"\r\n")
				 
    f.write("\t"+"tx_fifo_not_empty <= not tx_empty;"+"\r\n")
        
    f.write("end Behavioral;") 
    
    f.close()  # Close header file    
    
    if test:
        print("UART > Finalizado")
        