from Admon.AdmonFuentes import AdmonFuentes

class Entrada:

    #Constuctor
    def __init__(self):
        print('Objeto tipo Entrada creado y listo para usarse..!!')
        self.menu()

    # métodos
    def menu(self):
        opcion = -1
        while opcion != 0:
            print('==================================')
            print('............OPCIONES..............')
            print('==================================')
            print('0. Salir')          
            print('1. FUENTES DE FINANCIACION')
            print('2. PROFESORES')
            print('3. DEPARTAMENTOS')
            print('4. PROYECTOS')
            print('5. PROGRAMAS')
            print('6. PARTICIPACION PROYECTOS')
            print('7. FINANCIACION PROYECTOS')
            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                print("Adios ..!!")

            elif opcion == 1:
                AdmonFuentes()

            else:
                print('Esa opción NO existe..!!!')


Entrada()
