import time
import serial
from datetime import datetime
import random
import sys
import signal

from vhdl import *

global objetos


# Variables globales con valores iniciales ------------------------------------


global trama
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

def generar_random():  

   global trama
   trama = ""

   for i in range(21):
       trama = trama + str(random.randint(0,1))
   return


   
def agregar_tags(tag_inicial,tag_final):  

   global trama
   global trama_tagged
   
   trama_tagged = tag_inicial+trama+tag_final
   
   return

def procesar_trama_recibida(leido):
    
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
    
    for i in range(7):
        par =  sem[2*i:2*i+2]
       
        if par == "00":
            color = "rojo" 
        elif par == "01":
            color = "amarillo" 
        elif par == "10":
            color = "naranja" 
        elif par == "11":
            color = "verde" 
            
        print ("Semaforos_"+str(i+1)+": ", color)
    
    if N_pan > 0:    
        print ("Pasos a nivel: ", pan) 
    
    if N_mdc > 0:
        if mdc == "1":
            cambio = "normal" 
        else:
            cambio = "reverso"
             
        print ("Cambio: ", cambio) 

def sendData( tag_inicial,tag_final,manual = False ):
   #print( "Dato enviado --------------------------------------------\n" )
   
   
   generar_random()
   agregar_tags('<','>')

   if manual:
       trama_tagged = "<"+"111111"+"00000000000000"+"1"+">";
       
   print ("Enviando: ",  trama_tagged)
   ser.write(str(trama_tagged).encode())
   time.sleep(0.1)
   
   try:
      #print ("Leyendo ...")   
      leido = ser.read(ser.in_waiting).decode('ascii')
      #time.sleep(1)
      procesar_trama_recibida(leido)
      
   except:
      pass
   
   #print( "Dato enviado: " + EAN_13_tagged + '' )
   ser.flushInput()  # flush input buffer, discarding all its contents
   ser.flushOutput() # flush output buffer, aborting current output 
                            # and discard all that is in buffer
   
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

def cmd_0():
   sendData( '<',')',True )
   return   

# comando 1:  Tag inicial erroneo
def cmd_1():
   sendData( '<',')',False )
   return

# comando 1:  Tag final erroneo
def cmd_2():
   sendData( '(','>',False )
   return

# comando 3: Checksum erroneo
def cmd_3():
   sendData( '(',')',False )
   return

# comando 4: Todo OK
def cmd_4():
   sendData( '(',')',False )   
   return


# comando r: Enviar un dato aleatorio del equipo con ID1.
def cmd_adelante():

   for i in range(10):
       sendData( '(',')',True )
   return            
 
def cmd_atras():

   for i in range(10):
       sendData( '(',')',True )
   return   
     
# Inicializa y abre el puertos serie ------------------------------------------           
def uart_main(secciones):
    
    signal.signal(signal.SIGINT, signal_handler)
    
    ser.port = "COM4"            # Puerto por defecto para Windows
    
    global objetos
    objetos = calcular_paquete(secciones)
    
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
                cmd_0()
                
             elif command == '1':   # Insertar tren
                cmd_1()
              
             elif command == '2':   # Remover tren
                 cmd_2()
             
             elif command == '3':   # Modificar aspecto semaforo
                 cmd_3()    
    
             elif command == '4':   # Modificar aspecto de maquina de cambios
                 cmd_4()  
                 
             elif command == '>':   # Avanzar todos los trenes
                cmd_adelante()
                
             elif command == '<':   # Retroceder todos los trenes
                cmd_atras()
                
                
             else:
                print("Comando no conocido.")
    
       except Exception as e1:
          print("Error de comunicación." + str(e1))
    
    else:
       print("No se puede abrir el puerto serie.")
       #exit()
       return;
       
#%%

       
