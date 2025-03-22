
# Tipos de datos
# Enteros
123

#flot
123.45

# string
"123"

variable = "Texto con formato"

texto_concatenado = "Texto " + "Texto2"
"{}".format(variable)

# Format string
f"Este es un mensaje con formato {variable}"

#boolean
True
False

#list
lista = [1,2,3,4,5]
lista.append(6)
lista.extend([5,6,7])
lista.pop(0)
lista.remove(2)


# diccionario
{ "nombre": "Juan", "edad": 25, "ciudad": "Buenos Aires" }

# Tupla 
(1,2,3,4,5)

# Vacio
None

lista = []

for i in range(10):
    lista.append(i)

# Copia profunda
lista2 = lista.copy()


def foo(variable=[]):
    print(id(variable))
    variable.append(1)
    return variable


def foo2(variable=None):
    if variable is None:
        variable = []
    print(id(variable))
    variable.append(1)
    return variable





class Vehiculo:
    def __init__(self, marca, modelo):
        print("Vehiculo")
        self.marca = marca
        self.modelo = modelo


class Auto(Vehiculo):
    def __init__(self, marca, modelo, rodado):
        # Extendiendo
        super().__init__(marca, modelo)
        print("Auto")
        self.rodado = rodado


class Moto(Vehiculo):
    def __init__(self, cilindrada):
        # Sobreescribiendo
        print("Moto")
        self.cilindrada = cilindrada

vehiculo = Vehiculo("Ford", "Fiesta")
auto = Auto("Ford", "Fiesta", "17")
moto = Moto("150cc")

print(auto.marca)
print(auto.modelo)
print(auto.rodado)


class Sector:
    pass

class IT(Sector):
    def __str__(self):
        return "IT"
    pass

class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.sector = IT() # Composición

empleado = Empleado("Juan", "Perez")
print(empleado.nombre)
print(empleado.apellido)
print(empleado.sector)



# Abstracción
class SerHumano:
    def caminar(self):
        pass
    
    def hablar(self):
        pass

    def pensar(self):
        pass


class Persona(SerHumano):
    def caminar(self):
        print("Caminando")
    
    def hablar(self):
        print("Hablando")

    def pensar(self):
        print("Pensando")

# Encapsulamiento
class Robot:
    def __init__(self):
        # Mililitros
        # Variable privada tienen _
        self._aceite = 1000
        self._maximo_aceite = 5000

    @property
    def nivel_aceite(self):
        # Getter
        # Solo lectura
        return self._aceite

    def cargar_aceite(self, cantidad):
        # Setter
        if self._aceite < self._maximo_aceite:
            self._aceite += cantidad
        return self._aceite

robot = Robot()

print(robot.nivel_aceite)
robot.nivel_aceite = 2000
print(robot.cargar_aceite(1000))

