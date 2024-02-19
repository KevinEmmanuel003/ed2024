#Clase que representa un nodo dentro de la cola, contiene un next y un prev.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

#Clase que representa una cola doblemente circular.
class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None
#Inserta un valor dado al final de la cola.
    def insertar(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

        print(f"Se insertó el valor {value}")
#Elimina el primer nodo de la cola.
    def eliminar(self):
        if not self.head:
            print("La cola está vacía")
            return
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

        print(f"Se eliminó el valor {value}")
#Muestra todos los elementos de la cola, desde next hasta volver a head.
    def mostrar(self):
        if not self.head:
            print("La cola está vacía")
            return
        current = self.head
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Crear una cola circular
cola = CircularQueue()

# Insertar elementos
cola.insertar(1)
cola.insertar(2)
cola.insertar(3)

# Mostrar la cola
cola.mostrar()

# Eliminar un elemento
cola.eliminar()

# Mostrar la cola después de la eliminación
cola.mostrar()
