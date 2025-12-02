from .procesos import Proceso

class SJF:
    def __init__(self):
        self.nombre = "SJF"
        self.descripcion = "Shortest Job First (No Expropiativo)"
    
    def ejecutar(self, procesos):
        procesos_copia = [Proceso(p.id, p.tiempo_llegada, p.tiempo_rafaga) for p in procesos]
        procesos_copia.sort(key=lambda p: p.tiempo_llegada)
        
        tiempo_actual = 0
        procesos_completados = 0
        n = len(procesos_copia)
        resultados = []
        procesos_restantes = procesos_copia.copy()
        
        while procesos_completados < n:
            # Filtrar procesos que han llegado
            procesos_disponibles = [p for p in procesos_restantes if p.tiempo_llegada <= tiempo_actual]
            
            if not procesos_disponibles:
                tiempo_actual += 1
                continue
            
            # Seleccionar el proceso con menor tiempo de ráfaga
            proceso_actual = min(procesos_disponibles, key=lambda p: p.tiempo_rafaga)
            
            # Marcar tiempo de respuesta
            if proceso_actual.tiempo_respuesta == -1:
                proceso_actual.tiempo_respuesta = tiempo_actual - proceso_actual.tiempo_llegada
            
            # Ejecutar proceso completo
            tiempo_inicio = tiempo_actual
            tiempo_actual += proceso_actual.tiempo_rafaga
            proceso_actual.tiempo_finalizacion = tiempo_actual
            proceso_actual.tiempo_espera = tiempo_inicio - proceso_actual.tiempo_llegada
            
            resultados.append({
                'proceso': proceso_actual,
                'tiempo_inicio': tiempo_inicio,
                'tiempo_finalizacion': tiempo_actual
            })
            
            procesos_restantes.remove(proceso_actual)
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