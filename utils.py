from algoritmos.procesos import Proceso

def generar_procesos_ejemplo():
    """Genera un conjunto de procesos de ejemplo"""
    return [
        Proceso(1, 0, 5),
        Proceso(2, 1, 3),
        Proceso(3, 2, 8),
        Proceso(4, 3, 6),
        Proceso(5, 4, 2)
    ]

def generar_procesos_aleatorios(n=6):
    """Genera n procesos con tiempos aleatorios"""
    import random
    procesos = []
    for i in range(n):
        llegada = random.randint(0, 5)
        rafaga = random.randint(1, 10)
        procesos.append(Proceso(i+1, llegada, rafaga))
    return procesos

def imprimir_resultados(algoritmo, resultados, metricas):
    """Imprime los resultados de forma legible"""
    print(f"\n{'='*60}")
    print(f"ALGORITMO: {algoritmo.nombre}")
    print(f"Descripción: {algoritmo.descripcion}")
    print(f"{'='*60}")
    
    print("\nEJECUCIÓN DETALLADA:")
    for resultado in resultados:
        if 'duracion' in resultado:  # Round Robin
            print(f"Proceso {resultado['proceso'].id}: Inicio={resultado['tiempo_inicio']}, "
                  f"Fin={resultado['tiempo_final']}, Duración={resultado['duracion']}")
        else:  # FIFO o SJF
            print(f"Proceso {resultado['proceso'].id}: Inicio={resultado['tiempo_inicio']}, "
                  f"Fin={resultado['tiempo_finalizacion']}")
    
    print("\nMÉTRICAS POR PROCESO:")
    procesos_unicos = list(set(r['proceso'] for r in resultados))
    for proceso in sorted(procesos_unicos, key=lambda p: p.id):
        print(f"P{proceso.id}: Espera={proceso.tiempo_espera}, "
              f"Respuesta={proceso.tiempo_respuesta}, "
              f"Retorno={proceso.tiempo_finalizacion - proceso.tiempo_llegada}")
    
    print(f"\nMÉTRICAS GENERALES:")
    for metrica, valor in metricas.items():
        print(f"{metrica.replace('_', ' ').title()}: {valor:.2f}")