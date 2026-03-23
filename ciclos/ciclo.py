nombres = []

# print(nombres[2])




# for nombre in nombres:
#     print(nombre)



while True :
    
    
    print(f"""
                    menu
          1.Agregar nombres a la lista
          2.Mostrar nombres
          3.Eliminar listas
          4.Salir""")
    
    
    opcion = input("Ingrese la opcion: ")

    if opcion == "1":

        nuevonombre = nombres.append(input("Ingrese el nombre: "))
        

    elif opcion == "2":
        print(nombres)

    elif opcion =="3":
        nombres.clear()

    elif opcion == "4":
        print("Saliendo")
        break

    else:
        print("Opcion no valida")

        