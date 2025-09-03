# transformaciones_geometricas.py

import numpy as np
import math

# Función para escalar un punto
def escalar(punto, escala):
    matriz_escalado = np.array([[escala, 0], [0, escala]])
    return np.dot(matriz_escalado, punto)

# Función para trasladar un punto
def trasladar(punto, translacion):
    return punto + translacion

# Función para rotar un punto
def rotar(punto, angulo):
    radianes = math.radians(angulo)
    matriz_rotacion = np.array([[math.cos(radianes), -math.sin(radianes)],
                                 [math.sin(radianes), math.cos(radianes)]])
    return np.dot(matriz_rotacion, punto)

# Cálculos para una pirámide con base triangular
def calcular_piramide(base, altura):
    # Base: coordenadas de los vértices de la base
    # altura: altura de la pirámide
    A, B, C = base
    # Calcular el área de la base triangular
    area_base = 0.5 * np.linalg.norm(np.cross(B - A, C - A))
    volumen = area_base * altura / 3
    return area_base, volumen

# Solución paso a paso para tareas de geometría
def tarea_geometrica():
    # Ejemplo de transformación
    punto = np.array([1, 1])
    escala = 2
    punto_escalado = escalar(punto, escala)
    print(f"Punto escalado: {punto_escalado}")

    # Cálculo de la pirámide
    base = np.array([[0, 0], [1, 0], [0.5, math.sqrt(3)/2]])
    altura = 3
    area_base, volumen = calcular_piramide(base, altura)
    print(f"Área de la base: {area_base}, Volumen: {volumen}")

# Ejecutar la tarea geométrica
if __name__ == "__main__":
    tarea_geometrica()