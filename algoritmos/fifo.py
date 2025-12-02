from .procesos import Proceso

class FIFO:
    def __init__(self):
        self.nombre = "FIFO"
        self.descripcion = "First-In, First-Out (First-Come, First-Served)"
    
    def ejecutar(self, procesos):
        # Ordenar procesos por tiempo de llegada
        procesos_ordenados = sorted(procesos, key=lambda p: p.tiempo_llegada)
        
        tiempo_actual = 0
        resultados = []
        
        for proceso in procesos_ordenados:
            # Si el proceso llega después del tiempo actual, avanzar el tiempo
            if tiempo_actual < proceso.tiempo_llegada:
                tiempo_actual = proceso.tiempo_llegada
            
            # Tiempo de respuesta es 0 para FIFO (comienza inmediatamente al llegar)
            if proceso.tiempo_respuesta == -1:
                proceso.tiempo_respuesta = tiempo_actual - proceso.tiempo_llegada
            
            # Ejecutar el proceso completo
            tiempo_inicio = tiempo_actual
            tiempo_actual += proceso.tiempo_rafaga
            proceso.tiempo_finalizacion = tiempo_actual
            
            # Calcular tiempos
            proceso.tiempo_espera = tiempo_inicio - proceso.tiempo_llegada
            
            resultados.append({
                'proceso': proceso,
                'tiempo_inicio': tiempo_inicio,
                'tiempo_finalizacion': tiempo_actual
            })
        
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