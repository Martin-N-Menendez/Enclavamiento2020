
from VHDL import *
from Conectores import *
import random

ENM_bloque = "enmascarador"

#%%   ########################################### Señalamiento - variables auxiliares ############################################ 
def enmascarador_aux(f):
   f.write("\tSignal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);\n")
   f.write("\tSignal Reset_sem_s,Reset_Pan_s: std_logic;\r\n") 
    
#%%   ########################################### Mediador - Proceso ############################################   
def enmascarador_proceso(f,N_rutas,N_CVS,N_MDC,N_PAN,N_SEM): 
    #f.write("\tprocess(Clock,Reset)\n")
    #f.write("\tbegin\n")
    #f.write("\t\tif (Clock ='1' and Clock'Event and Reset='1') then\n")
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"if Reset = '1' then\n")
    
    for i in range(N_rutas):
        f.write("\t\t\t\tEstado_PAN_Ruta_"+str(i+1)+" <= (others => '0');\n") 
        f.write("\t\t\t\tPAN_bloq_temp_solape_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_alarma_inmediata_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_alarma_total_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_aprox_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_despeje_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_int_Ruta_"+str(i+1)+" <= '0';\n")
        f.write("\t\t\t\tCV_paralelo_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tCV_paralelo_temp_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tMDC_bloq_temp_solape_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tPos_MDC_aprox_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tPos_MDC_despeje_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tPos_MDC_ruta_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tPos_MDC_solape_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tEstado_ruta_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tEstado_ruta_bloq_Ruta_"+str(i+1)+"<= (others => '0');\n")
        f.write("\t\t\t\tEstado_ruta_cond_Ruta_"+str(i+1)+"<= (others => '0');\n")
        f.write("\t\t\t\tEstado_ruta_confl_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tEstado_sub_ruta_Ruta_"+str(i+1)+" <= (others => '0');\n")
        f.write("\t\t\t\tEstado_SEM_sgte_Ruta_"+str(i+1)+" <= (others => '0');\n")
    
    
    f.write("\t\t\t"+"else\n")
    
    f.write("\t\t\tOcupacion(1) <= Ruta_in(1);\n")
    for i in range(N_rutas):
        
        for j in range(15):  
            text = "Barrera_alta_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Barrera_alta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_PAN_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")

        for j in range(22):  
            text = "Barrera_baja_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Barrera_alta_in("+str(k+1)+")"          
            f.write("\t\t\t\tPAN_bloq_temp_solape_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
            
        for j in range(21):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_alarma_inmediata_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
            
        for j in range(20):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_alarma_total_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
        
        for j in range(4):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_aprox_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
            
        for j in range(3):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_despeje_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
     
        f.write("\t\t\t\tCV_int_Ruta_"+str(i+1)+" <= Circuito_de_via(0) or Circuito_de_via(1);\n")
        f.write("\t\t\t\tEstado_CV_bloq_Ruta_"+str(i+1)+" <= Circuito_de_via(0) and Circuito_de_via(0);\n")
        
        for j in range(1):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_paralelo_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
         
        for j in range(2):  
            text = "Circuito_de_via(0)"
            for k in range(N_CVS-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Circuito_de_via("+str(k+1)+")"          
            f.write("\t\t\t\tCV_paralelo_temp_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")    
 
        for j in range(18):  
            text = "Maquina_reversa_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_normal_in("+str(k+1)+")"          
            f.write("\t\t\t\tMDC_bloq_temp_solape_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n") 
        
        for j in range(10):  
            text = "Maquina_normal_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_reversa_in("+str(k+1)+")"          
            f.write("\t\t\t\tPos_MDC_aprox_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n") 
         
        for j in range(11):  
            text = "Maquina_normal_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_reversa_in("+str(k+1)+")"          
            f.write("\t\t\t\tPos_MDC_despeje_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")     

        for j in range(9):  
            text = "Maquina_normal_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_reversa_in("+str(k+1)+")"          
            f.write("\t\t\t\tPos_MDC_ruta_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
         
        for j in range(12):  
            text = "Maquina_normal_in(0)"
            for k in range(N_PAN-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_reversa_in("+str(k+1)+")"          
            f.write("\t\t\t\tPos_MDC_solape_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")    
 
        for j in range(19):  
            text = "Ruta_in(0)"
            for k in range(N_rutas-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Ruta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_ruta_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
            
        for j in range(17):  
            text = "Ruta_in(0)"
            for k in range(N_rutas-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Ruta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_ruta_bloq_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")
         
        for j in range(6):  
            text = "Ruta_in(0)"
            for k in range(N_rutas-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Ruta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_ruta_cond_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")    
   
        for j in range(7):  
            text = "Ruta_in(0)"
            for k in range(N_rutas-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Ruta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_ruta_confl_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n") 
         
        for j in range(5):  
            text = "Ruta_in(0)"
            for k in range(N_rutas-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Ruta_in("+str(k+1)+")"          
            f.write("\t\t\t\tEstado_sub_ruta_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")     
        

        for j in range(13):  
            text = "Maquina_reversa_in(0)"
            for k in range(N_MDC-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_normal_in("+str(k+1)+")"          
            f.write("\t\t\t\tBloq_MDC_ruta_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")    
            
        for j in range(14):  
            text = "Maquina_normal_in(0)"
            for k in range(N_MDC-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Maquina_reversa_in("+str(k+1)+")"          
            f.write("\t\t\t\tBloq_MDC_solape_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")  
            
        for j in range(8):  
            text = "Semaforo_rojo_in(0)"
            for k in range(N_SEM-1):
                x = random.randint(1,3)
                if ( x != 3):
                    text += " or Semaforo_rojo_in("+str(k+1)+") or Semaforo_amarillo_in("+str(k+1)+") or Semaforo_verde_in("+str(k+1)+")"            
            f.write("\t\t\t\tEstado_SEM_sgte_Ruta_"+str(i+1)+"("+str(j)+") <= "+text+";\n")  
            

        
    f.write("\t\t\t"+"end if;\n")    
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")      
        #f.write("\t\t\tCV_int_Ruta_"+str(i+1)+"(1) <= Circuito_de_via(1);\n")
        
    #f.write("\t\tend if;\n")
    #f.write("\tend process;\n") 

#%%   ########################################### Aleatorizador  de rutas ############################################


#%%    ########################################### Enmascarador ############################################    
def enmascarador_crear(enmascarador,Layout,rutas_dim):
    
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(enmascarador.nombre + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ enmascarador.nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    enmascarador.generico = ["N_CVS","N_SEM","N_PAN","N_MDC","N_RUT"]
    enmascarador.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    enmascarador.puertos_in = ["Clock","Reset","Modo","Ruta_in","Circuito_de_via",
               "Semaforo_rojo_in","Semaforo_amarillo_in","Semaforo_verde_in",
               "Barrera_alta_in","Barrera_baja_in",
               "Maquina_normal_in","Maquina_reversa_in"]
    
    
    enmascarador.puertos_out = ["Ocupacion"]
    
    enmascarador.dimension = ["1"]*2+["N_RUT"]*2+["N_CVS"]*1+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2+["N_CVS"]*1
    
    crear_puertos_ruta(N_rutas,rutas_dim,enmascarador.puertos_out,enmascarador.dimension,"In","ENR")
 
    
    enmascarador.sentidos = ["in"]*(len(enmascarador.puertos_in))+["out"]*(len(enmascarador.puertos_out))
    enmascarador.tipos = ["std_logic"]*(len(enmascarador.puertos_in)+len(enmascarador.puertos_out))
    

    
    enmascarador.instancia = "entidad"
    
    crear_objeto_s(f,enmascarador)
    
    f.write("-- Arquitectura del enmascarador : Descripcion del comportamiento\n")
    
    f.write("architecture "+enmascarador.nombre+"_ARQ of "+enmascarador.nombre+" is\n")
    
    enmascarador_aux(f)
    
    f.write("\t"+"begin\n")   
    
    enmascarador_proceso(f,N_rutas,N_CVS,N_MDC,N_PAN,N_SEM) 
    
    f.write("end architecture "+enmascarador.nombre+"_ARQ;\n")   
    
    f.close() #Close header file
    