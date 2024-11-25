class Busqueda:
    @staticmethod
    def busqueda_binaria(lista, objetivo):
        inicio = 0
        fin = len(lista) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            if lista[medio] == objetivo:
                return medio
            elif lista[medio] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return -1

    @staticmethod
    def busqueda_secuencial(lista, objetivo):
        indices = [] 

        for i in range(len(lista)):
            if lista[i] == objetivo:
                indices.append(i) 

        if indices:
            return indices
        else:
            return -1

    def menu(self):
        lista = [1,2,3,4,5,6,7,8,9,10]
        print (lista)

        while True:
            print("\n--- Menú de Búsqueda ---")
            print("1. Búsqueda Binaria")
            print("2. Búsqueda Secuencial")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                # Búsqueda Binaria
                objetivo = int(input("Introduce el número a buscar: "))
                resultado = self.busqueda_binaria(lista, objetivo)
                if resultado != -1:
                    print(f"El número {objetivo} se encuentra en la posición {resultado}.")
                else:
                    print(f"El número {objetivo} no se encuentra en la lista.")

            elif opcion == "2":
                # Búsqueda Secuencial
                objetivo = int(input("Introduce el número a buscar: "))
                resultado = self.busqueda_secuencial(lista, objetivo)
                if resultado != -1:
                    print(f"El número {objetivo} se encuentra en las posiciones: {resultado}.")
                    if len(resultado) > 1:
                        print(f"El número {objetivo} aparece {len(resultado)} veces en la lista.")
                else:
                    print(f"El número {objetivo} no se encuentra en la lista.")

            elif opcion == "3":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intenta nuevamente.")

busqueda = Busqueda()
busqueda.menu()
