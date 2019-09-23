from VHDL import *
from Nodos import *


CAL_bloque = "capa_logica"

NODOS = "nodo"

CFG_bloque = "validador_modo"
RUT_bloque = "validador_rutas"
ERR_bloque = "gestor_de_errores"
UCE_bloque = "unidad_central_enclavamiento"

#%%   ########################################### Capa lógica - variables auxiliares ############################################ 
def Contar_rango(Grafo):
    
    cantidad = 0
    coordenada = []
    
    for i in range(len(Grafo)):
        for j in range(len(Grafo)):
            if Grafo[i][j] == '1':
                cantidad += 1
                coordenada.append([i,j])

    return cantidad,coordenada
#%%   ########################################### Capa lógica - variables auxiliares ############################################ 
def CAL_aux(f,Grafo):
   
    conexiones,coordenada = Contar_rango(Grafo)
    #print("Conexiones : {} | {}".format(conexiones,coordenada))
    
    aux = "";
    for i in range(conexiones):
        #print("{}".format(coordenada[i]))
        aux += "conector_"+str(coordenada[i][0])+"a"+str(coordenada[i][1])
        if i < conexiones-1:
            aux += " , "
    
    print("{}".format(aux))
    
    f.write("\tSignal "+aux+" : std_logic;\r\n")

#%%   ########################################### RUT_FSM - Instanciación ############################################     
def CAL_inst_NODOS(f,i,N,Grafo):
    
    f.write("\t"+NODOS+"_inst_"+str(i+1)+":"+NODOS+"_"+str(i+1)+"\n")
    f.write("\t\tport map(\n")
    f.write("\t\t\tClock => Clock,\n")
    
    
    conexiones,coordenada = Contar_rango(Grafo)
    
    for j in range(conexiones):
        if i in coordenada[j]:
            print("{} en <{}>".format(i,coordenada[j]))
            if i == coordenada[j][0]:
                #print("{} en <{}>".format(i,coordenada[j][0]))
                f.write("\t\t\tPosterior => wires("+str(i+1)+"),\n")
            if i == coordenada[j][1]:
                #print("{} en <{}>".format(i,coordenada[j][0]))
                f.write("\t\t\tAnterior => wires("+str(i)+"),\n")
     
    if i == 0:
        f.write("\t\t\tAnterior => wires(0),\n")     
         
    #f.write("\t\t\tAnterior => Clock,\n")
    #f.write("\t\t\tPosterior => Clock,\n")
    f.write("\t\t\tDesvio => Clock,\n")
    ##auto_conector_mdc(f,i,N,"In")
    
    ##auto_conector_mdc(f,i,N,"Out")
    
    f.write("\t\t\tReset => Reset\n")
    f.write("\t\t);\r\n")

#%%   ########################################### Capa lógica - conexiones ############################################ 
def CAL_conexiones(f):
    
    f.write("\r\tRojo_in_s <= Semaforo_rojo_in;\n")
    #f.write("\tAmarillo_in_s <= Semaforo_amarillo_in;\n")
    #f.write("\tVerde_in_s <= Semaforo_verde_in;\n")
    #f.write("\tSemaforo_rojo_out <= Rojo_out_s;\n")
    #f.write("\tSemaforo_amarillo_out <= Amarillo_out_s;\n")
    #f.write("\tSemaforo_verde_out <= Verde_out_s;\n")
    #f.write("\tAlto_in_s <= Barrera_alta_in;\n")
    #f.write("\tBajo_in_s <= Barrera_baja_in;\n")
    #f.write("\tBarrera_alta_out <= Alto_out_s;\n")
    #f.write("\tBarrera_baja_out <= Bajo_out_s;\n")
    #f.write("\tMaquina_normal_in_s <= Maquina_normal_in;\n")
    #f.write("\tMaquina_reversa_in_s <= Maquina_reversa_in;\n")
    #f.write("\tMaquina_normal_out <= Maquina_normal_out_s;\n")
    f.write("\tMaquina_reversa_out <= Maquina_reversa_out_s;\r\n")

#%%   ########################################### Unidad Central de Enclavamiento - Proceso ############################################
def CAL_proceso(f):   
    
    f.write("\t"+"process(Clock,Reset)\n")
    f.write("\t"+"begin\n")
    f.write("\t\t"+"if (Clock ='1' and Clock'Event and Reset='1') then\n")
    f.write("\t\t\t"+"Reset_sem_s <= '0';\n")
    f.write("\t\t\t"+"Reset_pan_s <= '0';\n")
    f.write("\t\t"+"end if;\n")
    f.write("\t"+"end process;\r\n")    
    
    
#%%    ########################################### Capa logica ############################################      
def capa_logica_crear(capa_logica,conectores,nodos,Layout,Grafo):

    
    N_rutas = Layout[0]
    N_CVS   = Layout[1]
    N_MDC   = Layout[2]
    N_PAN   = Layout[3]
    N_SEM   = Layout[4]
    
    #red_nodos(nodos,enmascarador,enrutador,mediador,senialamiento,
    #          FSM_rutas,FSM_semaforos,FSM_barreras,FSM_cambios,
    #          SEM_bloque,PAN_bloque,MDC_bloque,Layout,rutas_dim,FSM_dim)

    f = open(CAL_bloque + ".vhd", "w")
    
    #Comentario inicial
    f.write("-- "+ CAL_bloque +".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n")
    
    #Incluir librerias
    incluir_librerias(f)
    
    # Entidad capa_logica
    capa_logica.generico = ["N_CVS","N_SEM","N_PAN","N_MDC","N_RUT"]
    capa_logica.dimension_generico = [str(N_CVS),str(N_SEM),str(N_PAN),str(N_MDC),str(N_rutas)]
    
    capa_logica.puertos_in = ["Clock","Reset","Modo","Ruta_in","Circuitos_de_via"]
    capa_logica.puertos_out = ["Semaforo_out","Barrera_out","Maquina_out"]
    capa_logica.sentidos = ["in"]*5+["out"]*3
    capa_logica.tipos = ["std_logic"]*8
    capa_logica.dimension = ["1"]*2+["N_RUT"]*2+["N_CVS"]*1+["N_SEM"]*1+["N_PAN"]*1+["N_MDC"]*1
    
    capa_logica.instancia = "entidad"
    
    crear_objeto_s(f,capa_logica)
    
    f.write("-- Arquitectura de la "+CAL_bloque+": Descripcion del comportamiento\n")
    
    f.write("architecture "+CAL_bloque+"_ARQ of "+CAL_bloque+" is\n")
    
    
    # componente nodoss 
    for i in range(N_rutas):
        nodos.instancia = "entidad"
        nodos_crear(nodos,i,Layout)
        nodos.instancia = "componente"
        crear_objeto_s_i(f,nodos,i)
    
    
    CAL_aux(f,Grafo)
    
    
    f.write("\tSignal wires : std_logic_vector(10 downto 0);\r\n")
    
    f.write("\t"+"begin\r\n")   
    
    f.write("\twires(0) <= Clock;\r\n")
    
    for i in range(N_rutas):
        CAL_inst_NODOS(f,i,N_rutas,Grafo)
    
    #CAL_conexiones(f)   
    
    #CAL_proceso(f)
    
    f.write("end architecture "+CAL_bloque+"_ARQ;\n")
    
    f.close() #Close header file
    
    
    