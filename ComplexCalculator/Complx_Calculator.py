"""
ARCHIVO Complx_Calculator QUE LLEVA UNA CLASE PRINCIPAL Complx, Y TIENE 2 SUBCLASES DE TIPO COMPLEJO (Complx) LLAMADAS
Cartesian y Pol, EN LAS QUE SE DESARROLLAN TODAS LAS OPERACIONES ENTRE NUMEROS COMPLEJOS, Y EN DONDE SE DESCRIBE SU FUNCIONAMIENTO.
PARA PODER INICIALIZAR NUMEROS DE TIPO COMPLEJO SE DEBERÁ HACER, POR EJEMPLO, DE LA SIGUIENTE MANERA:
- c = Cartesian((4, 8)) que representa el complejo cartesiano 4 + 8i
- c = Pol((2, 45)) que representa el complejo polar con magnitud 2 y angulo de 45 grados
EL ARGUMENTO SIEMPRE DEBE SER UNA TUPLA CON 2 ELEMENTOS DE TIPO NUMERICO: int O float.

PARA AMPLIAR INFORMACION SOBRE COMO UTILIZAR TODOS LOS METODOS, FAVOR REVISAR EL ARCHIVO Main.py PRESENTE
EN EL MISMO DIRECTORIO DEL ACTUAL ARCHIVO.
"""

import math

class Complx(object):
    """
    #############################
    ## CLASE PRINCIPAL: Complx ##
    #############################
    Clase principal Complx, que define un número complejo en forma de tupla sin especificar la correspondencia de cada elemento
    de la tupla, es decir, se define de manera general y sin una definicion de que tipo de complejo."""

    def __init__(self, tupl):
        """
        Constructor de la clase Principal Complx, que recibe una tupla con 2 elementos"""
        self.element_1 = tupl[0]
        self.element_2 = tupl[1]

    def __str__(self):
        """
        Metodo que permite visualizar los complejos como tuplas
        ya sea como cartesiano: (real, imaginario)
        o como polar: (radio, theta)
        Funciona con el metodo print(Complx)"""
        return "(" + str(self.element_1) + ", " + str(self.element_2) + ")"

class Cartesian(Complx):
    """
    ##########################################
    ## SUBCLASE DE TIPO COMPLEJO: Cartesian ##
    ##########################################
    Clase Cartesian, que opera con numeros complejos ordenados en tuplas"""

    def __init__(self, tupl):
        """
        Constructor de la clase Cartesian, que recibe una tupla con dos elementos en donde asigna respectivamente
        la parte real y la parte imaginaria"""
        self.real = tupl[0]
        self.imag = tupl[1]
        """
        Se inicializa con el constructor de la superclase"""
        Complx.__init__(self, tupl)

    def __add__(self, other):
        """
        Método para sumar de la clase Cartesian, que suma 2 numeros de tipo Cartesian
        Utiliza sobrecarga de operadores"""
        return Cartesian((self.real + other.real, self.imag + other.imag))
    
    def __sub__(self, other):
        """
        Método para restar de la clase Cartesian, que resta 2 numeros de tipo Cartesian
        Utiliza sobrecarga de operadores"""
        return Cartesian((self.real - other.real, self.imag - other.imag))

    def __mul__(self, other):
        """
        Método para multiplicar de la clase Cartesian, que multiplica 2 numeros de tipo Cartesian
        Utiliza sobrecarga de operadores"""
        return Cartesian((self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real))

    def div(self, other):
        """
        Método para dividir de la clase Cartesian, que divide 2 numeros de tipo Cartesian"""
        return Cartesian(( ((self.real*other.real)+(self.imag*other.imag))/((self.imag**2)+(other.imag**2)) ,
                        ((self.imag*other.real)-(self.real*other.imag))/((self.imag**2)+(other.imag**2))))

    def conj(self):
        """
        Metodo que devuelve el conjugado de un numero de tipo Cartesian"""
        return Cartesian((self.real, -self.imag))

    def inv(self):
        """
        Metodo que devuelve el inverso aditivo de un numero de tipo Cartesian"""
        return Cartesian((-self.real, -self.imag))

    def pol_to_cart(self):
        """
        Metodo que convierte un complejo de tipo pol a un complejo de tipo Cartesian, es decir
        lo transforma de coordenadas polares a cartesianas"""
        ratio = self.element_1
        theta = self.element_2*(math.pi/180)
        return Cartesian((ratio*math.cos(theta), ratio*math.sin(theta)))

    def mod(self):
        """
        Metodo que devuelve el modulo de un numero de tipo cartesian"""
        return math.sqrt((self.real**2) + (self.imag**2))

class Pol(Complx):
    """
    ####################################
    ## SUBCLASE DE TIPO COMPLEJO: pol ##
    ####################################
    clase pol, que maneja complejos con coordenadas polares"""
    
    def __init__(self, tupl):
        """
        Constructor de la clase pol, que recibe una tupla con dos elementos en donde asigna respectivamente
        el radio r y el ángulo theta"""
        self.ratio = tupl[0]
        self.theta = tupl[1]
        Complx.__init__(self, tupl)

    def cart_to_pol(self):
        """
        Metodo que convierte un complejo de tipo Cartesian a un complejo de tipo Pol, es decir
        lo transforma de coordenadas cartesianas a polares"""
        return Pol(( (Cartesian((self.element_1, self.element_2))).mod(), phase((self.element_1, self.element_2)) ))


def phase(tupl):
    """
    ###########################
    ## FUNCION INDEPENDIENTE ##
    ###########################
    Funcion que recibe una tupla con 2 elementos, que corresponden a la forma cartesiana del número complejo.
    Esta funcion devuelve la fase o el angulo en representacióin polar que corresponde a las componentes recibidas.
    """
    #Casos particulares, angulos rectos
    if tupl[0] == tupl[1] == 0: return 0
    elif tupl[0] == 0 and tupl[1] > 0: return 90
    elif tupl[0] == 0 and tupl[1] < 0: return 270
    elif tupl[1] == 0 and tupl[0] > 0: return 0
    elif tupl[1] == 0 and tupl[0] < 0: return 180
    #Caso general, primer cuadrante
    elif (tupl[0] > 0) and (tupl[1] > 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi)
    #Caso general, segundo y tercer cuadrante
    elif (tupl[0] < 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi) + 180
    #Caso general, cuarto cuadrante
    elif (tupl[0] > 0) and (tupl[1] < 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi) + 360
