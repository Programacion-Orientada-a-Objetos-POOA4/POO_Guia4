import time
class Interfaz:
    def cargando(self):
        carga = "Cargando"
        for i in range(4):
            print(carga + "." * i, end="\r")
            time.sleep(0.5)  
        print("---------------------------------")
class Juegos(Interfaz):

    def run(self):
        while True:
            opciones=int(input("Seleccione la opcion que desea realizar: \n1. Entrar\n2. Salir\n"))
            if opciones==1:
                while True:
                    juego=int(input("Seleccione el juego que desea jugar: \n1. Bomberman\n2. Snake\n3. Puñogranada\n4. Inicio\n"))
                    if juego==1:
                        self.cargando()
                        print("BOMBERMAN")
                        while True:
                            opcion=int(input("¿jugar (1) o salir (2)?: "))
                            if opcion==1:
                                self.cargando()
                                print("jugaste BOMBERMAN")
                                while True:
                                    opcion_INTERNA=int(input("¿Desea guardar su progreso? YES(1) NO(2): "))
                                    if opcion_INTERNA==1:
                                        print ("PROCESO GUARDADO")
                                        break
                                    elif opcion_INTERNA==2:
                                        break
                            elif opcion==2:
                                break


                    elif juego==2:
                        self.cargando()
                        print("SNAKE")
                        while True:
                            opcion=int(input("¿jugar (1) o salir (2)?: "))
                            if opcion==1:
                                self.cargando()
                                print("jugaste SNAKE")
                                while True:
                                    opcion_INTERNA=int(input("¿Desea guardar su progreso? YES(1) NO(2): "))
                                    if opcion_INTERNA==1:
                                        print ("PROCESO GUARDADO")
                                        break
                                    elif opcion_INTERNA==2:
                                        break
                            elif opcion==2:
                                break
                    elif juego==3: 
                        self.cargando()
                        print("PUÑOGRANADA")
                        while True:
                            opcion=int(input("¿jugar (1) o salir (2)?: "))
                            if opcion==1:
                                self.cargando()
                                print("jugaste PUÑOGRANADA")
                                while True:
                                    opcion_INTERNA=int(input("¿Desea guardar su progreso? YES(1) NO(2): "))
                                    if opcion_INTERNA==1:
                                        print ("PROCESO GUARDADO")
                                        break
                                    elif opcion_INTERNA==2:
                                        break
                            elif opcion==2:
                                break
                    elif juego==4:
                        break
                    else:
                        print("Selecciona una opcion correcta...")
                        print("---------------------------------")

            elif opciones==2:
                print("Hasta luego!")
                break
            else:
                print("Selecciona una opcion correcta...")
                print("---------------------------------")

usuario=Juegos()
usuario.run()
