# Proyecto: Calculadora Básica en Python
# Autor: Thiago Guevara

print("=================================")
print("      CALCULADORA BÁSICA")
print("=================================")

while True:

    print("\nSeleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Opción: ")

    # Salir del programa
    if opcion == "5":
        print("Gracias por utilizar la calculadora.")
        break

    # Validación de opciones
    if opcion in ["1", "2", "3", "4"]:

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

        elif opcion == "4":
            if num2 == 0:
                print("Error: No se puede dividir para cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")

    else:
        print("Opción no válida.")
