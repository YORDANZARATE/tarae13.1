#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo.
# La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.





def calcular_temperatura_promedio(datos):

    promedios = {}

    for i, ciudad_datos in enumerate(datos):
        promedio = sum(ciudad_datos) / len(ciudad_datos)
        promedios[f'Ciudad_{i + 1}'] = promedio

    return promedios


# Ejemplo de uso
datos = [
    [25, 27, 30, 28],  # Temperaturas para la Ciudad QUITO
    [22, 24, 26, 23],  # Temperaturas para la Ciudad GUAYAQUIL
    [19, 21, 20, 22]  # Temperaturas para la Ciudad LOJA
]

promedios = calcular_temperatura_promedio(datos)
print(promedios)
