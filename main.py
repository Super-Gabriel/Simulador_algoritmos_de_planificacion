from algoritmos.procesos import Proceso
from algoritmos.fifo import FIFO
from utils import generar_procesos_ejemplo, generar_procesos_aleatorios, imprimir_resultados

def main():
    print("SIMULADOR DE ALGORITMOS DE PLANIFICACIÓN DE PROCESOS")
    print("=" * 60)
    
    # Seleccionar conjunto de procesos
    print("\nSeleccione el conjunto de procesos:")
    print("1. Procesos de ejemplo")
    print("2. Procesos aleatorios")
    
    opcion = input("Opción (1-2): ").strip()
    
    if opcion == "1":
        procesos = generar_procesos_ejemplo()
    else:
        n = int(input("Número de procesos (default 6): ") or "6")
        procesos = generar_procesos_aleatorios(n)
    
    print("\nPROCESOS A SIMULAR:")
    for proceso in procesos:
        print(proceso)
    
    # Configurar algoritmos
    quantum = int(input("\nQuantum para Round Robin (default 2): ") or "2")
    
    algoritmos = [
        FIFO(),
    ]
    
    # Ejecutar simulaciones
    for algoritmo in algoritmos:
        # Hacer copia de los procesos para cada algoritmo
        procesos_copia = [Proceso(p.id, p.tiempo_llegada, p.tiempo_rafaga) for p in procesos]
        
        # Ejecutar algoritmo
        resultados = algoritmo.ejecutar(procesos_copia)
        
        # Calcular métricas
        procesos_unicos = list(set(r['proceso'] for r in resultados))
        metricas = algoritmo.calcular_metricas(procesos_unicos)
        
        # Mostrar resultados
        imprimir_resultados(algoritmo, resultados, metricas)
    
    # Comparativa final
    print(f"\n{'='*80}")
    print("COMPARATIVA FINAL DE ALGORITMOS")
    print(f"{'='*80}")
    
    comparativa = []
    for algoritmo in algoritmos:
        procesos_copia = [Proceso(p.id, p.tiempo_llegada, p.tiempo_rafaga) for p in procesos]
        resultados = algoritmo.ejecutar(procesos_copia)
        procesos_unicos = list(set(r['proceso'] for r in resultados))
        metricas = algoritmo.calcular_metricas(procesos_unicos)
        comparativa.append((algoritmo.nombre, metricas))
    
    print(f"\n{'Algoritmo':<15} {'Espera Prom.':<15} {'Respuesta Prom.':<15} {'Retorno Prom.':<15}")
    print("-" * 65)
    for nombre, metricas in comparativa:
        print(f"{nombre:<15} {metricas['tiempo_espera_promedio']:<15.2f} "
              f"{metricas['tiempo_respuesta_promedio']:<15.2f} "
              f"{metricas['tiempo_retorno_promedio']:<15.2f}")

if __name__ == "__main__":
    main()
