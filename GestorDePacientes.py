import os

#Limpia la consola.
def LimpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

#Clase cola, encola, desencola y determina si está vacía.
class  Cola:
    def __init__(self):
        self.elementos = []
#Encola el paciente.
    def encolar(self, item):
        self.elementos.append(item)
#Desencola el paciente.
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacia")
#Determina si la cola está vacia.
    def esta_vacia(self):
        return len(self.elementos) == 0

#Pacientes predeterminados en la cola.
cola = Cola()
cola.encolar('Juan')
cola.encolar('Melissa')
cola.encolar('Pedro')

#Clase Menú, muestra la interfaz de texto al usuario.
class Menu:
    def __init__(self):
        self.Opciones = {
            '1': ('Registra paciente', self.Opcion_1),
            '2': ('Siguiente paciente', self.Opcion_2),
            '3': ('Lista de pacientes', self.Opcion_3),
            '4': ('Salir', self.Salir)
        }

#Muestra el menú.
    def Mostar_Menu(self):
        print('Seleccione una opción:')
        for key in sorted(self.Opciones):
            print(f' {key}) {self.Opciones[key][0]}')

#Lee la elección del usuario.
    def Leer_Eleccion(self):
        while True:
            choice = input('Opción: ')
            if choice in self.Opciones:
                return choice
            print('Opción incorrecta, vuelva a intentarlo.')

#Ejecuta la elección del usuario.
    def Ejecutar_Eleccion(self, option):
        self.Opciones[option][1]()

#Genera todo el menú.
    def CrearMenu(self):
        while True:
            LimpiarConsola()
            print('===============================================')
            print('== Bienvenido al gestor del sistema de salud ==')
            print('===============================================\n')
            self.Mostar_Menu()
            option = self.Leer_Eleccion()
            if option == '4':
                break
            self.Ejecutar_Eleccion(option)
            input('Presione Enter para continuar...')
            LimpiarConsola()

#Número 1 - Añade pacientes.
    def Opcion_1(self):
        print('Has elegido la opción 1')
        PacienteAgregar = input('Escriba el paciente a agregar\n')
        cola.encolar(PacienteAgregar);
        print("Paciente agregado:", PacienteAgregar)

#Número 2 - Siguiente paciente.
    def Opcion_2(self):
            try:
                print('Has elegido la opción 2')
                Paciente = cola.desencolar()
                print("Paciente atendido:", Paciente)
            except IndexError:
                print("Ya no hay pacientes en espera.")

#Número 3 - Muestra la lista de pacientes.
    def Opcion_3(self):
        print('Has elegido la opción 3')
        if not cola.esta_vacia():
            print("Lista de pacientes en la cola:")
            for paciente in cola.elementos:
                print("-", paciente)
        else:
            print("La cola está vacía. No hay pacientes en espera.")

#Número 4 - Cierra el programa.
    def Salir(self):
        print('¡Nos vemos pronto!')

if __name__ == '__main__':
    menu = Menu()
    menu.CrearMenu()
