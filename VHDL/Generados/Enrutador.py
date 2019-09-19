from VHDL import *
from Conectores import *

ENR_bloque = "enrutador"

RUT_FSM = "rut_fsm"
SEM_FSM = "sem_fsm"
PAN_FSM = "pan_fsm"
MDC_FSM = "mdc_fsm"



#%%   ########################################### RUT_FSM - Instanciación ############################################     
def ENR_inst_RUT_FSM(f,i,N):
    
    f.write("\t"+RUT_FSM+"_inst_"+str(i+1)+":"+RUT_FSM+"_"+str(i+1)+" port map(\n")    
    f.write("\t\tClock => Clock,\n")
    
    auto_conector_rut(f,i,N,"In")
    
    auto_conector_rut(f,i,N,"Out")
    
    f.write("\t\tReset => Reset);\n")
    

#%%   ########################################### RUT_FSM - Instanciación ############################################     
def ENR_inst_SEM_FSM(f,i,N):
    
    f.write("\t"+SEM_FSM+"_inst_"+str(i+1)+":"+SEM_FSM+"_"+str(i+1)+" port map(\n")    
    f.write("\t\tClock => Clock,\n")
    
    auto_conector_sem(f,i,N,"In")
    
    auto_conector_sem(f,i,N,"Out")
    
    f.write("\t\tReset => Reset);\n")

#%%   ########################################### RUT_FSM - Instanciación ############################################     
def ENR_inst_PAN_FSM(f,i,N):
    
    f.write("\t"+PAN_FSM+"_inst_"+str(i+1)+":"+PAN_FSM+"_"+str(i+1)+" port map(\n")    
    f.write("\t\tClock => Clock,\n")
    
    
    auto_conector_pan(f,i,N,"In")
    
    auto_conector_pan(f,i,N,"Out")
    
    f.write("\t\tReset => Reset);\n")
    

#%%   ########################################### RUT_FSM - Instanciación ############################################     
def ENR_inst_MDC_FSM(f,i,N):
    
    f.write("\t"+MDC_FSM+"_inst_"+str(i+1)+":"+MDC_FSM+"_"+str(i+1)+" port map(\n")
    f.write("\t\tClock => Clock,\n")
    
    auto_conector_mdc(f,i,N,"In")
    
    auto_conector_mdc(f,i,N,"Out")
    
    f.write("\t\tReset => Reset);\n")

    
#%%   ########################################### Enrutador - variables auxiliares ############################################ 
def ENR_aux(f,N,rutas_dim,FSM_dim):
   
   f.write("\tSignal cv_s,Posicion_in_s,Ruta_s,Permisos_s: std_logic_vector(N_RUT-1 downto 0);\n")
   f.write("\tSignal aux_s,Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s,Rojo_s,Amarillo_s,Verde_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal aux1_s,aux2_s,Alto_s,Bajo_s,Alto_out_s,Bajo_out_s,Alto_in_s,Bajo_in_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s,Maquina_normal_s,Maquina_reversa_s: std_logic_vector(N_MDC-1 downto 0);\n")   
   
   cambios_dim = convertir_lista_cambios_in(rutas_dim)
   
   auto_creador_mdc(f,N,cambios_dim,"In")
   
   auto_creador_mdc(f,N,FSM_dim,"Out")
   
   barreras_dim = convertir_lista_barreras_in(rutas_dim)
   
   auto_creador_pan(f,N,barreras_dim,"In")
   
   auto_creador_pan(f,N,FSM_dim,"Out")
   
   semaforos_dim = convertir_lista_semaforos_in(rutas_dim)
   
   #auto_creador_sem(f,N,semaforos_dim,"In")
   
   auto_creador_sem(f,N,FSM_dim,"Out")
   
   ruta_dim = convertir_lista_ruta_in(rutas_dim)
   
   auto_creador_rut(f,N,ruta_dim,"In")
   
   auto_creador_rut(f,N,FSM_dim,"Out")
   
   f.write("\tSignal Reset_sem_s,Reset_Pan_s: std_logic;\r\n")

#%%   ########################################### Enrutador - conexiones ############################################ 
def ENR_conexiones(f,N):
  
    for i in range(N):
        auto_conector_mdc(f,i,N,"Begin")
     
    for i in range(N):
        auto_conector_mdc(f,i,N,"End")    
    
    for i in range(N):
        auto_conector_pan(f,i,N,"Begin")
     
    for i in range(N):
        auto_conector_pan(f,i,N,"End")  
        
        
    #for i in range(N):
    #    auto_conector_sem(f,i,N,"Begin")
     
    for i in range(N):
        auto_conector_sem(f,i,N,"End") 
        
    for i in range(N):
        auto_conector_rut(f,i,N,"Begin")
     
    for i in range(N):
        auto_conector_rut(f,i,N,"End")     
    
#%%   ########################################### Enrutador - Proceso ############################################
def ENR_proceso(f):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event and Reset='1') then\n")
    f.write("\t\t\t"+"Salida1(1) <= '0';\n")
    f.write("\t\t\t"+"Salida2(1) <= '0';\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    
 
#%%   ########################################### FSM_Rutas - Proceso ############################################
def fsm_rutas_proceso(f,i):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"RUT_estado_Ruta_"+str(i+1)+" <= Bloq_MDC_ruta_Ruta_"+str(i+1)+"(1) or Bloq_MDC_solape_Ruta_"+str(i+1)+"(1) or CV_aprox_Ruta_"+str(i+1)+"(1) or CV_despeje_Ruta_"+str(i+1)+"(1) or CV_int_Ruta_"+str(i+1)+" or CV_paralelo_Ruta_"+str(i+1)+"(1) or CV_paralelo_temp_Ruta_"+str(i+1)+"(1);\n")
    f.write("\t\t\t"+"RUT_sem_bloq_slp_Ruta_"+str(i+1)+" <= Estado_PAN_Ruta_"+str(i+1)+"(1) or Estado_SEM_sgte_Ruta_"+str(i+1)+"(1) or Estado_ruta_cond_Ruta_"+str(i+1)+"(1) or Estado_ruta_confl_Ruta_"+str(i+1)+"(1) or Estado_sub_ruta_Ruta_"+str(i+1)+"(1) or Pos_MDC_aprox_Ruta_"+str(i+1)+"(1) or Pos_MDC_despeje_Ruta_"+str(i+1)+"(1);\n")
    f.write("\t\t\t"+"SEM_estado_Ruta_"+str(i+1)+" <= Pos_MDC_ruta_Ruta_"+str(i+1)+"(1) or Pos_MDC_solape_Ruta_"+str(i+1)+"(1) or Estado_SEM_sgte_Ruta_"+str(i+1)+"(1) or Estado_ruta_confl_Ruta_"+str(i+1)+"(1) or CV_int_Ruta_"+str(i+1)+" or CV_despeje_Ruta_"+str(i+1)+"(1) or Bloq_MDC_ruta_Ruta_"+str(i+1)+"(1);\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")  
    
#%%   ########################################### FSM_Semaforos - Proceso ############################################
def fsm_semaforos_proceso(f,i):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"if Reset ='1' then\n")
    f.write("\t\t\t"+"SEM_rojo_Ruta_"+str(i+1)+" <= '0';\n")
    f.write("\t\t\t"+"SEM_doble_naranja_Ruta_"+str(i+1)+" <= '0';\n")
    f.write("\t\t\t"+"SEM_naranja_Ruta_"+str(i+1)+" <= '0';\n")
    f.write("\t\t\t"+"SEM_verde_Ruta_"+str(i+1)+" <= '0';\n")
    f.write("\t\t\t"+"else\n")
    
    f.write("\t\t\t\t"+"SEM_rojo_Ruta_"+str(i+1)+" <= SEM_estado_Ruta_"+str(i+1)+";\n")
    f.write("\t\t\t\t"+"SEM_doble_naranja_Ruta_"+str(i+1)+" <= not SEM_estado_Ruta_"+str(i+1)+";\n")
    f.write("\t\t\t\t"+"SEM_naranja_Ruta_"+str(i+1)+" <= SEM_estado_Ruta_"+str(i+1)+";\n")
    f.write("\t\t\t\t"+"SEM_verde_Ruta_"+str(i+1)+" <= not SEM_estado_Ruta_"+str(i+1)+";\n")
    
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    

#%%   ########################################### FSM_Barreras - Proceso ############################################
def fsm_barreras_proceso(f,i):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"PAN_alarma_Ruta_"+str(i+1)+" <= CV_alarma_inmediata_Ruta_"+str(i+1)+"(1) or CV_alarma_inmediata_Ruta_"+str(i+1)+"(2) or CV_alarma_inmediata_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"PAN_alto_Ruta_"+str(i+1)+" <= CV_alarma_total_Ruta_"+str(i+1)+"(1) or CV_alarma_total_Ruta_"+str(i+1)+"(2) or CV_alarma_total_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"PAN_bajo_Ruta_"+str(i+1)+" <= Estado_ruta_Ruta_"+str(i+1)+"(1) or Estado_ruta_Ruta_"+str(i+1)+"(2) or Estado_ruta_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"PAN_habilitacion_Ruta_"+str(i+1)+" <= PAN_bloq_temp_solape_Ruta_"+str(i+1)+"(1) or PAN_bloq_temp_solape_Ruta_"+str(i+1)+"(2) or PAN_bloq_temp_solape_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    

#%%   ########################################### FSM_Cambios - Proceso ############################################
def fsm_cambios_proceso(f,i):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t"+"MDC_cerrojado_Ruta_"+str(i+1)+" <= Estado_ruta_bloq_Ruta_"+str(i+1)+"(1) or Estado_ruta_bloq_Ruta_"+str(i+1)+"(2) or Estado_ruta_bloq_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"MDC_libre_Ruta_"+str(i+1)+" <= MDC_bloq_temp_solape_Ruta_"+str(i+1)+"(1) or MDC_bloq_temp_solape_Ruta_"+str(i+1)+"(2) or MDC_bloq_temp_solape_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"MDC_normal_Ruta_"+str(i+1)+" <= Estado_CV_bloq_Ruta_"+str(i+1)+" or MDC_bloq_temp_solape_Ruta_"+str(i+1)+"(2) or Estado_ruta_bloq_Ruta_"+str(i+1)+"(3);\n")
    f.write("\t\t\t"+"MDC_reverso_Ruta_"+str(i+1)+" <= Estado_CV_bloq_Ruta_"+str(i+1)+";\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\n")    
    
#%%   ########################################### FSM Rutas ############################################
def fsm_rutas_crear(FSM_rutas,i,Layout,rutas_dim):   
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    
    f = open(FSM_rutas.nombre + "_" + str(i+1) + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ FSM_rutas.nombre + "_" + str(i+1) + ".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    FSM_rutas.generico = ["N_RUT","N_SEM"]
    FSM_rutas.dimension_generico = [str(N_rutas),str(N_SEM)]
    FSM_rutas.puertos_in = ["Clock","Reset"]
    FSM_rutas.puertos_out = []
    FSM_rutas.dimension = ["1"]*2
    
    ruta_dim = convertir_lista_ruta_in(rutas_dim)
    
    crear_puertos_ruta(i,ruta_dim,FSM_rutas.puertos_in,FSM_rutas.dimension,"In","RUT")
    
    ruta_dim = convertir_lista_ruta_out(rutas_dim)
    
    crear_puertos_ruta(i,ruta_dim,FSM_rutas.puertos_out,FSM_rutas.dimension,"Out","RUT")
    
    FSM_rutas.sentidos = ["in"]*(len(FSM_rutas.puertos_in))+["out"]*(len(FSM_rutas.puertos_out))
    FSM_rutas.tipos = ["std_logic"]*(len(FSM_rutas.puertos_in)+len(FSM_rutas.puertos_out))    
    
    FSM_rutas.instancia = "entidad"
    
    crear_objeto_s_i(f,FSM_rutas,i) 
    
    
    f.write("-- Arquitectura de FSM_rutas"+str(i+1)+" : Descripcion del comportamiento\n")
    
    f.write("architecture "+FSM_rutas.nombre+ "_" + str(i+1) +"_ARQ of "+FSM_rutas.nombre+"_"+str(i+1)+" is\n")
    f.write("\t"+"begin\n")   
    
    fsm_rutas_proceso(f,i) 
    
    f.write("end architecture "+FSM_rutas.nombre+ "_" + str(i+1) +"_ARQ;\n")
    
    
    f.close() #Close header file
    
#%%   ########################################### FSM Semaforo ############################################
def fsm_semaforos_crear(FSM_semaforos,i,Layout,rutas_dim):   
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(FSM_semaforos.nombre + "_" + str(i+1) + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ FSM_semaforos.nombre + "_" + str(i+1) + ".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias  
    
    semaforos_dim = []
    FSM_semaforos.generico = ["N_RUT","N_SEM"]
    FSM_semaforos.dimension_generico = [str(N_rutas),str(N_SEM)]
    FSM_semaforos.puertos_in = ["Clock","Reset"]
    FSM_semaforos.puertos_out = []
    FSM_semaforos.dimension = ["1"]*2
    
    semaforos_dim = convertir_lista_semaforos_in(rutas_dim)
    
    crear_puertos_ruta(i,semaforos_dim,FSM_semaforos.puertos_in,FSM_semaforos.dimension,"In","SEM")
    
    semaforos_dim = convertir_lista_semaforos_out(rutas_dim)
    
    crear_puertos_ruta(i,semaforos_dim,FSM_semaforos.puertos_out,FSM_semaforos.dimension,"Out","SEM")
    
    FSM_semaforos.sentidos = ["in"]*(len(FSM_semaforos.puertos_in))+["out"]*(len(FSM_semaforos.puertos_out))
    FSM_semaforos.tipos = ["std_logic"]*(len(FSM_semaforos.puertos_in)+len(FSM_semaforos.puertos_out))
 
    FSM_semaforos.instancia = "entidad"
        
    crear_objeto_s_i(f,FSM_semaforos,i)
    
    f.write("-- Arquitectura de FSM_semaforos"+str(i+1)+" : Descripcion del comportamiento\n")
    
    f.write("architecture "+FSM_semaforos.nombre+ "_" + str(i+1) +"_ARQ of "+FSM_semaforos.nombre+"_"+str(i+1)+" is\n")
    f.write("\t"+"begin\n")   
    
    fsm_semaforos_proceso(f,i) 
    
    f.write("end architecture "+FSM_semaforos.nombre+ "_" + str(i+1) +"_ARQ;\n") 
    
    f.close() #Close header file

#%%   ########################################### FSM Barreras ############################################
def fsm_barreras_crear(FSM_barreras,i,Layout,rutas_dim):   
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
        
    f = open(FSM_barreras.nombre + "_" + str(i+1) + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ FSM_barreras.nombre + "_" + str(i+1) + ".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    barreras_dim = []
    FSM_barreras.generico = ["N_RUT","N_SEM"]
    FSM_barreras.dimension_generico = [str(N_rutas),str(N_SEM)]
    FSM_barreras.puertos_in = ["Clock","Reset"]
    FSM_barreras.puertos_out = []
    FSM_barreras.dimension = ["1"]*2
    
    barreras_dim = convertir_lista_barreras_in(rutas_dim)
    
    #print("{}".format(barreras_dim))
    
    crear_puertos_ruta(i,barreras_dim,FSM_barreras.puertos_in,FSM_barreras.dimension,"In","PAN")
    
    barreras_dim = convertir_lista_barreras_out(rutas_dim)
    
    crear_puertos_ruta(i,barreras_dim,FSM_barreras.puertos_out,FSM_barreras.dimension,"Out","PAN")
    
    FSM_barreras.sentidos = ["in"]*(len(FSM_barreras.puertos_in))+["out"]*(len(FSM_barreras.puertos_out))
    FSM_barreras.tipos = ["std_logic"]*(len(FSM_barreras.puertos_in)+len(FSM_barreras.puertos_out))
    
    FSM_barreras.instancia = "entidad"
    
    crear_objeto_s_i(f,FSM_barreras,i)
    
    f.write("-- Arquitectura de FSM_barreras_"+str(i+1)+" : Descripcion del comportamiento\n")
    
    f.write("architecture "+FSM_barreras.nombre+ "_" + str(i+1) +"_ARQ of "+FSM_barreras.nombre+"_"+str(i+1)+" is\n")
    f.write("\t"+"begin\n")   
    
    fsm_barreras_proceso(f,i) 
    
    f.write("end architecture "+FSM_barreras.nombre+ "_" + str(i+1) +"_ARQ;\n")      
    
    f.close() #Close header file

#%%   ########################################### FSM Cambios ############################################
def fsm_cambios_crear(FSM_cambios,i,Layout,rutas_dim):   
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    f = open(FSM_cambios.nombre + "_" + str(i+1) + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ FSM_cambios.nombre + "_" + str(i+1) + ".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f) #Incluir librerias
    
    cambios_dim = []
    FSM_cambios.generico = ["N_RUT","N_SEM"]
    FSM_cambios.dimension_generico = [str(N_rutas),str(N_SEM)]
    FSM_cambios.puertos_in = ["Clock","Reset"]
    FSM_cambios.puertos_out = []   
    FSM_cambios.dimension = ["1"]*2
    
    cambios_dim = convertir_lista_cambios_in(rutas_dim)
    
    crear_puertos_ruta(i,cambios_dim,FSM_cambios.puertos_in,FSM_cambios.dimension,"In","MDC")
    
    #FSM_cambios.dimension += ["N_SEM"]*1
    
    cambios_dim = convertir_lista_cambios_out(rutas_dim)
    
    crear_puertos_ruta(i,cambios_dim,FSM_cambios.puertos_out,FSM_cambios.dimension,"Out","MDC")
    
    FSM_cambios.sentidos = ["in"]*(len(FSM_cambios.puertos_in))+["out"]*(len(FSM_cambios.puertos_out))
    FSM_cambios.tipos = ["std_logic"]*(len(FSM_cambios.puertos_in)+len(FSM_cambios.puertos_out))
     
    FSM_cambios.instancia = "entidad"
    
    crear_objeto_s_i(f,FSM_cambios,i)    
    
    f.write("-- Arquitectura de FSM_cambios_"+str(i+1)+" : Descripcion del comportamiento\n")
    
    f.write("architecture "+FSM_cambios.nombre+ "_" + str(i+1) +"_ARQ of "+FSM_cambios.nombre+"_"+str(i+1)+" is\n")
    f.write("\t"+"begin\n")   
    
    fsm_cambios_proceso(f,i) 
    
    f.write("end architecture "+FSM_cambios.nombre+ "_" + str(i+1) +"_ARQ;\n")   
    
    f.close() #Close header file
    


#%%   ########################################### Enrutador - Proceso ############################################    
def enrutador_crear(enrutador,FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,Layout,rutas_dim,FSM_dim):
        
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    
    
 
    f = open(ENR_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ enrutador.nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
        
    enrutador.generico = ["N","N_SEM","N_PAN","N_MDC","N_RUT"]
    enrutador.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    enrutador.puertos_in = ["Clock","Reset"]
    enrutador.puertos_out = []
    enrutador.dimension = ["1"]*2
    
    crear_puertos_ruta(N_rutas,rutas_dim,enrutador.puertos_in,enrutador.dimension,"In","ENR")
    
    #enrutador.dimension += ["N"]*2
    
    crear_puertos_ruta(N_rutas,FSM_dim,enrutador.puertos_out,enrutador.dimension,"Out","ENR")
      
    
    enrutador.sentidos = ["in"]*(len(enrutador.puertos_in))+["out"]*(len(enrutador.puertos_out))
    enrutador.tipos = ["std_logic"]*(len(enrutador.puertos_in)+len(enrutador.puertos_out))
    
    enrutador.instancia = "entidad"
 
    crear_objeto_s(f,enrutador) 
    
    
    f.write("-- Arquitectura del enrutador : Descripcion del comportamiento\n")
    
    f.write("architecture "+enrutador.nombre+"_ARQ of "+enrutador.nombre+" is\n")
    
    # componente fsm_cambios 
    for i in range(N_rutas):
        FSM_cambios.instancia = "entidad"
        fsm_cambios_crear(FSM_cambios,i,Layout,rutas_dim)
        FSM_cambios.instancia = "componente"
        crear_objeto_s_i(f,FSM_cambios,i)
    
    # componente fsm_barreras
    for i in range(N_rutas):
        FSM_barreras.instancia = "entidad"
        fsm_barreras_crear(FSM_barreras,i,Layout,rutas_dim)
        FSM_barreras.instancia = "componente"
        crear_objeto_s_i(f,FSM_barreras,i)
     
    # componente fsm_semaforo 
    for i in range(N_rutas):
        FSM_semaforos.instancia = "entidad"
        fsm_semaforos_crear(FSM_semaforos,i,Layout,rutas_dim)
        FSM_semaforos.instancia = "componente"
        crear_objeto_s_i(f,FSM_semaforos,i)     

    # componente fsm_rutas 
    for i in range(N_rutas):
        FSM_rutas.instancia = "entidad"
        fsm_rutas_crear(FSM_rutas,i,Layout,rutas_dim)
        FSM_rutas.instancia = "componente"
        crear_objeto_s_i(f,FSM_rutas,i)  


    ENR_aux(f,N_rutas,rutas_dim,FSM_dim)
    
    f.write("\t"+"begin\n")   
    
    
    for i in range(N_rutas):
        ENR_inst_MDC_FSM(f,i,N_rutas)
 
    for i in range(N_rutas):
        ENR_inst_PAN_FSM(f,i,N_rutas)
    
    for i in range(N_rutas):
        ENR_inst_SEM_FSM(f,i,N_rutas)
 
    for i in range(N_rutas):
        ENR_inst_RUT_FSM(f,i,N_rutas)
        
    ENR_conexiones(f,N_rutas)   
    
    #ENR_proceso(f)
    
    f.write("end architecture "+enrutador.nombre+"_ARQ;\n")
    
    f.close() #Close header file