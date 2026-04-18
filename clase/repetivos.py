def main():
    while True:
        print("""\nElija La Opcion Deseada:
        
1. Eliminar Caracteres Repetidos
2. Funcion De Histograma
3. Encontrar Elementos Comunes
4. Salir
""")

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese un numero valido")
            continue

        if opcion == 1:
            texto_usuario = input("Ingrese el texto: ")
            print("Resultado:", unrepeated(texto_usuario))

        elif opcion == 2:
            numeros = list(map(int, input("Ingrese numeros separados por espacio: ").split()))
            caracter = input("Ingrese el caracter para el histograma: ")
            print(histogram(numeros, caracter))

        elif opcion == 3:
            lista1 = input("Ingrese la primera lista (separada por espacios): ").split()
            lista2 = input("Ingrese la segunda lista (separada por espacios): ").split()
            print("Elementos comunes:", comunes(lista1, lista2))

        elif opcion == 4:
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")


def unrepeated(texto):
    vistos = set()
    resultado = ""

    for caracter in texto:
        if caracter not in vistos:
            vistos.add(caracter)
            resultado += caracter

    return resultado


def histogram(numeros, caracteres):
    resultado = ""

    for n in numeros:
        resultado += caracteres * n + "\n"

    return resultado


def comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))


main()