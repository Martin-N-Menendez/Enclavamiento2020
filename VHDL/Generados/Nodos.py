from VHDL import *
from Enmascarador import *
from Enrutador import *
from Mediador import *
from Senialamiento import *
from Conectores import *

NODOS = "nodo"
ENM_bloque = "enmascarador"
ENR_bloque = "enrutador"
MED_bloque = "mediador"
SEN_bloque = "senialamiento"

#%%   ########################################### Unidad Central de Enclavamiento - variables auxiliares ############################################ 
def UCE_aux(f,N_rutas,rutas_dim,FSM_dim):
   
   f.write("\tSignal aux1_a,aux2_a,aux1_b,aux2_b,aux1_c,aux2_c,cv_s,Posicion_in_s,Permisos_s: std_logic_vector(N-1 downto 0);\n")
   f.write("\tSignal Cosa_1_a,Cosa_2_a,Cosa_3_a,Cosa_4_a,Cosa_5_a: std_logic_vector(N-1 downto 0);\n")
   f.write("\tSignal Cosa_1_b,Cosa_2_b,Cosa_3_b,Cosa_4_b,Cosa_5_b: std_logic_vector(N-1 downto 0);\n")
   f.write("\tSignal Cosa_1_c,Cosa_2_c,Cosa_3_c,Cosa_4_c,Cosa_5_c: std_logic_vector(N-1 downto 0);\n")
   f.write("\tSignal Ruta_in_s: std_logic_vector(N_RUT-1 downto 0);\n")
   f.write("\tSignal Rojo_a,Amarillo_a,Verde_a,Rojo_b,Amarillo_b,Verde_b,Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s,Rojo_s,Amarillo_s,Verde_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal Alto_a,Bajo_a,Alto_b,Bajo_b,Alto_s,Bajo_s,Alto_out_s,Bajo_out_s,Alto_in_s,Bajo_in_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_a,Maquina_reversa_a,Maquina_normal_b,Maquina_reversa_b,Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s,Maquina_normal_s,Maquina_reversa_s: std_logic_vector(N_MDC-1 downto 0);\n")
   f.write("\tSignal Reset_sem_s,Reset_Pan_s: std_logic;\r\n")
   
   auto_creador_rutas(f,N_rutas,rutas_dim,"In")
   
   auto_creador_rutas(f,N_rutas,FSM_dim,"Out")
    

#%%   ########################################### Unidad Central de Enclavamiento - conexiones ############################################ 
def UCE_conexiones(f):
  
    f.write("\tcv_s <= Ocupacion;\n")      
    f.write("\tRojo_in_s <= Semaforo_rojo_in;\n")
    f.write("\tAmarillo_in_s <= Semaforo_amarillo_in;\n")
    f.write("\tVerde_in_s <= Semaforo_verde_in;\n")
    f.write("\tSemaforo_rojo_out <= Rojo_out_s;\n")
    f.write("\tSemaforo_amarillo_out <= Amarillo_out_s;\n")
    f.write("\tSemaforo_verde_out <= Verde_out_s;\n")
    f.write("\tAlto_in_s <= Barrera_alta_in;\n")
    f.write("\tBajo_in_s <= Barrera_baja_in;\n")
    f.write("\tBarrera_alta_out <= Alto_out_s;\n")
    f.write("\tBarrera_baja_out <= Bajo_out_s;\n")
    f.write("\tMaquina_normal_in_s <= Maquina_normal_in;\n")
    f.write("\tMaquina_reversa_in_s <= Maquina_reversa_in;\n")
    f.write("\tMaquina_normal_out <= Maquina_normal_out_s;\n")
    f.write("\tMaquina_reversa_out <= Maquina_reversa_out_s;\r\n")
    

#%%   ########################################### Enmascarador - Instanciación ############################################   
def UCE_inst_ENM(f,N_rutas):
    
    f.write("\tenmascarador_inst:enmascarador port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")
    f.write("\t\tModo => Modo,\n")
    f.write("\t\tRuta_in => Ruta_in,\n")
    f.write("\t\tCircuito_de_via => cv_s,\n")
    f.write("\t\tSemaforo_rojo_in => Semaforo_rojo_in,\n")
    f.write("\t\tSemaforo_amarillo_in => Semaforo_amarillo_in,\n")
    f.write("\t\tSemaforo_verde_in => Semaforo_verde_in,\n")
    f.write("\t\tBarrera_alta_in => Barrera_alta_in,\n")
    f.write("\t\tBarrera_baja_in => Barrera_baja_in,\n")  
    
    auto_conector_enrutador(f,N_rutas,"In")    
    
    f.write("\t\tMaquina_normal_in => Maquina_normal_in,\n")
    f.write("\t\tMaquina_reversa_in => Maquina_reversa_in);\r\n")  
               
#%%   ########################################### Enrutador - Instanciación ############################################     
def UCE_inst_ENR(f,N_rutas):
    f.write("\tenrutador_inst:enrutador port map(\n")
    f.write("\t\tClock => Clock,\n")
    

          
    auto_conector_enrutador(f,N_rutas,"In")
    
    auto_conector_enrutador(f,N_rutas,"Out")
    
    f.write("\t\tReset => Reset);\r\n")
    
    #f.write("\t\tSalida1 => aux1_b,\n")
    #f.write("\t\tSalida2 => aux2_b);\r\n")
    
#%%   ########################################### Mediador - Instanciación ############################################   
def UCE_inst_MED(f,N_rutas):
    
    f.write("\tmediador_inst:mediador port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")

    auto_conector_enrutador(f,N_rutas,"Out")

    f.write("\t\tBarrera_alta => Alto_s,\n")
    f.write("\t\tBarrera_baja => Bajo_s,\n")
    f.write("\t\tMaquina_normal => Maquina_normal_s,\n")
    f.write("\t\tMaquina_reversa => Maquina_reversa_s,\n")
    f.write("\t\tSemaforo_rojo => Rojo_s,\n")
    f.write("\t\tSemaforo_amarillo => Amarillo_s,\n")
    f.write("\t\tSemaforo_verde => Verde_s);\r\n")  
    
#%%   ########################################### Señalamiento - Instanciación ############################################   
def UCE_inst_SEN(f):
    
    f.write("\tsenialamiento_inst:senialamiento port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset\n")
   
    f.write("\t\t);\r\n")
    

    
 
#%%   ########################################### Unidad Central de Enclavamiento - Proceso ############################################
def UCE_proceso(f):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event and Reset='1') then\n")
    f.write("\t\t\t"+"Reset_sem_s <= '0';\n")
    f.write("\t\t\t"+"Reset_pan_s <= '0';\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    

#%%   ########################################### Enmascarador - Proceso ############################################
def enmascarador_proceso(f):
    
    f.write("\t"+"process(Clock)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"Maquina_reversa_out <= Maquina_reversa_in;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")
  

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

#%%
def nodos_crear(nodos,i,Layout):   
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(nodos.nombre + "_" + str(i+1) + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ nodos.nombre + "_" + str(i+1) + ".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    cambios_dim = []
    nodos.generico = ["N_RUT","N_SEM"]
    nodos.dimension_generico = [str(N_rutas),str(N_SEM)]
    nodos.puertos_in = ["Clock","Reset","Anterior","Desvio"]
    nodos.puertos_out = ["Posterior"]   
    nodos.dimension = ["1"]*5
    
    nodos.sentidos = ["in"]*(len(nodos.puertos_in))+["out"]*(len(nodos.puertos_out))
    nodos.tipos = ["std_logic"]*(len(nodos.puertos_in)+len(nodos.puertos_out))
     
    nodos.instancia = "entidad"
    
    crear_objeto_s_i(f,nodos,i)    
    
    f.write("-- Arquitectura de FSM_cambios_"+str(i+1)+" : Descripcion del comportamiento\n")
    
    f.write("architecture "+nodos.nombre+ "_" + str(i+1) +"_ARQ of "+nodos.nombre+"_"+str(i+1)+" is\n")
    f.write("\t"+"begin\n")   
    
    #fsm_cambios_proceso(f,i) 
    
    f.write("end architecture "+nodos.nombre+ "_" + str(i+1) +"_ARQ;\n")   
    
    f.close() #Close header file

    
#%%    ########################################### Señalamiento ############################################      
def red_nodos(nodos,enmascarador,enrutador,mediador,senialamiento,
                      FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,
                      SEM_bloque,PAN_bloque,MDC_bloque,
                      Layout,rutas_dim,FSM_dim):

    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    

   #enrutador_crear(enrutador,FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,Layout,rutas_dim,FSM_dim)

    

    f = open(NODOS + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ NODOS +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    nodos.generico = ["N","N_SEM","N_PAN","N_MDC","N_RUT"]
    nodos.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    nodos.puertos_in = ["Clock","Reset","Modo","Ruta_in"]
    nodos.puertos_out = ["Semaforo_rojo_out"]
    nodos.sentidos = ["in"]*4+["out"]*1
    nodos.tipos = ["std_logic"]*5
    nodos.dimension = ["1"]*2+["N_RUT"]*4+["N_SEM"]*1
    nodos.instancia = "entidad"
    
    crear_objeto_s(f,nodos)
    
    f.write("-- Arquitectura del señalamiento : Descripcion del comportamiento\n")
    
    f.write("architecture "+NODOS+"_ARQ of "+NODOS+" is\n")
    
    # componente enmascarador
    nodos.instancia = "componente"
    
    crear_objeto_s(f,nodos)
    
    
    
    UCE_aux(f,N_rutas,rutas_dim,FSM_dim)
    
    f.write("\t"+"begin\n")   
    
    UCE_inst_ENM(f,N_rutas) 
 
  
    UCE_conexiones(f)   
    
    UCE_proceso(f)
    
    f.write("end architecture "+NODOS+"_ARQ;\n")
    
    f.close() #Close header file