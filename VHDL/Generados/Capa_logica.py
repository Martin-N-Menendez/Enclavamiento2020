from VHDL import *
from Unidad_central_enclavamiento import *

CAL_bloque = "capa_logica"

CFG_bloque = "validador_modo"
RUT_bloque = "validador_rutas"
ERR_bloque = "gestor_de_errores"
UCE_bloque = "unidad_central_enclavamiento"

#%%   ########################################### Capa lógica - variables auxiliares ############################################ 
def CAL_aux(f):
   
   f.write("\tSignal cv_s,aux_s: std_logic_vector(N_CVS-1 downto 0);\n")
   f.write("\tSignal Modo_in_s,Modo_s,Rutas_s: std_logic_vector(N_RUT-1 downto 0);\n")
   f.write("\tSignal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);\n")
   f.write("\tSignal Reset_sem_s,Reset_Pan_s,aux1_s,aux2_s: std_logic;\r\n")


#%%   ########################################### Capa lógica - conexiones ############################################ 
def CAL_conexiones(f):
    
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
    
#%%   ########################################### Validador de modos - Instanciación ############################################     
def CAL_inst_CFG(f):
    
    f.write("\tvalidador_modo_inst:validador_modo port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tModo_in => Modo,\n")
    f.write("\t\tModo_out => Modo_s);\r\n")
#%%   ########################################### Validador de rutas - Instanciación ############################################     
def CAL_inst_RUT(f):
    
    f.write("\tvalidador_rutas_inst:validador_rutas port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tModo_in => Modo_s,\n")
    f.write("\t\tRuta_in => Ruta_in,\n")
    f.write("\t\tOcupacion => Circuitos_de_via,\n")
    f.write("\t\tRutas_out => Rutas_s);\r\n")
#%%   ########################################### Gestor de errores - Instanciación ############################################     
def CAL_inst_ERR(f):
    
    f.write("\tgestor_de_errores_inst:gestor_de_errores port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tError_1 => aux1_s,\n")
    f.write("\t\tError_2 => aux2_s,\n")
    f.write("\t\tError => aux_s);\r\n")
#%%   ########################################### Unidad central de enclavamiento - Instanciación ############################################     
def CAL_inst_UCE(f):
    
    f.write("\tunidad_central_enclavamiento_inst:unidad_central_enclavamiento port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")
    f.write("\t\tOcupacion => Circuitos_de_via,\n") 
    f.write("\t\tRuta_in => Rutas_s,\n") 
    f.write("\t\tModo => Modo_s,\n") 
    f.write("\t\tSemaforo_rojo_in => Rojo_in_s,\n")
    f.write("\t\tSemaforo_amarillo_in => Amarillo_in_s,\n")
    f.write("\t\tSemaforo_verde_in => Verde_in_s,\n")
    f.write("\t\tSemaforo_rojo_out => Rojo_out_s,\n")
    f.write("\t\tSemaforo_amarillo_out => Amarillo_out_s,\n")
    f.write("\t\tSemaforo_verde_out => Verde_out_s,\n")
    f.write("\t\tBarrera_alta_in => Alto_in_s,\n")
    f.write("\t\tBarrera_baja_in => Bajo_in_s,\n")
    f.write("\t\tBarrera_alta_out => Alto_out_s,\n")
    f.write("\t\tBarrera_baja_out => Bajo_out_s,\n")
    f.write("\t\tMaquina_normal_in => Maquina_normal_in_s,\n")
    f.write("\t\tMaquina_reversa_in => Maquina_reversa_in_s,\n")
    f.write("\t\tMaquina_normal_out => Maquina_normal_out_s,\n")
    f.write("\t\tMaquina_reversa_out => Maquina_reversa_out_s);\r\n")    

#%%   ########################################### Validador de modo - Proceso ############################################
def validador_modo_proceso(f):
    
    f.write("\t"+"process(Clock)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"Modo_out <= Modo_in;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")
   
#%%   ########################################### Validador de ruta - Proceso ############################################
def validador_ruta_proceso(f):
    
    f.write("\t"+"process(Clock)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"Rutas_out <= Ruta_in;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")

#%%   ########################################### Gestor de errores - Proceso ############################################
def gestor_errores_proceso(f):
    
    f.write("\t"+"process(Clock)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"Error(1) <= Error_1;\n")
    f.write("\t\t\t"+"Error(2) <= Error_2;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")

#%%   ########################################### Unidad Central de Enclavamiento - Proceso ############################################
def CAL_proceso(f):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event and Reset='1') then\n")
    f.write("\t\t\t"+"Reset_sem_s <= '0';\n")
    f.write("\t\t\t"+"Reset_pan_s <= '0';\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    
    
#%%    ########################################### Validador de modo ############################################    
def validador_modo(validador_modos,Layout):
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(CFG_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ CFG_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    validador_modos.generico = ["N_CVS","N_RUT"]
    validador_modos.dimension_generico = [str(N_CVS),str(N_rutas)]
    validador_modos.puertos_in = ["Clock","Modo_in"]
    validador_modos.puertos_out = ["Modo_out"]
    validador_modos.sentidos = ["in"]*2+["out"]*1
    validador_modos.tipos = ["std_logic"]*3
    validador_modos.dimension = ["1"]*1+["N_RUT"]*2
    
    validador_modos.instancia = "entidad"
    
    crear_objeto_s(f,validador_modos)
    
    f.write("-- Arquitectura del validador_modo : Descripcion del comportamiento\n")
    
    f.write("architecture "+CFG_bloque+"_ARQ of "+CFG_bloque+" is\n")
    f.write("\t"+"begin\n")   
    
    validador_modo_proceso(f) 
    
    f.write("end architecture "+CFG_bloque+"_ARQ;\n")    
    
    f.close() #Close header file
    
#%%    ########################################### Validador de ruta ############################################   
def validador_ruta(validador_rutas,Layout):
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(RUT_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ RUT_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")

    incluir_librerias(f) #Incluir librerias
    
    validador_rutas.generico = ["N_CVS","N_RUT"]
    validador_rutas.dimension_generico = [str(N_CVS),str(N_rutas)]
    validador_rutas.puertos_in = ["Clock","Modo_in","Ruta_in","Ocupacion"]
    validador_rutas.puertos_out = ["Rutas_out"]
    validador_rutas.sentidos = ["in"]*4+["out"]*1
    validador_rutas.tipos = ["std_logic"]*5
    validador_rutas.dimension = ["1"]*1+["N_RUT"]*2+["N_CVS"]*1+["N_RUT"]*1
    
    validador_rutas.instancia = "entidad"
    
    crear_objeto_s(f,validador_rutas)

    
    f.write("-- Arquitectura del validador_modo : Descripcion del comportamiento\n")
    
    f.write("architecture "+RUT_bloque+"_ARQ of "+RUT_bloque+" is\n")
    f.write("\t"+"begin\n")   
    
    validador_ruta_proceso(f) 
    
    f.write("end architecture "+RUT_bloque+"_ARQ;\n")
    
    f.close() #Close header file

    
#%%    ########################################### Gestor de errores ############################################    
def gestor_de_errores(gestor_errores,Layout):
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(ERR_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ ERR_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    gestor_errores.generico = ["N_CVS"]
    gestor_errores.dimension_generico = [str(N_CVS)]
    gestor_errores.puertos_in = ["Clock","Error_1","Error_2"]
    gestor_errores.puertos_out = ["Error"]
    gestor_errores.sentidos = ["in"]*3+["out"]*1
    gestor_errores.tipos = ["std_logic"]*4
    gestor_errores.dimension = ["1"]*3+["N_CVS"]*1
    gestor_errores.instancia = "entidad"
    
    crear_objeto_s(f,gestor_errores)
    
    f.write("-- Arquitectura del validador_modo : Descripcion del comportamiento\n")
    
    f.write("architecture "+ERR_bloque+"_ARQ of "+ERR_bloque+" is\n")
    f.write("\t"+"begin\n")   
    
    gestor_errores_proceso(f) 
    
    f.write("end architecture "+ERR_bloque+"_ARQ;\n")   
    
    f.close() #Close header file
    
    
#%%    ########################################### Capa logica ############################################      
def capa_logica_crear(capa_logica,validador_modos,validador_rutas,gestor_errores,UCE,
                      enmascarador,enrutador,mediador,senialamiento,
                      FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,
                      SEM_bloque,PAN_bloque,MDC_bloque,
                      Layout,rutas_dim,FSM_dim):

    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    validador_modo(validador_modos,Layout)
    validador_ruta(validador_rutas,Layout)
    gestor_de_errores(gestor_errores,Layout)


    unidad_central_enclavamiento(UCE,enmascarador,enrutador,mediador,senialamiento,
                      FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,
                      SEM_bloque,PAN_bloque,MDC_bloque,Layout,rutas_dim,FSM_dim)

    f = open(CAL_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ CAL_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    # Entidad capa_logica
    capa_logica.generico = ["N_CVS","N_SEM","N_PAN","N_MDC","N_RUT"]
    capa_logica.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    
    capa_logica.puertos_in = ["Clock","Reset","Modo","Ruta_in","Circuitos_de_via",
               "Semaforo_rojo_in","Semaforo_amarillo_in","Semaforo_verde_in",
               "Barrera_alta_in","Barrera_baja_in",
               "Maquina_normal_in","Maquina_reversa_in"]
    capa_logica.puertos_out = ["Semaforo_rojo_out","Semaforo_amarillo_out","Semaforo_verde_out",
               "Barrera_alta_out","Barrera_baja_out",
               "Maquina_normal_out","Maquina_reversa_out"]
    capa_logica.sentidos = ["in"]*12+["out"]*7
    capa_logica.tipos = ["std_logic"]*19
    capa_logica.dimension = ["1"]*2+["N_RUT"]*2+["N_CVS"]*1+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2
    
    capa_logica.instancia = "entidad"
    
    crear_objeto_s(f,capa_logica)
    
    f.write("-- Arquitectura del señalamiento : Descripcion del comportamiento\n")
    
    f.write("architecture "+CAL_bloque+"_ARQ of "+CAL_bloque+" is\n")

    # componente validador_modos 
    validador_modos.instancia = "componente"
    
    crear_objeto_s(f,validador_modos)
    
    # componente validador_rutas
    validador_rutas.instancia = "componente"
    
    crear_objeto_s(f,validador_rutas)
    
    # componente gestor_errores
    gestor_errores.instancia = "componente"
    
    crear_objeto_s(f,gestor_errores)

    # componente gestor_errores
    UCE.instancia = "componente"
    
    #crear_objeto_s(f,UCE)
   
#    generico = []
#    dimension_generico = []
#    puertos = ["Clock","Reset","Modo","Ruta_in","Ocupacion",
#               "Semaforo_rojo_in","Semaforo_amarillo_in","Semaforo_verde_in",
#               "Barrera_alta_in","Barrera_baja_in",
#               "Maquina_normal_in","Maquina_reversa_in",
#               "Semaforo_rojo_out","Semaforo_amarillo_out","Semaforo_verde_out",
#               "Barrera_alta_out","Barrera_baja_out",
#               "Maquina_normal_out","Maquina_reversa_out"]
#    sentidos = ["in"]*12+["out"]*7
#    tipos = ["std_logic"]*19
#    dimension = ["1"]*3+["N_RUT"]*1+["N"]*1+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2
#    instancia = "componente"
#    
#    crear_objeto(f,UCE_bloque,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)
    
    UCE.instancia = "componente"
    
    crear_objeto_s(f,UCE)
    
    CAL_aux(f)
    
    f.write("\t"+"begin\n")   
    
    CAL_inst_CFG(f)
    CAL_inst_RUT(f)
    CAL_inst_ERR(f)
    CAL_inst_UCE(f)
    
    CAL_conexiones(f)   
    
    CAL_proceso(f)
    
    f.write("end architecture "+CAL_bloque+"_ARQ;\n")
    
    f.close() #Close header file
    
    
    