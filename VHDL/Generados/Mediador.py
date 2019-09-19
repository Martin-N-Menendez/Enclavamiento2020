
from VHDL import *
from Conectores import *

MDC_salida_bloque = "cambios"
MDC_salida_subbloque = "cambio"

PAN_salida_bloque = "pasos_a_nivel"
PAN_salida_subbloque = "paso_a_nivel"

SEM_salida_bloque = "semaforos"
SEM_salida_subbloque = "semaforo"

MED_bloque = "mediador"

#%%   ########################################### Señalamiento - variables auxiliares ############################################ 
def mediador_aux(f):
   f.write("\tSignal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);\n")
   f.write("\tSignal Reset_sem_s,Reset_Pan_s: std_logic;\r\n") 
    
#%%   ########################################### Mediador - Proceso ############################################   
def mediador_proceso(f,N_rutas,N_CVS,N_MDC,N_PAN,N_SEM): 
    f.write("\tprocess(Clock,Reset)\n")
    f.write("\tbegin\n")
    f.write("\t\tif (Clock ='1' and Clock'Event and Reset='1') then\n")
    for i in range(N_PAN):
        f.write("\t\t\tBarrera_alta("+str(i)+") <= PAN_alto_Ruta_"+str(i+1)+" or PAN_habilitacion_Ruta_"+str(i+1)+";\n")
        f.write("\t\t\tBarrera_baja("+str(i)+") <= PAN_bajo_Ruta_"+str(i+1)+" or PAN_habilitacion_Ruta_"+str(i+1)+";\n")
    for i in range(N_MDC):
        f.write("\t\t\tMaquina_normal("+str(i)+") <= MDC_normal_Ruta_"+str(i+1)+" or MDC_libre_Ruta_"+str(i+1)+" or MDC_cerrojado_Ruta_"+str(i+1)+";\n")
        f.write("\t\t\tMaquina_reversa("+str(i)+") <= MDC_reverso_Ruta_"+str(i+1)+" or MDC_libre_Ruta_"+str(i+1)+" or MDC_cerrojado_Ruta_"+str(i+1)+";\n")
    for i in range(N_SEM):
        f.write("\t\t\tSemaforo_rojo("+str(i)+") <= SEM_rojo_Ruta_"+str(i+1)+";\n")
        f.write("\t\t\tSemaforo_amarillo("+str(i)+") <= SEM_naranja_Ruta_"+str(i+1)+" or SEM_doble_naranja_Ruta_"+str(i+1)+";\n")
        f.write("\t\t\tSemaforo_verde("+str(i)+") <= SEM_verde_Ruta_"+str(i+1)+";\n")
    f.write("\t\tend if;\n")
    f.write("\tend process;\n") 

#%%   ########################################### Aleatorizador  de rutas ############################################
def salida_rutas(add):   
    
    puertos = []
    for i in range(add):
        puertos.append("Cosa_out_"+str(i+1))
    
    return puertos

def entrada_rutas(add):   
    
    puertos = []
    for i in range(add):
        puertos.append("Cosa_in_"+str(i+1))
    
    return puertos

#%%    ########################################### Mediador ############################################      
def mediador_crear(mediador,Layout,rutas_dim,FSM_dim):

    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(mediador.nombre + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ mediador.nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
  
    mediador.generico = ["N_CVS","N_SEM","N_PAN","N_MDC","N_RUT"]
    mediador.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    mediador.puertos_in = ["Clock","Reset"]
    mediador.puertos_out = ["Semaforo_rojo","Semaforo_amarillo","Semaforo_verde"] + ["Barrera_baja","Barrera_alta"] + ["Maquina_normal","Maquina_reversa"]
    mediador.dimension = ["1"]*2
    
    crear_puertos_ruta(N_rutas,FSM_dim,mediador.puertos_in,mediador.dimension,"Out","ENR")
    
    mediador.dimension += ["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2
    
    mediador.sentidos = ["in"]*(len(mediador.puertos_in))+["out"]*(len(mediador.puertos_out))
    mediador.tipos = ["std_logic"]*(len(mediador.puertos_in)+len(mediador.puertos_out))
    
    mediador.instancia = "entidad"  
    
    
    crear_objeto_s(f,mediador)
    
    f.write("-- Arquitectura del señalamiento : Descripcion del comportamiento\n")
    
    f.write("architecture "+mediador.nombre+"_ARQ of "+mediador.nombre+" is\n")

    mediador_aux(f)
    
    f.write("\t"+"begin\n")   
    
    mediador_proceso(f,N_rutas,N_CVS,N_MDC,N_PAN,N_SEM)
    
    f.write("end architecture "+mediador.nombre+"_ARQ;\n")
    
    f.close() #Close header file
    