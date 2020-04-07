import time
import serial
from datetime import datetime
import random
import sys
import signal


from vhdl import *
from Estaciones import *
from Plotear import *

global objetos

global intento
intento = 0

# Variables globales con valores iniciales ------------------------------------

global cvs_t
global sem_t
global pan_t
global mdc_t
global trama

cvs_t = "111111"
sem_t = "00000000000000"
pan_t = ""
mdc_t = "1"

global trama_tagged

global ser
ser = serial.Serial()

def signal_handler(sig, frame):
    print('Se pulsó Ctrl+C!, saliendo del programa!')
    try:
        ser.close()
    except:
        pass
    else:
        print('Se cerró el puerto OK.')
    sys.exit(0)    
    
# Funciones -------------------------------------------------------------------
#%%
def calcular_sem_owner(secciones,i):

    acumulado = secciones[0].N_semaforos
    #k = 0
    
    for j in range(len(secciones)):
        
        if i+1 < acumulado:  
            #k = 0;
            return j
        else:
            acumulado += secciones[j].N_semaforos
            #k = k + 1
            
    return j+1   

#%%
def calcular_sem_index(secciones,sem_owner,sem_index,nuevo):
    
    Limite = secciones[sem_owner-1].N_semaforos

    #print (Limite)
    
    #print("int({})|{}".format(sem_owner,sem_index))
    if nuevo:
        sem_index = 0
    #print("int({})|{}".format(sem_owner,sem_index))      
        
    if sem_index < Limite:
        sem_index += 1
        
        if sem_index == Limite:       
            return sem_index, True
        else:
            return sem_index, False
    
     
    
#%%
def procesar_trama_recibida(leido,secciones):
    
    #print(objetos)
    
    sem = ""
    pan = ""
    mdc = ""
    
    N_sem = objetos[1]
    N_pan = objetos[2]
    N_mdc = objetos[3]
    
    sem = leido[0:2*N_sem]
    
    if N_pan > 0:
        pan = leido[2*N_sem:2*N_sem+N_pan]
 
    if N_mdc > 0:
        mdc = leido[2*N_sem+N_pan:2*N_sem+N_pan+N_mdc]
    
    print ("Recibido: ", leido) 
    
    print ("Sem: ", sem) 
    
    sem_index = 0
    nuevo = False
    
    for i in range(N_sem):
        par =  sem[2*i:2*i+2]
        
        sem_owner = calcular_sem_owner(secciones,i)
        
        sem_index,nuevo = calcular_sem_index(secciones,sem_owner,sem_index,nuevo)
        
        #print("({})|{}".format(sem_owner,sem_index))
        
        if par == "00":
            color = "Rojo"          
        elif par == "01":
            color = "Amarillo" 
        elif par == "10":
            color = "Amarillo" 
        elif par == "11":
            if secciones[sem_owner-1].N_aspectos[sem_index-1] == '3':
                color = "Verde"
            else:
                color = "Amarillo"

        
        secciones[sem_owner-1].aspecto[sem_index-1] = color
        
        print ("({})Semaforos_{}:{} ".format( sem_owner,i+1,color ))
    
    
    
    if N_pan > 0:    
        print ("Pasos a nivel: ", pan) 
    
    if N_mdc > 0:
        if mdc == "0":
            cambio = "normal" 
        else:
            cambio = "reverso"
             
        print ("Cambio: ", cambio) 

def sendData( trama , secciones ,conexiones ):

   trama_tagged = "<"+ trama +">";
   
    
   print ("Enviando: ",  trama_tagged)
   ser.write(str(trama_tagged).encode())
   time.sleep(0.1)
   
   try:
      #print ("Leyendo ...")   
      leido = ser.read(ser.in_waiting).decode('ascii')
      #time.sleep(1)
      procesar_trama_recibida(leido,secciones)     
      mostrar_grafo(secciones,10,j = intento,gif_mode = True)
   except:
      pass
   
   #print( "Dato enviado: " + EAN_13_tagged + '' )
   ser.flushInput()  # flush input buffer, discarding all its contents
   ser.flushOutput() # flush output buffer, aborting current output 
                            # and discard all that is in buffer
   
   #ser.close()
  
   
   
   #if (leido[0:-1] == trama_tagged):
   #    estado = "Ok"
   #else:
   #    estado = "Falla"
   #
   #print ("Estatus: "+estado)
   
   return

def cmd_h():
   print( "Comandos disponibles -----------------------------------------------" )
   print( "   'h' (help) Imprime esta lista de comandos." )
   print( "   'q' (quit) Salir del programa." )
   print( "   '1' Insertar tren" )
   print( "   '2' Remover tren" )
   print( "   '3' Modificar aspecto de semaforo" )
   print( "   '4' Modificar posición de la máquina de cambios" )
   print( "   '>' Avanzar todos los trenes" )
   print( "   '<' Retroceder todos los trenes" )
   print( "--------------------------------------------------------------------\n" )
   return

# comando 1:  Tag inicial erroneo

def cmd_0(secciones,conexiones):
   sendData( "101111"+"00000000000000"+"1" , secciones ,conexiones)
   return   

# comando 1:  Tag inicial erroneo
def cmd_1(secciones,conexiones):
    
   N_cvs = objetos[0]

   global cvs_t
      
   comando = ""
    
   print("Ingresar tramo ocupado")
   comando = input(">> ")      # for Python 3

   if comando >= '1' and comando <= str(N_cvs):
       print("Ocupado tramo "+str(comando))
       index = int(comando)
       cvs_t = cvs_t[:index-1] + '0' + cvs_t[index:]
       secciones[index-1].ocupado = True;
       
       
   sendData( cvs_t + sem_t + pan_t + mdc_t , secciones,conexiones )
   return

# comando 1:  Tag final erroneo
def cmd_2(secciones,conexiones):
   N_cvs = objetos[0]

   global cvs_t 
      
   comando = ""
    
   print("Ingresar tramo desocupado")
   comando = input(">> ")      # for Python 3

   if comando >= '1' and comando <= str(N_cvs):
       print("Desocupando tramo "+str(comando))
       index = int(comando)
       cvs_t = cvs_t[:index-1] + '1' + cvs_t[index:]
       secciones[index-1].ocupado = False;
   
       
         
   sendData( cvs_t + sem_t + pan_t + mdc_t , secciones,conexiones  )
   return

# comando 3: Checksum erroneo
def cmd_3(secciones):
   #sendData( '(',')',False )
   return

# comando 4: Todo OK
def cmd_4(secciones,conexiones):
   N_mdc = objetos[3]

   global mdc_t 
      
   comando = ""
    
   print("Ingresar maquina de cambios a modificar")
   comando = input(">> ")      # for Python 3

   if comando >= '1' and comando <= str(N_mdc):
       print("Modificando maquina de cambios "+str(comando))
       index = int(comando)
       if mdc_t[index-1] == '1':
           mdc_t = mdc_t[:index-1] + '0' + mdc_t[index:]
       else:
           mdc_t = mdc_t[:index-1] + '1' + mdc_t[index:]
           
   sendData( cvs_t + sem_t + pan_t + mdc_t , secciones,conexiones )  
   return


# comando r: Enviar un dato aleatorio del equipo con ID1.
def cmd_adelante(secciones,conexiones):

   #for i in range(10):
   #    sendData( '(',')',True )
   return            
 
def cmd_atras(secciones,conexiones):

   #for i in range(10):
   #    sendData( '(',')',True )
   return   
     
# Inicializa y abre el puertos serie ------------------------------------------           
def uart_main(secciones,conexiones):
    
    signal.signal(signal.SIGINT, signal_handler)
    
    ser.port = "COM4"            # Puerto por defecto para Windows    
    
    global objetos
    objetos = calcular_paquete(secciones)
    
    global intento
    intento = 0
    
    print("Conectandose a "+str(ser.port))
    
    ser.baudrate = 19200
    ser.bytesize = serial.EIGHTBITS    # number of bits per bytes # SEVENBITS
    ser.parity = serial.PARITY_NONE    # set parity check: no parity # PARITY_ODD
    ser.stopbits = serial.STOPBITS_ONE # number of stop bits # STOPBITS_TWO
    #ser.timeout = None                 # block read
    ser.timeout = 1                    # non-block read
    #ser.timeout = 2                    # timeout block read
    ser.xonxoff = False                # disable software flow control
    ser.rtscts = False                 # disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False                 # disable hardware (DSR/DTR) flow control
    ser.writeTimeout = 2               # timeout for write
    
    try: 
       ser.open()
    except Exception as e:
       print("Error abriendo puerto serie.\n" + str(e) + '\nFin de programa.')
       #exit()
       return;
    
    # Si pudo abrir el puerto -----------------------------------------------------
    
    if ser.isOpen():
    
       print(ser.name + ' abierto.\n')
    
       try:
          ser.flushInput()  # flush input buffer, discarding all its contents
          ser.flushOutput() # flush output buffer, aborting current output 
                            # and discard all that is in buffer
    
          cmd_h()           # Imprime la lista de comandos
    
          # Ciclo infinito hasta comando exit (q) ---------------------------------
          while True: 
    
              command = ""
    
             # get keyboard input
             # input = raw_input(">> ")  # for Python 2
              command = input(">> ")      # for Python 3
    
              if command == 'q':
                print("Puerto cerrado. Se cierra el programa.")
                ser.close()
                #exit()
                return;
    
              elif command == 'h':
                cmd_h()
    
              elif command == '0':   # Insertar trama manual
                intento += 1
                cmd_0(secciones,conexiones)
                
              elif command == '1':   # Insertar tren
                intento += 1  
                cmd_1(secciones,conexiones)
              
              elif command == '2':   # Remover tren
                 intento += 1 
                 cmd_2(secciones,conexiones)
             
              elif command == '3':   # Modificar aspecto semaforo
                 intento += 1 
                 cmd_3(secciones,conexiones)    
    
              elif command == '4':   # Modificar aspecto de maquina de cambios
                 intento += 1 
                 cmd_4(secciones,conexiones)  
                 
              elif command == '>':   # Avanzar todos los trenes
                intento += 1  
                cmd_adelante(secciones,conexiones)
                
              elif command == '<':   # Retroceder todos los trenes
                intento += 1  
                cmd_atras(secciones,conexiones)
                
                
              else:
                print("Comando no conocido.")
    
       except Exception as e1:
          print("Error de comunicación." + str(e1))
    
    else:
       print("No se puede abrir el puerto serie.")
       #exit()
       return;
       
#%%

       
