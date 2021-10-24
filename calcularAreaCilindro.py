Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
area = 0.0
def calcular_area(v_radio):
    return ((3.1416) * pow(v_radio,2))

area = calcular_area(float(input("Ingrese el radio: ")))
Ingrese el radio: 0.5
print("El área del circulo es: " + str(area))
El área del circulo es: 0.7854

altura= float(input("Ingrese la altura: "))
Ingrese la altura: 3
volumen=altura * area
print("El volumen del cilindro es: " + str(volumen))
El volumen del cilindro es: 2.3562
