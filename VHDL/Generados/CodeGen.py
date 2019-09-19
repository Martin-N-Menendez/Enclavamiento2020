
import csv
from Senialamiento import *
from Nodos import *
from Capa_logica import *
from VHDL import *
from Conectores import *


#%%
        
class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.generico = []
        self.generico_dim = []
        self.puertos_in = []
        self.puertos_out = []
        self.sentidos = []
        self.tipos = []
        self.dimension = []
        self.instancia = []
        self.cantidad = 0
#%%
CAL_bloque = "capa_logica"

conectores_estructura = "conector"
nodos_estructura = "nodo"

ENM_bloque = "enmascarador"
ENR_bloque = "enrutador"
MED_bloque = "mediador"
SEN_bloque = "senialamiento"

RUT_FSM = "rut_fsm"
SEM_FSM = "sem_fsm"
PAN_FSM = "pan_fsm"
MDC_FSM = "mdc_fsm"

SEM_salida_bloque = "semaforo"

PAN_salida_bloque = "barreras"
PAN_salida_subbloque = "barrera"

MDC_salida_bloque = "cambios"
MDC_salida_subbloque = "cambio"

#%%
capa_logica = Modulo(CAL_bloque)
conectores = Modulo(conectores_estructura)
nodos = Modulo(nodos_estructura)

enmascarador = Modulo(ENM_bloque)
enrutador = Modulo(ENR_bloque)
mediador = Modulo(MED_bloque)
senialamiento = Modulo(SEN_bloque)

FSM_rutas = Modulo(RUT_FSM)
FSM_semaforos = Modulo(SEM_FSM)
FSM_barreras = Modulo(PAN_FSM)
FSM_cambios = Modulo(MDC_FSM)

SEM_bloque = Modulo("semaforo")
#SEM_subbloque = Modulo("semaforo")
PAN_bloque = Modulo("barreras")
PAN_subbloque = Modulo("barrera")
MDC_bloque = Modulo("cambios")
MDc_subbloque = Modulo("cambio")

#%%
def RAILIB_CODEGEN_Translator(table_name, name, lang):

    f = open(table_name,"r")

    if(lang=="VHDL"):
        RAILIB_CODEGEN_VHDL(f,name)
    else:
        return 0

    return 1

    

    
#%%
def RAILIB_CODEGEN_VHDL(file,name):

    ########################################### RELEVANT VARIABLES ############################################
    
    # Number of devices of every type
    routes_num = 13 
   
    tracks_num = 14
    switches_num = 1
    crossings_num = 3
    signals_num = 13

     
    linenum = 0     #Line number
    rt_flag = 0     # Route Table flag   
    ct_flag = 0     #Crossings Table flag
    cnt = 0         #Auxiliary counter

    #Actual device under analysis
    route = 0
    signal = 0

    
    N_RUT   = 3
    N_CVS   = 3
    N_MDC   = 2
    N_PAN   = 1
    N_SEM   = N_RUT
    
    Layout = [N_RUT, N_CVS, N_MDC, N_PAN, N_SEM]
    
    
    Grafo =    [
                ['0','1','0'],
                ['0','0','1'],
                ['0','0','0'],
                ]
    
    
    capa_logica_crear(capa_logica,conectores,nodos,Layout,Grafo)
    
    








    #%%
    #Create source file
    fc = open("IXL_"+name+".vhd","w")

    #Write source's header
    fc.write("-- IXL_"+name+".vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB\r\n"+
             "library IEEE;\n"+
             "use IEEE.std_logic_1164.all;\n"+
             "use IEEE.numeric_std.all;\r\n")
             
    #fc.write("--Sistema central de enclavamiento\n"+"RAILIB_ENCLAVAMIENTO_t IXL_"+name+"_ixl;\n")

    # Use CSV parsing to transform the tsv file to a table
    table = csv.reader(file,delimiter='\t')

    #For every row
    for row in table:

        linenum = linenum + 1

        # Search system size commands until a Route Table mark appears ("rt")
        if(rt_flag == 0):

            #Break the first row component
            components = row[0].split(',')

            #Compare the first string with the size commands
            if (components[0] == "tr"):
                tracks_num = int(components[1])
            elif (components[0] == "si"):
                signals_num = int(components[1])
            elif (components[0] == "sw"):
                switches_num = int(components[1])
            elif (components[0] == "cr"):
                crossings_num = int(components[1])
            elif (components[0] == "ro"):
                routes_num = int(components[1])

            #Until the RT mark shows
            elif (components[0] == "rt"):

                rt_flag = 1

                print("Tabla de rutas detectada en linea ",linenum,"\n")

                print("SECCIONES DE VIA : \t\t",tracks_num)
                fc.write("\n --SECCIONES DE VIA"+
                         "\n#define IXL_"+name+"_TR_NUM " + str(tracks_num) + "\n"+
                         "RAILIB_TRACK_t IXL_"+name+"_tracks[IXL_"+name+"_TR_NUM];\n")

                print("SEÑALES : \t\t\t",signals_num)
                fc.write("\n --SEÑALES" +
                         "\n#define IXL_" + name + "_SI_NUM " + str(signals_num) + "\n" +
                         "RAILIB_SIGNAL_t IXL_" + name + "_signals[IXL_" + name + "_SI_NUM];\n")


                print("CAMBIOS DE VIAS : \t\t",switches_num)
                fc.write("\n --CAMBIOS DE VIAS" +
                         "\n#define IXL_" + name + "_SW_NUM " + str(switches_num) + "\n" +
                         "RAILIB_SWITCH_t IXL_" + name + "_switches[IXL_" + name + "_SW_NUM];\n")


                print("PASOS A NIVEL : \t\t",crossings_num)
                fc.write("\n --PASOS A NIVEL" +
                         "\n#define IXL_" + name + "_CR_NUM " + str(crossings_num) + "\n" +
                         "RAILIB_CROSSING_t IXL_" + name + "_crossings[IXL_" + name + "_CR_NUM];\n")


                print("RUTAS : \t\t\t",routes_num)
                fc.write("\n --RUTAS" +
                         "\n#define IXL_" + name + "_RO_NUM " + str(routes_num) + "\n" +
                         "RAILIB_ROUTE_t IXL_" + name + "_routes[IXL_" + name + "_RO_NUM];\n")

                if(tracks_num == 0):
                    print("\n ADVERTENCIA : NO HAY CIRCUITOS DE VIA DEFINIDOS\n")
                if (signals_num == 0):
                    print("\n ADVERTENCIA : NO HAY SEÑALES DEFINIDAS\n")
                if (switches_num == 0):
                    print("\n ADVERTENCIA : NO HAY CAMBIOS DEVIAS DEFINIDOS\n")
                if (crossings_num == 0):
                    print("\n ADVERTENCIA : NO PASOS A NIVEL DEFINIDOS\n")
                if (routes_num == 0):
                    print("\n ADVERTENCIA : NO HAY RUTAS DEFINIDAS\n")

            else:
                print("LINEA ",linenum," : ORDEN NO DEFINIDA\n")
                return

        elif(ct_flag == 0):

            # Build route connections
            index = 0

            #Read route number (as string)
            route = row[index]
            if(route == "ct"):
                ct_flag = 1
                print("\nTabla de pasos a nivel detectada en linea ", linenum, "\n")
            else:
                if(int(route) > routes_num):
                    print("Linea ",linenum," : Numero de ruta "+route+" Excede la dimensión máxima\n")
                    return
                fc.write("\n --Ruta " + route + " Parametros")
                index = index + 1

                #Read internal tracks
                fc.write("\n RAILIB_TRACK_t* IXL_"+name+"_r"+route+"_itracks[] = {")
                cnt = 0
                if(row[index]!="/"):
                    for comp in row[index].split(',') :
                        it = int(comp)
                        cnt = cnt + 1
                        if(it>tracks_num):
                            print("Linea ",linenum," : Numero de circuito de via ",it," Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_"+name+"_tracks+"+str(it-1)+" ,")
                    fc.seek(fc.tell()-2)
                fc.write("};\n")
                fc.write("#define IXL_"+name+"_r"+route+"_itracks_num "+str(cnt)+"\n")
                index = index + 1


                #Read signal
                signal = row[index]
                if (int(signal) > signals_num):
                    print("Linea ", linenum, " : Numero de señal " + signal + " Excede la dimensión máxima\n")
                    return
                fc.write("\n#define IXL_"+name+"_r"+route+"_signal (IXL_"+name+"_signals+"+str(int(signal)-1)+")\n")
                index = index + 1

                # Read danger track sections
                fc.write("\nRAILIB_TRACK_t* IXL_" + name + "_r" + route + "_dtracks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > tracks_num):
                            print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_dtracks_num " + str(cnt) + "\n")
                index = index + 1

                # Read caution track sections
                fc.write("\n RAILIB_TRACK_t* IXL_" + name + "_r" + route + "_ctracks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > tracks_num):
                            print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_ctracks_num " + str(cnt) + "\n")
                index = index + 1

                # Read permanent overlap track sections
                fc.write("\n RAILIB_TRACK_t* IXL_" + name + "_r" + route + "_otracks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > tracks_num):
                            print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_otracks_num " + str(cnt) + "\n")
                index = index + 1

                # Read temporized overlap track sections
                fc.write("\n RAILIB_TRACK_t* IXL_" + name + "_r" + route + "_ottracks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > tracks_num):
                            print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_ottracks_num " + str(cnt) + "\n")
                index = index + 1

                # Read overlap delays and create overlap timers
                if (row[index] != "/"):
                    fc.write("\nuint32_t IXL_" + name + "_r"+ route +"_overdelays[] = {"+row[index]+"};\n")
                    fc.write("\nuint32_t IXL_" + name + "_r"+ route +
                             "_overtimers[IXL_" + name + "_r"+ route +"_ottracks_num] = {0};\n")
                else:
                    fc.write("\nuint32_t IXL_" + name + "_r" + route + "_overdelays[] = {};\n")
                    fc.write("\nuint32_t IXL_" + name + "_r" + route + "_overtimers[] = {};\n")
                index = index + 1

                # Read proximity track sections
                fc.write("\nRAILIB_TRACK_t* IXL_" + name + "_r" + route + "_ptracks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > tracks_num):
                            print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_ptracks_num " + str(cnt) + "\n")
                index = index + 1

                # Read conflictive routes
                fc.write("\n RAILIB_ROUTE_t* IXL_" + name + "_r" + route + "_croutes[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > routes_num):
                            print("Linea ", linenum, " : Ruta ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_routes+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_croutes_num " + str(cnt) + "\n")
                index = index + 1

                # Read cancellation blocking routes
                fc.write("\n RAILIB_ROUTE_t* IXL_" + name + "_r" + route + "_cbroutes[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > routes_num):
                            print("Linea ", linenum, " : Ruta ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_routes+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_cbroutes_num " + str(cnt) + "\n")
                index = index + 1

                # Read cancellation delays
                if (row[index] != "/"):
                    fc.write("\nuint32_t IXL_" + name + "_r" + route + "_cancdelays[] = {" + row[index] + "};\n")
                else:
                    fc.write("\nuint32_t IXL_" + name + "_r" + route + "_cancdelays[] = {};\n")
                index = index + 1

                # Read normal switches
                fc.write("\n RAILIB_SWITCH_t* IXL_" + name + "_r" + route + "_nswitches[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > switches_num):
                            print("Linea ", linenum, " : Cambio de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_switches+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_nswitches_num " + str(cnt) + "\n")
                index = index + 1

                # Read normal switches
                fc.write("\nRAILIB_SWITCH_t* IXL_" + name + "_r" + route + "_rswitches[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > switches_num):
                            print("Linea ", linenum, " : Cambio de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_switches+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_rswitches_num " + str(cnt) + "\n")
                index = index + 1

                # Read crossing locks
                fc.write("\nRAILIB_CROSSING_t* IXL_" + name + "_r" + route + "_crosslocks[] = {")
                cnt = 0
                if (row[index] != "/"):
                    for comp in row[index].split(','):
                        it = int(comp)
                        cnt = cnt + 1
                        if (it > crossings_num):
                            print("Linea ", linenum, " : Cambio de via ", it, " Excede la dimensión máxima\n")
                            return
                        else:
                            fc.write("IXL_" + name + "_crossings+" + str(it - 1) + " ,")
                    fc.seek(fc.tell() - 2)
                fc.write("};\n")
                fc.write("#define IXL_" + name + "_r" + route + "_crosslocks_num " + str(cnt) + "\n")
                index = index + 1

        else:

            # Read crossing number (as string)
            crossing = row[index]
            if (int(crossing) > crossings_num):
                print("Linea ", linenum, " : Numero de Paso a nivel " + crossing + " Excede la dimensión máxima\n")
                return
            fc.write("\n -- Paso a nivel " + crossing + " Parametros")
            index = index + 1

            # Read permanent announcement track sections
            fc.write("\nRAILIB_TRACK_t* IXL_" + name + "_c" + crossing + "_atracks[] = {")
            cnt = 0
            if (row[index] != "/"):
                for comp in row[index].split(','):
                    it = int(comp)
                    cnt = cnt + 1
                    if (it > tracks_num):
                        print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                        return
                    else:
                        fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                fc.seek(fc.tell() - 2)
            fc.write("};\n")
            fc.write("#define IXL_" + name + "_c" + crossing + "_atracks_num " + str(cnt) + "\n")
            index = index + 1

            # Read temporized announcement track sections
            fc.write("\nRAILIB_TRACK_t* IXL_" + name + "_c" + crossing + "_tatracks[] = {")
            cnt = 0
            if (row[index] != "/"):
                for comp in row[index].split(','):
                    it = int(comp)
                    cnt = cnt + 1
                    if (it > tracks_num):
                        print("Linea ", linenum, " : Numero de circuito de via ", it, " Excede la dimensión máxima\n")
                        return
                    else:
                        fc.write("IXL_" + name + "_tracks+" + str(it - 1) + " ,")
                fc.seek(fc.tell() - 2)
            fc.write("};\n")
            fc.write("#define IXL_" + name + "_c" + crossing + "_tatracks_num " + str(cnt) + "\n")
            index = index + 1

            # Read announcement delays and create associated timers
            if (row[index] != "/"):
                fc.write("\nuint32_t IXL_" + name + "_c" + crossing + "_anndelays[] = {" + row[index] + "};\n")
                fc.write("\nuint32_t IXL_" + name + "_c" + crossing +
                         "_anntimers[IXL_" + name + "_c" + crossing + "_tatracks_num] = {0};\n")
            else:
                fc.write("\nuint32_t IXL_" + name + "_c" + crossing + "_anndelays[] = {};\n")
                fc.write("\nuint32_t IXL_" + name + "_c" + crossing + "_anntimers[] = {};\n")


     #Write the rest of the source file

    
    #%%  Init function
    fc.write("\nvoid IXL_"+name+"_Init(){\n")

    # Main interlocking block
    fc.write("\n\t --Creacion del enclavamiento")
    fc.write("\n\tRAILIB_INTERLOCKING_Create(&IXL_"+name+"_ixl,0);")
    fc.write("\n\tRAILIB_INTERLOCKING_Add(&IXL_"+name+"_ixl,IXL_SIGNALS,IXL_"+name+"_signals,IXL_"+name+"_SI_NUM);")
    fc.write("\n\tRAILIB_INTERLOCKING_Add(&IXL_"+name+"_ixl,IXL_ROUTES,IXL_"+name+"_routes,IXL_"+name+"_RO_NUM);")
    fc.write("\n\tRAILIB_INTERLOCKING_Add(&IXL_"+name+"_ixl,IXL_SWITCHES,IXL_"+name+"_switches,IXL_"+name+"_SW_NUM);")
    fc.write("\n\tRAILIB_INTERLOCKING_Add(&IXL_"+name+"_ixl,IXL_CROSSINGS,IXL_"+name+"_crossings,IXL_"+name+"_CR_NUM);")
    fc.write("\n\tRAILIB_INTERLOCKING_Add(&IXL_"+name+"_ixl,IXL_TRACKS,IXL_"+name+"_tracks,IXL_"+name+"_TR_NUM);")
    fc.write("\n\tRAILIB_INTERLOCKING_Init(&IXL_"+name+"_ixl);")

    # Routes connection
    for i in range(routes_num):
        fc.write( "\n\n\t -- Ruta "+str(i+1)+" (conexiones)");
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",INTERNAL_TRACKS,IXL_"+name+"_r"+str(i+1)+"_itracks,IXL_"+name+"_r"+str(i+1)+"_itracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",ROUTE_SIGNAL,IXL_"+name+"_r"+str(i+1)+"_signal,1);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",NORMAL_SWITCHES,IXL_"+name+"_r"+str(i+1)+"_nswitches,IXL_"+name+"_r"+str(i+1)+"_nswitches_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",REVERSE_SWITCHES,IXL_"+name+"_r"+str(i+1)+"_rswitches,IXL_"+name+"_r"+str(i+1)+"_rswitches_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",CAUTION_TRACKS,IXL_"+name+"_r"+str(i+1)+"_ctracks,IXL_"+name+"_r"+str(i+1)+"_ctracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",DANGER_TRACKS,IXL_"+name+"_r"+str(i+1)+"_dtracks,IXL_"+name+"_r"+str(i+1)+"_dtracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",PROXIMITY_TRACKS,IXL_"+name+"_r"+str(i+1)+"_ptracks,IXL_"+name+"_r"+str(i+1)+"_ptracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",OVERLAP_TRACKS,IXL_"+name+"_r"+str(i+1)+"_otracks,IXL_"+name+"_r"+str(i+1)+"_otracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",OVER_TEMP_TRACKS,IXL_"+name+"_r"+str(i+1)+"_ottracks,IXL_"+name+"_r"+str(i+1)+"_ottracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",OVERLAP_TIMINGS,IXL_"+name+"_r"+str(i+1)+"_overdelays,IXL_"+name+"_r"+str(i+1)+"_ottracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",INHIBIT_ROUTES,IXL_"+name+"_r"+str(i+1)+"_croutes,IXL_"+name+"_r"+str(i+1)+"_croutes_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",CANC_PROX_ROUTES,IXL_"+name+"_r"+str(i+1)+"_cbroutes,IXL_"+name+"_r"+str(i+1)+"_cbroutes_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",CANC_PROX_TIMES,IXL_"+name+"_r"+str(i+1)+"_cancdelays,IXL_"+name+"_r"+str(i+1)+"_cbroutes_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",OVERLAP_TIMERS,IXL_"+name+"_r"+str(i+1)+"_overtimers,IXL_"+name+"_r"+str(i+1)+"_ottracks_num);")
        fc.write( "\n\tRAILIB_ROUTE_Connect(IXL_"+name+
                  "_routes+"+str(i)+",CROSSING_LOCKS,IXL_"+name+"_r"+str(i+1)+"_crosslocks,IXL_"+name+"_r"+str(i+1)+"_crosslocks_num);")
        
    #Crossings connection
    for i in range(crossings_num):
        fc.write("\n\n\t -- Paso a nivel "+str(i+1)+" (conexiones)");
        fc.write("\n\tRAILIB_CROSSING_Connect(IXL_"+name+"_crossings+"+str(i)+
                 ",ANNOUNCEMENT_TRACKS,IXL_"+name+"_c"+str(i+1)+"_atracks,IXL_"+name+"_c"+str(i+1)+"_atracks_num);")
        fc.write("\n\tRAILIB_CROSSING_Connect(IXL_"+name+"_crossings+"+str(i)+
                 ",TEMP_ANNOUNCEMENT_TRACKS,IXL_"+name+"_c"+str(i+1)+"_tatracks,IXL_"+name+"_c"+str(i+1)+"_tatracks_num);")
        fc.write("\n\tRAILIB_CROSSING_Connect(IXL_"+name+"_crossings+"+str(i)+
                 ",ANNOUNCEMENT_TIMINGS,IXL_"+name+"_c"+str(i+1)+"_anndelays,IXL_"+name+"_c"+str(i+1)+"_tatracks_num);")
        fc.write("\n\tRAILIB_CROSSING_Connect(IXL_"+name+"_crossings+"+str(i)+
                 ",ANNOUNCEMENT_TIMERS,IXL_"+name+"_c"+str(i+1)+"_anntimers,IXL_"+name+"_c"+str(i+1)+"_tatracks_num);")
        
    # End of Init function
    fc.write("\n\n}\n\n")
    
    #Other functions
    fc.write("RAILIB_TRACK_STATE_t IXL_"+name+"_GetTrackState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_TR_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_TRACK_GetState(IXL_"+name+"_tracks + index-1);\n\t}\n}\n\n")

    fc.write("RAILIB_SIGNAL_ASPECT_t IXL_"+name+"_GetSignalState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_SI_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_SIGNAL_GetAspect(IXL_"+name+"_signals + index-1);\n\t}\n}\n\n")

    fc.write("RAILIB_CROSSING_STATE_t IXL_"+name+"_GetCrossingState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_CR_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_CROSSING_GetState(IXL_"+name+"_crossings + index-1);\n\t}\n}\n\n")

    fc.write("RAILIB_SWITCH_STATE_t IXL_"+name+"_GetSwitchState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_SW_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_SWITCH_GetState(IXL_"+name+"_switches + index-1);\n\t}\n}\n\n")

    fc.write("RAILIB_SWITCH_STATE_t IXL_"+name+"_GetSwitchReqState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_SW_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_SWITCH_GetReqState(IXL_"+name+"_switches + index-1);\n\t}\n}\n\n")

    fc.write("RAILIB_ROUTE_STATUS_t IXL_"+name+"_GetRouteState(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_ROUTE_GetStatus(IXL_"+name+"_routes + index-1);\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_SetTrackState(uint32_t index, RAILIB_TRACK_STATE_t state){\n\
                    \n\tif(index>IXL_"+name+"_TR_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_TRACK_SetState(IXL_"+name+"_tracks + index-1,state);\
                    \n\treturn 1;\n\n\t}\n}\n")

    fc.write("uint32_t IXL_"+name+"_RequestRoute(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\treturn RAILIB_ROUTE_Request(IXL_"+name+"_routes + index-1);\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_ReqRouteSwitches(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_ROUTE_ReqSwitches(IXL_"+name+"_routes + index-1);\
                    \n\t\treturn 1;\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_ReqRouteCrossings(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_ROUTE_ReqCrossings(IXL_"+name+"_routes + index-1);\
                    \n\t\treturn 1;\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_CancelRoute(uint32_t index){\n\
                    \n\tif(index>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_ROUTE_CancelRequest(IXL_"+name+"_routes + index-1);\
                    \n\t\treturn 1;\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_Update(){\
                    \n\tRAILIB_INTERLOCKING_Update(&IXL_"+name+"_ixl);\n\treturn 1;\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_UpdateTimers(){\
                    \n\tRAILIB_INTERLOCKING_UpdateTimers(&IXL_"+name+"_ixl);\n\treturn 1;\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_SetOpMode(RAILIB_ROUTE_OPMODE_t mode){\
                    \n\tRAILIB_INTERLOCKING_SetOpmode(&IXL_"+name+"_ixl, mode);\n\treturn 1;\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_SetOpModeLocal(RAILIB_ROUTE_OPMODE_t mode, uint32_t route){\n\
                    \n\tif(route>IXL_"+name+"_RO_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_INTERLOCKING_SetLocalOpmode(&IXL_"+name+"_ixl,mode,route-1);\
                    \n\t\treturn 1;\n\t}\n}\n\n")

    fc.write("uint32_t IXL_"+name+"_GetDeviceNum(RAILIB_INTERLOCKING_DEVICES_t type){\
                    \n\tswitch(type){\
                    \n\t\tcase IXL_ROUTES :\
                    \n\t\t\treturn IXL_"+name+"_RO_NUM;\
                    \n\t\tbreak;\
                    \n\t\tcase IXL_SIGNALS :\
                    \n\t\t\treturn IXL_"+name+"_SI_NUM;\
                    \n\t\tbreak;\
                    \n\t\tcase IXL_TRACKS :\
                    \n\t\t\treturn IXL_"+name+"_TR_NUM;\
                    \n\t\tbreak;\
                    \n\t\tcase IXL_SWITCHES :\
                    \n\t\t\treturn IXL_"+name+"_SW_NUM;\
                    \n\t\tbreak;\
                    \n\t\tcase IXL_CROSSINGS :\
                    \n\t\t\treturn IXL_"+name+"_CR_NUM;\
                    \n\t\tbreak;\
                    \n\t\tdefault :\
                    \n\t\t\treturn -1;\
                    \n\t\tbreak;\
                    \n\t}\
                    \n}\n\n")

    fc.write("uint32_t IXL_"+name+"_SetSignalType(uint32_t index, RAILIB_SIGNAL_TYPE_t type){\n\
                    \n\tif(index>IXL_"+name+"_SI_NUM){\
                    \n\t\treturn -1;\
                    \n\t}else{\
                    \n\t\tRAILIB_SIGNAL_SetType(IXL_"+name+"_signals + index-1,type);\
                    \n\t\treturn 1;\n\t}\n\treturn 1;\n}\n\n")

    # Close source file
    fc.close()
    ############################################## CLOSE FILES ################################################


#Test
RAILIB_CODEGEN_Translator("TEST.txt","TEST","VHDL")

##
#   @}
#