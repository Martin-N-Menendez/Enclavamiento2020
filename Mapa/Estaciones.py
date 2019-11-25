
from operator import attrgetter

class Estaciones:
     
    def imprimir(self):
        print("##################")
        print("<{}>:[{},{}]".format(self.id,self.pos_x,self.pos_y)) 
        #print("Vecinos <{}> : {}".format(self.N_vecinos,self.vecinos)) 
        if self.anterior != "":
            print("Anterior: {} ".format(self.anterior))
        if self.posterior != "":   
            print("Posterior: {} ".format(self.posterior))
            
        #if (self.desvio != "" ):    
        #    print("Desvio: {} ".format(self.desvio))
        if (self.desvio_inf != ""):    
            print("Desvio_inf: {} {}".format(self.desvio_inf,self.desvio_inf_dir))
        if (self.desvio_sup != ""):    
            print("Desvio_sup: {} {}".format(self.desvio_sup,self.desvio_sup_dir))

#        if (len(self.direccion) > 0):    
#            print("direccion del desvio: {} ".format(self.direccion))
        print("Tipo : {}".format(self.tipo)) 
        if self.semaforo == True:
            print("Cantidad de Aspectos <{}> : {}".format(self.N_semaforos,self.N_aspectos)) 
            print("Sentido <{}> : {}".format(self.N_semaforos,self.sentido)) 
            print("Estado <{}> : {}".format(self.N_semaforos,self.aspecto)) 
        #if self.barrera == True:
        #    print("Estado de barrera : {}".format(self.barrera_estado)) 
        if self.cambio == True:
            if self.cambio_estado:
                mensaje = "Normal"
            else:
                mensaje = "Reverso"
            print("Estado de cambio : {}".format(mensaje))  
            
    def calcular_vecinos(self):
        self.N_vecinos = len(self.vecinos)
            
     
    def calcular_semaforos(self):
        self.N_semaforos = len(self.N_aspectos)
        
    def __init__(self,index,pos_x,pos_y, b = False):
        self.id = index
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.vecinos = []
        self.anterior = ""
        self.posterior = ""
        #self.desvio = ""
        self.desvio_sup = ""
        self.desvio_inf = ""
        self.desvio_sup_dir = ""
        self.desvio_inf_dir = ""
        self.N_vecinos = 0
        self.T_vecino = []
        
        self.tipo = ""
        
        self.semaforo = False
        self.prox_semaforo = []
        self.N_aspectos = []
        self.N_semaforos = 0
        self.sentido = []
        self.aspecto = []
        self.libre = ""
        self.ocupado = False
        
        self.cambio = False
        #self.cambio_orden = ""
        #self.cambio_estado = True
        
        self.barrera = b
        self.barrera_index = 0
        #self.barrera_orden = ""
        #self.barrera_estado = ""
        
        #self.col = color(random(200) + 20, random(200) + 20, random(200) + 20)
        
        #self.generate_route(stops, grid)
        
        #self.cargar_estaciones()
        #self.imprimir()   
        #self.estaciones_contar()
