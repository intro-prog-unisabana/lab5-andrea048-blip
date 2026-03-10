def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)
print(promedio_estudiante([85, 92, 78]))
