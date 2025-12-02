from .procesos import Proceso
from collections import deque

class RoundRobin:
    def __init__(self, quantum=2):
        self.nombre = "Round Robin"
        self.descripcion = f"Algoritmo Round Robin con Quantum={quantum}"
        self.quantum = quantum
    
    def ejecutar(self, procesos):
        # Crear copias de los procesos para no modificar los originales
        procesos_copia = [Proceso(p.id, p.tiempo_llegada, p.tiempo_rafaga) for p in procesos]
        
        # Ordenar por tiempo de llegada
        procesos_copia.sort(key=lambda p: p.tiempo_llegada)
        
        cola = deque()
        tiempo_actual = 0
        indice = 0
        resultados = []
        procesos_completados = 0
        n = len(procesos_copia)
        
        while procesos_completados < n:
            # Agregar procesos que han llegado a la cola
            while indice < n and procesos_copia[indice].tiempo_llegada <= tiempo_actual:
                cola.append(procesos_copia[indice])
                indice += 1
            
            if not cola:
                tiempo_actual += 1
                continue
            
            proceso_actual = cola.popleft()
            
            # Marcar tiempo de respuesta si es la primera vez
            if proceso_actual.tiempo_respuesta == -1:
                proceso_actual.tiempo_respuesta = tiempo_actual - proceso_actual.tiempo_llegada
            
            # Ejecutar por quantum o hasta completar
            tiempo_ejecucion = min(self.quantum, proceso_actual.tiempo_rafaga_restante)
            tiempo_inicio = tiempo_actual
            tiempo_actual += tiempo_ejecucion
            proceso_actual.tiempo_rafaga_restante -= tiempo_ejecucion
            
            resultados.append({
                'proceso': proceso_actual,
                'tiempo_inicio': tiempo_inicio,
                'tiempo_final': tiempo_actual,
                'duracion': tiempo_ejecucion
            })
            
            # Agregar procesos que llegaron durante esta ejecución
            while indice < n and procesos_copia[indice].tiempo_llegada <= tiempo_actual:
                cola.append(procesos_copia[indice])
                indice += 1
            
            # Si el proceso no ha terminado, volver a la cola
            if proceso_actual.tiempo_rafaga_restante > 0:
                cola.append(proceso_actual)
            else:
                proceso_actual.tiempo_finalizacion = tiempo_actual
                proceso_actual.tiempo_espera = (proceso_actual.tiempo_finalizacion - 
                                              proceso_actual.tiempo_llegada - 
                                              proceso_actual.tiempo_rafaga)
                procesos_completados += 1
        
        return resultados
    
    def calcular_metricas(self, procesos):
        tiempo_espera_promedio = sum(p.tiempo_espera for p in procesos) / len(procesos)
        tiempo_respuesta_promedio = sum(p.tiempo_respuesta for p in procesos) / len(procesos)
        tiempo_retorno_promedio = sum(p.tiempo_finalizacion - p.tiempo_llegada for p in procesos) / len(procesos)
        
        return {
            'tiempo_espera_promedio': tiempo_espera_promedio,
            'tiempo_respuesta_promedio': tiempo_respuesta_promedio,
            'tiempo_retorno_promedio': tiempo_retorno_promedio
        } 
from .procesos import Proceso
from collections import deque

class RoundRobin:
    def __init__(self, quantum=2):
        self.nombre = "Round Robin"
        self.descripcion = f"Algoritmo Round Robin con Quantum={quantum}"
        self.quantum = quantum
    
    def ejecutar(self, procesos):
        # Crear copias de los procesos para no modificar los originales
        procesos_copia = [Proceso(p.id, p.tiempo_llegada, p.tiempo_rafaga) for p in procesos]
        
        # Ordenar por tiempo de llegada
        procesos_copia.sort(key=lambda p: p.tiempo_llegada)
        
        cola = deque()
        tiempo_actual = 0
        indice = 0
        resultados = []
        procesos_completados = 0
        n = len(procesos_copia)
        
        while procesos_completados < n:
            # Agregar procesos que han llegado a la cola
            while indice < n and procesos_copia[indice].tiempo_llegada <= tiempo_actual:
                cola.append(procesos_copia[indice])
                indice += 1
            
            if not cola:
                tiempo_actual += 1
                continue
            
            proceso_actual = cola.popleft()
            
            # Marcar tiempo de respuesta si es la primera vez
            if proceso_actual.tiempo_respuesta == -1:
                proceso_actual.tiempo_respuesta = tiempo_actual - proceso_actual.tiempo_llegada
            
            # Ejecutar por quantum o hasta completar
            tiempo_ejecucion = min(self.quantum, proceso_actual.tiempo_rafaga_restante)
            tiempo_inicio = tiempo_actual
            tiempo_actual += tiempo_ejecucion
            proceso_actual.tiempo_rafaga_restante -= tiempo_ejecucion
            
            resultados.append({
                'proceso': proceso_actual,
                'tiempo_inicio': tiempo_inicio,
                'tiempo_final': tiempo_actual,
                'duracion': tiempo_ejecucion
            })
            
            # Agregar procesos que llegaron durante esta ejecución
            while indice < n and procesos_copia[indice].tiempo_llegada <= tiempo_actual:
                cola.append(procesos_copia[indice])
                indice += 1
            
            # Si el proceso no ha terminado, volver a la cola
            if proceso_actual.tiempo_rafaga_restante > 0:
                cola.append(proceso_actual)
            else:
                proceso_actual.tiempo_finalizacion = tiempo_actual
                proceso_actual.tiempo_espera = (proceso_actual.tiempo_finalizacion - 
                                              proceso_actual.tiempo_llegada - 
                                              proceso_actual.tiempo_rafaga)
                procesos_completados += 1
        
        return resultados
    
    def calcular_metricas(self, procesos):
        tiempo_espera_promedio = sum(p.tiempo_espera for p in procesos) / len(procesos)
        tiempo_respuesta_promedio = sum(p.tiempo_respuesta for p in procesos) / len(procesos)
        tiempo_retorno_promedio = sum(p.tiempo_finalizacion - p.tiempo_llegada for p in procesos) / len(procesos)
        
        return {
            'tiempo_espera_promedio': tiempo_espera_promedio,
            'tiempo_respuesta_promedio': tiempo_respuesta_promedio,
            'tiempo_retorno_promedio': tiempo_retorno_promedio
        }