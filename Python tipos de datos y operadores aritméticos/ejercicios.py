import math

# EJERCICIO 1: Asignación Secuencial
a = 4
a = a + 5  # Reasignación de 'a'
b = a - 2  # Evaluación con el nuevo valor de 'a'
c = a * b  # Evaluación con los valores actualizados de 'a' y 'b'

print("--- Ejercicio 1 ---")
print(f"a = {a}, b = {b}, c = {c}\n")

# EJERCICIO 2: Polinomio Cúbico Simple
x = 3
y = (x ** 3) + (2 * (x ** 2)) - (5 * x) + 7

print("--- Ejercicio 2 ---")
print(f"Resultado de y = {y}\n")

# EJERCICIO 3: Expresión con Paréntesis
a, b, c_var, d = 5, 2, 8, 4  # c_var usado para no reescribir variables después
z = ((a + b) * (c_var - d)) / (a * b)

print("--- Ejercicio 3 ---")
print(f"Resultado de z = {z}\n")

# EJERCICIO 4: Distancia Euclidiana
x1, y1 = 2, 3
x2, y2 = 6, 6
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("--- Ejercicio 4 ---")
print(f"Distancia entre los puntos = {distancia}\n")

# EJERCICIO 5: Interés Compuesto
P, r, n, t = 1000, 0.05, 12, 3
A = P * ((1 + (r / n)) ** (n * t))

print("--- Ejercicio 5 ---")
print(f"Monto final acumulado A = {A:.4f}\n")

# EJERCICIO 6: Promedio Ponderado
n1, n2, n3 = 85, 90, 78
w1, w2, w3 = 0.3, 0.4, 0.3
promedio = ((n1 * w1) + (n2 * w2) + (n3 * w3)) / (w1 + w2 + w3)

print("--- Ejercicio 6 ---")
print(f"Promedio ponderado = {promedio:.2f}\n")

# EJERCICIO 7: Fórmulas Cuadráticas
a_cuad, b_cuad, c_cuad = 1, -5, 6
discriminante = (b_cuad ** 2) - (4 * a_cuad * c_cuad)

x1_raiz = (-b_cuad + math.sqrt(discriminante)) / (2 * a_cuad)
x2_raiz = (-b_cuad - math.sqrt(discriminante)) / (2 * a_cuad)

print("--- Ejercicio 7 ---")
print(f"Primera raíz (x1) = {x1_raiz}")
print(f"Segunda raíz (x2) = {x2_raiz}\n")

# EJERCICIO 8: Conversión de Temperatura
F = 98.6
C = (F - 32) * (5 / 9)
K = C + 273.15

print("--- Ejercicio 8 ---")
print(f"Temperatura en Celsius: {C:.2f} °C")
print(f"Temperatura en Kelvin: {K:.2f} K\n")

# EJERCICIO 9: Expresión Fraccionaria I
a_frac, b_frac, c_frac = 6, 3, 2
numerador_9 = (a_frac + b_frac) / c_frac
denominador_9 = a_frac - (b_frac / c_frac)
r_result = numerador_9 / denominador_9

print("--- Ejercicio 9 ---")
print(f"Resultado de r = {r_result}\n")


# EJERCICIO 10: Expresión Fraccionaria II
a_10, b_10, c_10, d_10 = 10, 4, 2, 8
num_10 = ((a_10 + b_10) ** 2) - ((c_10 + d_10) ** 2)
den_10 = (a_10 * c_10) / (b_10 * d_10)
m = num_10 / den_10

print("--- Ejercicio 10 ---")
print(f"Resultado de m = {m}")