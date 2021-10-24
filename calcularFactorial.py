Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def factorial(numero): 
    if int(numero) < 0: 
        print("Factorial no se puede calcular a un negativo")
    elif numero == 0: 
        return 1
    else: 
        factorial = 1
        while(numero > 1): 
            factorial *= numero 
            numero -= 1
        return factorial

    
numero=int(input("Ingree un número: "))
Ingree un número: 5
print("Factorial de",numero," es: ", factorial(numero))
Factorial de 5  es:  120
