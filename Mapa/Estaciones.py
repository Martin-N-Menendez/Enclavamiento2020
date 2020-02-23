
from operator import attrgetter

class Estaciones:
     
    def imprimir(self):
        print("##################")
        print("<{}>:({})[{},{}]".format(self.id,self.nombre,self.pos_x,self.pos_y)) 

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

        if self.tipo == 'Extremo':
            if self.extremo:
                print("Tipo : {} absoluto".format(self.tipo))
            else:
                print("Tipo : {} relativo".format(self.tipo))
        elif self.tipo == "Cruce":
            if self.cambio_raiz:
                print("Tipo : {} raiz".format(self.tipo))
            else:
                print("Tipo : {} heredado".format(self.tipo))
        else:
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
        
    def __init__(self,nombre,index,pos_x,pos_y, sentido = '<>', barrera = False, extremo = False):
        self.id = index
        self.nombre = nombre
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.vecinos = []
        self.anterior = ""
        self.posterior = ""
        
        self.desvio_sup = ""
        self.desvio_inf = ""
        self.desvio_sup_dir = ""
        self.desvio_inf_dir = ""
        
        self.N_vecinos = 0
        
        self.tipo = ""
        self.sentido = sentido
        self.extremo = extremo
        
        self.semaforo = False     
        self.N_aspectos = []
        self.sem_sentido = []
        self.aspecto = [] 
        self.N_semaforos = 0 
        self.prox_semaforo = []
        
        self.ocupado = False
        
        self.cambio = False
        self.cambio_raiz = False

        #self.cambio_orden = ""
        #self.cambio_estado = True
        
        self.barrera = barrera
        self.barrera_index = 0
        #self.barrera_orden = ""
        #self.barrera_estado = ""
        
        #self.col = color(random(200) + 20, random(200) + 20, random(200) + 20)
        
        #self.generate_route(stops, grid)
        
        #self.cargar_estaciones()
        #self.imprimir()   
        #self.estaciones_contar()
