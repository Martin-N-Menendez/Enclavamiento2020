
from VHDL import *

MDC_salida_bloque = "cambios"
MDC_salida_subbloque = "cambio"

PAN_salida_bloque = "pasos_a_nivel"
PAN_salida_subbloque = "paso_a_nivel"

SEM_salida_bloque = "semaforos"
SEM_salida_subbloque = "semaforo"

SEN_bloque = "senialamiento"

#%%   ########################################### Señalamiento - variables auxiliares ############################################ 
def senialamiento_aux(f):
   f.write("\tSignal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);\n")
   f.write("\tSignal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);\n")
   f.write("\tSignal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);\n")
   f.write("\tSignal Reset_sem_s,Reset_Pan_s: std_logic;\r\n") 

#%%   ########################################### señalamiento - conexiones ############################################ 
def senialamiento_conexiones(f):
    
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
    
#%%   ########################################### Semaforos - Instanciación ############################################   
def senialamiento_inst_SEM(f):
    f.write("\tsemaforo_inst : semaforos port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")
    f.write("\t\tRojo_in => Rojo_in_s,\n")
    f.write("\t\tAmarillo_in => Amarillo_in_s,\n")
    f.write("\t\tVerde_in => Verde_in_s,\n")
    f.write("\t\tRojo_out => Rojo_out_s,\n")
    f.write("\t\tAmarillo_out => Amarillo_out_s,\n")
    f.write("\t\tVerde_out => Verde_out_s);\r\n")
    
#%%   ########################################### Pasos a nivel - Instanciación ############################################   
def senialamiento_inst_PAN(f):
    f.write("\tpaso_a_nivel_inst:pasos_a_nivel port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")
    f.write("\t\tAlto_in => Alto_in_s,\n")
    f.write("\t\tBajo_in => Bajo_in_s,\n")
    f.write("\t\tAlto_out => Alto_out_s,\n")
    f.write("\t\tBajo_out => Bajo_out_s);\r\n")
    
#%%   ########################################### Cambios de vias - Instanciación ############################################   
def senialamiento_inst_MDC(f):
    f.write("\tcambio_inst:cambios port map(\n")
    f.write("\t\tClock => Clock,\n")
    f.write("\t\tReset => Reset,\n")
    f.write("\t\tMaquina_normal_in => Maquina_normal_in_s,\n")
    f.write("\t\tMaquina_reversa_in => Maquina_reversa_in_s,\n")
    f.write("\t\tMaquina_normal_out => Maquina_normal_out_s,\n")
    f.write("\t\tMaquina_reversa_out => Maquina_reversa_out_s);\r\n")
    
#%%   ########################################### Señalamiento - Proceso ############################################   
def senialamiento_proceso(f): 
    f.write("\tprocess(Clock,Reset)\n")
    f.write("\tbegin\n")
    f.write("\t\tif (Clock ='1' and Clock'Event and Reset='1') then\n")
    f.write("\t\t\tReset_sem_s <= '0';\n")
    f.write("\t\t\tReset_pan_s <= '0';\n")
    f.write("\t\tend if;\n")
    f.write("\tend process;\n") 
    
#%%   ########################################### Paso a nivel - Proceso ############################################
def paso_a_nivel_proceso(f):   
    
    f.write("\t\t"+"process(Clock,Reset)\n")
    f.write("\t\t"+"begin\n")
    f.write("\t\t\t"+"if Reset='1' then\n")
    f.write("\t\t\t\t"+"Alto_out <= '0';\n")
    f.write("\t\t\t\t"+"Bajo_out <= '0';\n")
    f.write("\t\t\t"+"elsif (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t\t"+"Alto_out <= Alto_in;\n")
    f.write("\t\t\t\t"+"Bajo_out <= Bajo_in;\n")
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end process;\n")

#%%   ########################################### Paso a nivel - Generate ############################################
def paso_a_nivel_generate(f,nombre_i):  
    
    f.write("\t\t"+nombre_i+"_i: for i in 0 to N_PAN-1 generate\n")
    f.write("\t\t\t"+nombre_i+"_inst:"+nombre_i+" port map(\n")
    
    f.write("\t\t\t\t"+"Clock => Clock,\n") 
    f.write("\t\t\t\t"+"Reset => Reset,\n")
    f.write("\t\t\t\t"+"Alto_in => Alto_in(i),\n")
    f.write("\t\t\t\t"+"Bajo_in => Bajo_in(i),\n") 
    f.write("\t\t\t\t"+"Alto_out => Alto_out(i),\n") 
    f.write("\t\t\t\t"+"Bajo_out => Bajo_out(i));\n")
   
    f.write("\t\t"+"end generate;\n")
 
#%%   ########################################### Cambio de via - Proceso ############################################
def cambio_de_via_proceso(f):   
    
    f.write("\t\t"+"process(Clock,Reset)\n")
    f.write("\t\t"+"begin\n")
    f.write("\t\t\t"+"if Reset='1' then\n")
    f.write("\t\t\t\t"+"Maquina_normal_out <= '0';\n")
    f.write("\t\t\t\t"+"Maquina_reversa_out <= '0';\n")
    f.write("\t\t\t"+"elsif (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t\t"+"Maquina_normal_out <= Maquina_normal_in;\n")
    f.write("\t\t\t\t"+"Maquina_reversa_out <= Maquina_reversa_in;\n")
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end process;\n")
    
#%%   ########################################### Cambio de via - Generate ############################################
def cambio_de_via_generate(f,nombre_i):          
    
    f.write("\t\t"+nombre_i+"_i: for i in 0 to N_MDC-1 generate\n")
    f.write("\t\t\t"+nombre_i+"_inst:"+nombre_i+" port map(\n")
    
    f.write("\t\t\t\t"+"Clock => Clock,\n") 
    f.write("\t\t\t\t"+"Reset => Reset,\n")
    f.write("\t\t\t\t"+"Maquina_normal_in => Maquina_normal_in(i),\n")
    f.write("\t\t\t\t"+"Maquina_reversa_in => Maquina_reversa_in(i),\n") 
    f.write("\t\t\t\t"+"Maquina_normal_out => Maquina_normal_out(i),\n") 
    f.write("\t\t\t\t"+"Maquina_reversa_out => Maquina_reversa_out(i));\n")
   
    f.write("\t\t"+"end generate;\n")

#%%   ########################################### Semaforo - Proceso ############################################
def semaforo_proceso(f):   
    
    f.write("\t\t"+"process(Clock,Reset)\n")
    f.write("\t\t"+"begin\n")
    f.write("\t\t\t"+"if Reset='1' then\n")
    f.write("\t\t\t\t"+"Rojo_out <= '0';\n")
    f.write("\t\t\t\t"+"Amarillo_out <= '0';\n")
    f.write("\t\t\t\t"+"Verde_out <= '0';\n")
    f.write("\t\t\t"+"elsif (Clock ='1' and Clock'Event) then\n")
    f.write("\t\t\t\t"+"Rojo_out <= Rojo_in;\n")
    f.write("\t\t\t\t"+"Amarillo_out <= Amarillo_in;\n")
    f.write("\t\t\t\t"+"Verde_out <= Verde_in;\n")
    f.write("\t\t\t"+"end if;\n")
    f.write("\t\t"+"end process;\n")
    
#%%   ########################################### Semaforo - Generate ############################################
def semaforo_generate(f,nombre_i):          
    
    f.write("\t\t"+nombre_i+"_i: for i in 0 to N_SEM-1 generate\n")
    f.write("\t\t\t"+nombre_i+"_inst:"+nombre_i+" port map(\n")
    
    f.write("\t\t\t\t"+"Clock => Clock,\n") 
    f.write("\t\t\t\t"+"Reset => Reset,\n")
    f.write("\t\t\t\t"+"Rojo_in => Rojo_in(i),\n")
    f.write("\t\t\t\t"+"Amarillo_in => Amarillo_in(i),\n") 
    f.write("\t\t\t\t"+"Verde_in => Verde_in(i),\n") 
    f.write("\t\t\t\t"+"Rojo_out => Rojo_out(i),\n") 
    f.write("\t\t\t\t"+"Amarillo_out => Amarillo_out(i),\n") 
    f.write("\t\t\t\t"+"Verde_out => Verde_out(i));\n")
   
    f.write("\t\t"+"end generate;\n")

      
#%%   ########################################### Paso a nivel ############################################
def paso_a_nivel_i(MDc_bloque):    
    nombre_i = PAN_salida_subbloque
    
    f = open(nombre_i + ".vhd", "w")
    
    f.write("-- "+ nombre_i +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n") #Comentario inicial 
    incluir_librerias(f)    #Incluir librerias
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Alto_in","Bajo_in","Alto_out","Bajo_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","1","1","1","1"]
    instancia = "entidad"
    
    crear_objeto(f,nombre_i,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)

    f.write("-- Arquitectura del paso a nivel : Descripcion del comportamiento\n")
    
    f.write("architecture "+nombre_i+"_ARQ of "+nombre_i+" is\n")
    f.write("\t"+"begin\n")   
    
    paso_a_nivel_proceso(f)
    
    f.write("end architecture "+nombre_i+"_ARQ;\n")
    
    f.close() #Close header file  
    
 #%%   ########################################### Pasos a nivel ############################################
def pasos_a_nivel(MDC_bloque,Layout):
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    nombre_i = PAN_salida_subbloque
    nombre = PAN_salida_bloque
    
    f = open(nombre + ".vhd", "w")

    #Comentario inicial
    f.write("-- "+ nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    generico = ["N_PAN"]
    dimension_generico = [str(N_PAN)]
    puertos = ["Clock","Reset","Alto_in","Bajo_in","Alto_out","Bajo_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","N_PAN","N_PAN","N_PAN","N_PAN"]
    instancia = "entidad"
    
    crear_objeto(f,nombre,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)

    f.write("-- Arquitectura de los pasos a nivel : Descripcion del comportamiento\n")
    
    f.write("architecture "+nombre+"_ARQ of "+nombre+" is\n")
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Alto_in","Bajo_in","Alto_out","Bajo_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","1","1","1","1"]
    instancia = "componente"
    
    crear_objeto(f,nombre_i,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)
    
    f.write("\t"+"begin\n")   
    
    paso_a_nivel_generate(f,nombre_i)   
    
    f.write("end architecture "+nombre+"_ARQ;\n")
    
    f.close() #Close header file

#%%   ########################################### Cambio de via ############################################    
def cambio_de_via_i(PAN_bloque):
    
    nombre_i = MDC_salida_subbloque
    
    f = open(nombre_i + ".vhd", "w")

    #Comentario inicial
    f.write("-- "+ nombre_i +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Maquina_normal_in","Maquina_reversa_in","Maquina_normal_out","Maquina_reversa_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","1","1","1","1"]
    instancia = "entidad"
    
    crear_objeto(f,nombre_i,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)

    f.write("-- Arquitectura del cambio ferroviario : Descripcion del comportamiento\n")
    
    f.write("architecture "+nombre_i+"_ARQ of "+nombre_i+" is\n")
    f.write("\t"+"begin\n")   
    
    cambio_de_via_proceso(f)
    
    f.write("end architecture "+nombre_i+"_ARQ;\n")
        
    f.close() #Close header file

#%%   ########################################### Cambios de via ############################################  
def cambios_de_via(PAN_bloque,Layout):
      
    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    nombre_i = MDC_salida_subbloque
    nombre = MDC_salida_bloque
    
    f = open(nombre + ".vhd", "w")

    #Comentario inicial
    f.write("-- "+ nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    generico = ["N_MDC"]
    dimension_generico = [str(N_MDC)]
    puertos = ["Clock","Reset","Maquina_normal_in","Maquina_reversa_in","Maquina_normal_out","Maquina_reversa_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","N_MDC","N_MDC","N_MDC","N_MDC"]
    instancia = "entidad"
    
    crear_objeto(f,nombre,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)

    f.write("-- Arquitectura de los cambios ferroviarios : Descripcion del comportamiento\n")
    
    f.write("architecture "+nombre+"_ARQ of "+nombre+" is\n")
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Maquina_normal_in","Maquina_reversa_in","Maquina_normal_out","Maquina_reversa_out"]
    sentidos = ["in","in","in","in","out","out"]
    tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"]
    dimension = ["1","1","1","1","1","1"]
    instancia = "componente"
    
    crear_objeto(f,nombre_i,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)
    
    f.write("\t"+"begin\n")   
    
    cambio_de_via_generate(f,nombre_i)
    
    f.write("end architecture "+nombre+"_ARQ;\n")
    
    f.close() #Close header file
  
#%%   ########################################### Semaforo ############################################
def semaforo_i(SEM_bloque):
    
    f = open(SEM_bloque.nombre + ".vhd", "w")

    #Comentario inicial
    f.write("-- "+ SEM_bloque.nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n") 
    
    incluir_librerias(f) #Incluir librerias
    
    SEM_bloque.generico = []
    SEM_bloque.dimension_generico = []
    SEM_bloque.puertos_in = ["Clock","Reset","Rojo_in","Amarillo_in","Verde_in"]
    SEM_bloque.puertos_out = ["Rojo_out","Amarillo_out","Verde_out"]
    SEM_bloque.sentidos = ["in","in","in","in","in","out","out","out"]
    SEM_bloque.tipos = ["std_logic","std_logic","std_logic","std_logic","std_logic","std_logic","std_logic","std_logic"] 
    SEM_bloque.dimension = ["1","1","1","1","1","1","1","1"]    
    SEM_bloque.instancia = "entidad"
    
    crear_objeto_s(f,SEM_bloque)
    
    f.write("-- Arquitectura del paso a nivel : Descripcion del comportamiento\n")
    
    f.write("architecture "+SEM_bloque.nombre+"_ARQ of "+SEM_bloque.nombre+" is\n")
    f.write("\t"+"begin\n")   
    
    semaforo_proceso(f) 
    
    f.write("end architecture "+SEM_bloque.nombre+"_ARQ;\n")
    
    f.close() #Close header file

#%%   ########################################### Semaforos ############################################ 
def semaforos(SEM_bloque,Layout):
       
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    SEM_bloque.nombre = SEM_bloque.nombre+'s'
    
    f = open(SEM_bloque.nombre + ".vhd", "w")

    #Comentario inicial
    f.write("-- "+ SEM_bloque.nombre +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    incluir_librerias(f)    #Incluir librerias
    
    SEM_bloque.generico = ["N_SEM"]
    SEM_bloque.dimension_generico = [str(N_SEM)]
    SEM_bloque.dimension = ["1","1","N_SEM","N_SEM","N_SEM","N_SEM","N_SEM","N_SEM"]
    SEM_bloque.instancia = "entidad"
    
    crear_objeto_s(f,SEM_bloque)

    f.write("-- Arquitectura de los "+ SEM_bloque.nombre +" : Descripcion del comportamiento\n")
    
    f.write("architecture "+SEM_bloque.nombre+"_ARQ of "+SEM_bloque.nombre+" is\n")
    
    SEM_bloque.nombre = SEM_bloque.nombre[:-1]
    SEM_bloque.generico = []
    SEM_bloque.dimension_generico = []
    SEM_bloque.tipos = ["std_logic"]*8
    SEM_bloque.dimension = ["1"]*8
    SEM_bloque.instancia = "componente"      
    
    crear_objeto_s(f,SEM_bloque)
    
    f.write("\t"+"begin\n")   
    
    semaforo_generate(f,SEM_bloque.nombre) 
    
    f.write("end architecture "+SEM_bloque.nombre+'s'+"_ARQ;\n")
    
    f.close() #Close header file

#%%    ########################################### Señalamiento ############################################      
def senialamiento_crear(senialamiento,SEM_bloque,PAN_bloque,MDC_bloque,Layout):

    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    semaforo_i(SEM_bloque)
    semaforos(SEM_bloque,Layout)
    paso_a_nivel_i(PAN_bloque)
    pasos_a_nivel(PAN_bloque,Layout)
    cambio_de_via_i(MDC_bloque)
    cambios_de_via(MDC_bloque,Layout)
     
    f = open(SEN_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ SEN_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
      
    add = 5
    senialamiento.generico = ["N_CVS","N_SEM","N_PAN","N_MDC"]
    senialamiento.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC)]
    senialamiento.puertos_in = ["Clock","Reset",
               "Semaforo_rojo_in","Semaforo_amarillo_in","Semaforo_verde_in",
               "Barrera_alta_in","Barrera_baja_in",
               "Maquina_normal_in","Maquina_reversa_in"]
    senialamiento.puertos_out = ["Semaforo_rojo_out","Semaforo_amarillo_out","Semaforo_verde_out",
               "Barrera_alta_out","Barrera_baja_out",
               "Maquina_normal_out","Maquina_reversa_out"]
    senialamiento.sentidos = ["in"]*9+["out"]*7
    senialamiento.tipos = ["std_logic"]*16
    senialamiento.dimension = ["1"]*2+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2+["N_SEM"]*3+["N_PAN"]*2+["N_MDC"]*2
    senialamiento.instancia = "entidad"
    
    crear_objeto_s(f,senialamiento) 
    
    f.write("-- Arquitectura del señalamiento : Descripcion del comportamiento\n")
    
    f.write("architecture "+SEN_bloque+"_ARQ of "+SEN_bloque+" is\n")
    
    SEM_bloque.nombre = SEM_bloque.nombre +'s'
    SEM_bloque.dimension = ["1","1","N_SEM","N_SEM","N_SEM","N_SEM","N_SEM","N_SEM"]
    crear_objeto_s(f,SEM_bloque)
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Alto_in","Bajo_in","Alto_out","Bajo_out"]
    sentidos = ["in"]*4+["out"]*2
    tipos = ["std_logic"]*6
    dimension = ["1"]*2+["N_PAN"]*4
    instancia = "componente"
    
    crear_objeto(f,PAN_salida_bloque,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)
    
    generico = []
    dimension_generico = []
    puertos = ["Clock","Reset","Maquina_normal_in","Maquina_reversa_in","Maquina_normal_out","Maquina_reversa_out"]
    sentidos = ["in"]*4+["out"]*2
    tipos = ["std_logic"]*6
    dimension = ["1"]*2+["N_MDC"]*4
    instancia = "componente"
    
    crear_objeto(f,MDC_salida_bloque,generico,dimension_generico,puertos,sentidos,tipos,dimension,instancia)
    
    senialamiento_aux(f)
    
    f.write("\t"+"begin\n")   
    
    senialamiento_inst_SEM(f)
    senialamiento_inst_PAN(f)
    senialamiento_inst_MDC(f)
    
    senialamiento_conexiones(f)   
    
    senialamiento_proceso(f)
    
    f.write("end architecture "+SEN_bloque+"_ARQ;\n")
    
    f.close() #Close header file
    