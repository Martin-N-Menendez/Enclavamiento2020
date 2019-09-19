# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:13:30 2019

@author: jinnkay
"""
import numpy as np

#%%
def convertir_lista_cambios_in(rutas_dim):
    
    cambios_dim = []
    
    for i in range(len(rutas_dim)):
            cambios_dim.append(rutas_dim[i][16:19])
            
    return cambios_dim

#%%
def convertir_lista_barreras_in(rutas_dim):
    
    barreras_dim = []
    
    for i in range(len(rutas_dim)):
            barreras_dim.append(rutas_dim[i][19:23])
            
    return barreras_dim

#%%
def convertir_lista_semaforos_in(rutas_dim):
    
    semaforos_dim = []
    
    for i in range(len(rutas_dim)):
            semaforos_dim.append(rutas_dim[i][16:17])
            
    return semaforos_dim

#%%
def convertir_lista_ruta_in(rutas_dim):
    
    ruta_dim = []
    
    for i in range(len(rutas_dim)):
            ruta_dim.append(rutas_dim[i][0:16])
            
    return ruta_dim

#%%
def convertir_lista_cambios_out(FSM_dim):
    
    cambios_dim = []
    
    for i in range(len(FSM_dim)):
            cambios_dim.append(FSM_dim[i][4:8])
            
    return cambios_dim

#%%
def convertir_lista_barreras_out(FSM_dim):
    
    barreras_dim = []
    
    for i in range(len(FSM_dim)):
            barreras_dim.append(FSM_dim[i][8:12])
            
    return barreras_dim

#%%
def convertir_lista_semaforos_out(FSM_dim):
    
    semaforos_dim = []
    
    for i in range(len(FSM_dim)):
            semaforos_dim.append(FSM_dim[i][0:4])
            
    return semaforos_dim

#%%
def convertir_lista_ruta_out(FSM_dim):
    
    ruta_dim = []
    
    for i in range(len(FSM_dim)):
            ruta_dim.append(FSM_dim[i][12:15])
            
    return ruta_dim
#%%
def enumerar_entradas_rutas():
        
    conector_1 = "CV_int_"+                 "Ruta_"
    conector_2 = "CV_paralelo_"+            "Ruta_"
    conector_3 = "CV_paralelo_temp_"+       "Ruta_"
    conector_4 = "CV_despeje_"+             "Ruta_"
    conector_5 = "CV_aprox_"+               "Ruta_"
    conector_6 = "Estado_sub_ruta_"+        "Ruta_"
    conector_7 = "Estado_ruta_cond_"+       "Ruta_"
    conector_8 = "Estado_ruta_confl_"+      "Ruta_"
    conector_9 = "Estado_SEM_sgte_"+        "Ruta_"
    conector_10 = "Pos_MDC_ruta_"+          "Ruta_"
    conector_11 = "Pos_MDC_aprox_"+         "Ruta_"
    conector_12 = "Pos_MDC_despeje_"+       "Ruta_"
    conector_13 = "Pos_MDC_solape_"+        "Ruta_"
    conector_14 = "Bloq_MDC_ruta_"+         "Ruta_"
    conector_15 = "Bloq_MDC_solape_"+       "Ruta_"
    conector_16 = "Estado_PAN_"+            "Ruta_"
    conector_17 = "Estado_CV_bloq_"+        "Ruta_"
    conector_18 = "Estado_ruta_bloq_"+      "Ruta_"
    conector_19 = "MDC_bloq_temp_solape_"+  "Ruta_"
    conector_20 = "Estado_ruta_"+           "Ruta_"
    conector_21 = "CV_alarma_total_"+       "Ruta_"
    conector_22 = "CV_alarma_inmediata_"+   "Ruta_"
    conector_23 = "PAN_bloq_temp_solape_"+  "Ruta_"
    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4,
             conector_5, conector_6, conector_7, conector_8,
             conector_9, conector_10, conector_11, conector_12,
             conector_13, conector_14, conector_15, conector_16, 
             conector_17, conector_18, conector_19, conector_20,
             conector_21, conector_22, conector_23                   
            ]    
        
    return conector

#%%
def enumerar_entradas_mdc():
        
    conector_1 = "Estado_CV_bloq_"+        "Ruta_"
    conector_2 = "Estado_ruta_bloq_"+      "Ruta_"
    conector_3 = "MDC_bloq_temp_solape_"+  "Ruta_"

    
    conector = [ 
             conector_1, conector_2, conector_3                         
            ]    
        
    return conector

#%%
def enumerar_entradas_pan():
        
    conector_1 = "Estado_ruta_"+           "Ruta_"
    conector_2 = "CV_alarma_total_"+       "Ruta_"
    conector_3 = "CV_alarma_inmediata_"+   "Ruta_"
    conector_4 = "PAN_bloq_temp_solape_"+  "Ruta_"

    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4                       
            ]    
        
    return conector

#%%
def enumerar_entradas_sem():
        
    conector_1 = "SEM_estado_"+           "Ruta_"


    
    conector = [ 
             conector_1                      
            ]    
        
    return conector

#%%
def enumerar_entradas_rut():
        
    conector_1 = "CV_int_"+                 "Ruta_"
    conector_2 = "CV_paralelo_"+            "Ruta_"
    conector_3 = "CV_paralelo_temp_"+       "Ruta_"
    conector_4 = "CV_despeje_"+             "Ruta_"
    conector_5 = "CV_aprox_"+               "Ruta_"
    conector_6 = "Estado_sub_ruta_"+        "Ruta_"
    conector_7 = "Estado_ruta_cond_"+       "Ruta_"
    conector_8 = "Estado_ruta_confl_"+      "Ruta_"
    conector_9 = "Estado_SEM_sgte_"+        "Ruta_"
    conector_10 = "Pos_MDC_ruta_"+          "Ruta_"
    conector_11 = "Pos_MDC_aprox_"+         "Ruta_"
    conector_12 = "Pos_MDC_despeje_"+       "Ruta_"
    conector_13 = "Pos_MDC_solape_"+        "Ruta_"
    conector_14 = "Bloq_MDC_ruta_"+         "Ruta_"
    conector_15 = "Bloq_MDC_solape_"+       "Ruta_"
    conector_16 = "Estado_PAN_"+            "Ruta_"

    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4,   
             conector_5, conector_6, conector_7, conector_8,
             conector_9, conector_10, conector_11, conector_12,
             conector_13, conector_14, conector_15, conector_16                   
            ]    
        
    return conector

#%%
def enumerar_salidas_rutas():
        
    conector_1 = "SEM_rojo_"+                 "Ruta_"
    conector_2 = "SEM_naranja_"+              "Ruta_"
    conector_3 = "SEM_doble_naranja_"+       "Ruta_"
    conector_4 = "SEM_verde_"+               "Ruta_"
    conector_5 = "MDC_normal_"+              "Ruta_"
    conector_6 = "MDC_reverso_"+             "Ruta_"
    conector_7 = "MDC_libre_"+               "Ruta_"
    conector_8 = "MDC_cerrojado_"+           "Ruta_"
    conector_9 = "PAN_alto_"+                "Ruta_"
    conector_10 = "PAN_bajo_"+                "Ruta_"
    conector_11 = "PAN_alarma_"+              "Ruta_"
    conector_12 = "PAN_habilitacion_"+        "Ruta_"
    conector_13 = "RUT_estado_"+              "Ruta_"
    conector_14 = "RUT_sem_bloq_slp_"+     "Ruta_"

    
    conector = [ 
             conector_1, conector_2, conector_3, 
             conector_4, conector_5, conector_6, 
             conector_7, conector_8, conector_9,   
             conector_10, conector_11, conector_12,
             conector_13, conector_14
            ]    
        
    return conector

#%%
def enumerar_salidas_mdc():
        
    conector_1 = "MDC_normal_"+              "Ruta_"
    conector_2 = "MDC_reverso_"+             "Ruta_"
    conector_3 = "MDC_libre_"+               "Ruta_"
    conector_4 = "MDC_cerrojado_"+           "Ruta_"
    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4                   
            ]    
        
    return conector

#%%
def enumerar_salidas_pan():
        
    conector_1 = "PAN_alto_"+                "Ruta_"
    conector_2 = "PAN_bajo_"+                "Ruta_"
    conector_3 = "PAN_alarma_"+              "Ruta_"
    conector_4 = "PAN_habilitacion_"+        "Ruta_"
    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4                   
            ]    
        
    return conector

#%%
def enumerar_salidas_sem():
        
    conector_1 = "SEM_rojo_"+                 "Ruta_"
    conector_2 = "SEM_naranja_"+              "Ruta_"
    conector_3 = "SEM_doble_naranja_"+       "Ruta_"
    conector_4 = "SEM_verde_"+               "Ruta_"
    
    conector = [ 
             conector_1, conector_2, conector_3, conector_4                   
            ]    
        
    return conector


#%%
def enumerar_salidas_rut():
     
    conector_1 = "SEM_estado_"+           "Ruta_"
    conector_2 = "RUT_estado_"+           "Ruta_"
    conector_3 = "RUT_sem_bloq_slp_"+     "Ruta_"
    
    conector = [ 
             conector_1, conector_2, conector_3              
            ]    
        
    return conector

#%%
def auto_creador_rutas(f,rutas,rutas_dim,tipo):
 
    if (tipo == "In"):
        conector = enumerar_entradas_rutas()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_rutas()  
    
    for i in range(rutas):
        aux = ""
        for j in range(len(conector)):   
           
            aux = conector[j]+str(i+1)+"_s"  
            if (rutas_dim[i][j] != "1"):
                f.write("\t"+"Signal "+aux+" : std_logic_vector("+rutas_dim[i][j]+"-1 downto 0);\n") 
            else:
                f.write("\t"+"Signal "+aux+" : std_logic;\n") 
#%%
def auto_creador_mdc(f,N,dimension,tipo):
 
    if (tipo == "In"):
        conector = enumerar_entradas_mdc()            
    
    if (tipo == "Out"):      
        conector = enumerar_salidas_mdc() 
        dimension = convertir_lista_cambios_out(dimension)        
                     
    for i in range(N):
        aux = ""
        for j in range(len(conector)):   
               
            aux = conector[j]+str(i+1)+"_s"  
                
            if (dimension[i][j] != "1"):
                f.write("\t"+"Signal "+aux+" : std_logic_vector("+dimension[i][j]+"-1 downto 0);\n") 
            else:
                f.write("\t"+"Signal "+aux+" : std_logic;\n") 
 
#%%
def auto_creador_pan(f,N,dimension,tipo):
 
    if (tipo == "In"):
        conector = enumerar_entradas_pan()            
    
    if (tipo == "Out"):      
        conector = enumerar_salidas_pan() 
        dimension = convertir_lista_barreras_out(dimension)        
                     
    for i in range(N):
        aux = ""
        for j in range(len(conector)):   
               
            aux = conector[j]+str(i+1)+"_s"  
                
            if (dimension[i][j] != "1"):
                f.write("\t"+"Signal "+aux+" : std_logic_vector("+dimension[i][j]+"-1 downto 0);\n") 
            else:
                f.write("\t"+"Signal "+aux+" : std_logic;\n") 

#%%
def auto_creador_sem(f,N,dimension,tipo):
 
    if (tipo == "In"):
        conector = enumerar_entradas_sem()            
    
    if (tipo == "Out"):      
        conector = enumerar_salidas_sem() 
        dimension = convertir_lista_semaforos_out(dimension)        
                     
    for i in range(N):
        aux = ""
        for j in range(len(conector)):   
               
            aux = conector[j]+str(i+1)+"_s"  
                
            if (dimension[i][j] != "1"):
                f.write("\t"+"Signal "+aux+" : std_logic_vector("+dimension[i][j]+"-1 downto 0);\n") 
            else:
                f.write("\t"+"Signal "+aux+" : std_logic;\n") 

#%%
def auto_creador_rut(f,N,dimension,tipo):
 
    if (tipo == "In"):
        conector = enumerar_entradas_rut()            
    
    if (tipo == "Out"):      
        conector = enumerar_salidas_rut() 
        dimension = convertir_lista_ruta_out(dimension)        
                     
    for i in range(N):
        aux = ""
        for j in range(len(conector)):   
                        
            aux = conector[j]+str(i+1)+"_s"  
                
            if (dimension[i][j] != "1"):
                f.write("\t"+"Signal "+aux+" : std_logic_vector("+dimension[i][j]+"-1 downto 0);\n") 
            else:
                f.write("\t"+"Signal "+aux+" : std_logic;\n")                 
#%%               
def auto_conector_enrutador(f,rutas,tipo):
      
    if (tipo == "In"):
        conector = enumerar_entradas_rutas()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_rutas() 
        
    for i in range(rutas):
        for j in range(len(conector)):             
            f.write("\t\t"+ conector[j]+str(i+1)+" => "+conector[j]+str(i+1)+"_s,\n")

#%%               
def auto_conector_mdc(f,i,N,tipo):
      
    if (tipo == "In"):
        conector = enumerar_entradas_mdc()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_mdc() 
    
    if (tipo == "Begin"):
        conector = enumerar_entradas_mdc() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+"_s <= "+conector[j]+str(i+1)+";\n")
            f.write("\n")    
            return
        
    if (tipo == "End"):
        conector = enumerar_salidas_mdc() 
        for k in range(N):
            for j in range(len(conector)):               
                f.write("\t"+ conector[j]+str(i+1)+" <= "+conector[j]+str(i+1)+"_s;\n")
            f.write("\n")    
            return
        
        
    for j in range(len(conector)):             
        f.write("\t\t"+ conector[j]+str(i+1)+" => "+conector[j]+str(i+1)+"_s,\n")

#%%               
def auto_conector_pan(f,i,N,tipo):
      
    if (tipo == "In"):
        conector = enumerar_entradas_pan()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_pan() 
    
    if (tipo == "Begin"):
        conector = enumerar_entradas_pan() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+"_s <= "+conector[j]+str(i+1)+";\n")
            f.write("\n")    
            return
        
    if (tipo == "End"):
        conector = enumerar_salidas_pan() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+" <= "+conector[j]+str(i+1)+"_s;\n")
            f.write("\n")    
            return
        
        
    for j in range(len(conector)):             
        f.write("\t\t"+ conector[j]+str(i+1)+" => "+conector[j]+str(i+1)+"_s,\n")
 
#%%               
def auto_conector_sem(f,i,N,tipo):
      
    if (tipo == "In"):
        conector = enumerar_entradas_sem()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_sem() 
    
    if (tipo == "Begin"):
        conector = enumerar_entradas_sem() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+"_s <= "+conector[j]+str(i+1)+";\n")
            f.write("\n")    
            return
        
    if (tipo == "End"):
        conector = enumerar_salidas_sem() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+" <= "+conector[j]+str(i+1)+"_s;\n")
            f.write("\n")    
            return
        
        
    for j in range(len(conector)):             
        f.write("\t\t"+ conector[j]+str(i+1)+" => "+conector[j]+str(i+1)+"_s,\n")
     
        
 #%%               
def auto_conector_rut(f,i,N,tipo):
      
    if (tipo == "In"):
        conector = enumerar_entradas_rut()           
    
    if (tipo == "Out"):
        conector = enumerar_salidas_rut() 
    
    if (tipo == "Begin"):
        conector = enumerar_entradas_rut() 
        for k in range(N):
            for j in range(len(conector)):             
                f.write("\t"+ conector[j]+str(i+1)+"_s <= "+conector[j]+str(i+1)+";\n")
            f.write("\n")    
            return
        
    if (tipo == "End"):
        conector = enumerar_salidas_rut() 
        for k in range(N):
            for j in range(len(conector)):  
                if ( j == 0 ):
                    continue
                f.write("\t"+ conector[j]+str(i+1)+" <= "+conector[j]+str(i+1)+"_s;\n")
            f.write("\n")    
            return
        
        
    for j in range(len(conector)):             
        f.write("\t\t"+ conector[j]+str(i+1)+" => "+conector[j]+str(i+1)+"_s,\n")
     
           
#%%
def crear_puertos_ruta(N,rutas_dim,puertos_out,dimension,tipo,bloque):   
        
    if (tipo == "In"):
        if ( bloque == "ENR" ):
            conector = enumerar_entradas_rutas()
        if ( bloque == "MDC" ):
            conector = enumerar_entradas_mdc() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append(rutas_dim[N][j]) 
            return
        if ( bloque == "PAN" ):
            conector = enumerar_entradas_pan() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append(rutas_dim[N][j]) 
            return
        if ( bloque == "SEM" ):
            conector = enumerar_entradas_sem() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append(rutas_dim[N][j]) 
            return
        if ( bloque == "RUT" ):
            conector = enumerar_entradas_rut() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append(rutas_dim[N][j]) 
            return
        
    if (tipo == "Out"):
        if ( bloque == "ENR" ):
            conector = enumerar_salidas_rutas() 
        if ( bloque == "MDC" ):
            conector = enumerar_salidas_mdc() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append('1') 
            return
        if ( bloque == "PAN" ):
            conector = enumerar_salidas_pan() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append('1') 
            return
        if ( bloque == "SEM" ):
            conector = enumerar_salidas_sem() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append('1') 
            return
        if ( bloque == "RUT" ):
            conector = enumerar_salidas_rut() 
            for j in range(len(conector)):         
                puertos_out.append(conector[j]+str(N+1))
                dimension.append('1') 
            return
        
    for i in range(N):
        for j in range(len(conector)):   
            
            puertos_out.append(conector[j]+str(i+1))
            dimension.append(rutas_dim[i][j])           

