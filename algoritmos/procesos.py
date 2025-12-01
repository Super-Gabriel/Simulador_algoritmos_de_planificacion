class Proceso:
    def __init__(self, id, tiempo_llegada, tiempo_rafaga, prioridad=0):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_rafaga = tiempo_rafaga
        self.tiempo_rafaga_restante = tiempo_rafaga
        self.tiempo_finalizacion = 0
        self.tiempo_espera = 0
        self.tiempo_respuesta = -1  # -1 indica que no ha comenzado
        self.prioridad = prioridad
    
    def __str__(self):
        return f"Proceso {self.id}: Llegada={self.tiempo_llegada}, Ráfaga={self.tiempo_rafaga}"
    
    def __repr__(self):
        return self.__str__()