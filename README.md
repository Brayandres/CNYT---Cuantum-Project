# CALCULADORA DE NÚMEROS COMPLEJOS
Proyecto del curso CNYT que aborda los temas fundamentales de la programación cuántica y como es el salto de lo clásico a lo cuántico, basado en sistemas y modelos físico-matemáticos.

## HERRAMIENTAS
- Lenguaje De Programación preferido, por ejemplo, PYTHON o JAVA.
- Se debe tener conocimientos de programacion ya que el proyecto debe desarrollrse Con ayuda de este.
- GITHUB: Servicio que permite alojar elementos (Para este caso un programa) versionados y realizar contribuciones y/o progresiones, en donde guardaremos nuestro proyecto.
- Libro guía: "Quantum Computing for Computer Scientists" de Noson S. Yanofsky & Mirco A. Mannucci.

## PRIMERA ENTREGA
Para Esta primera entrega se tiene una calculadora de números complejos que permite realizar distintas operaciones entre ellos para poder operar de manera adecuada.

### REQUISITOS
La librería debe soportar por lo menos las siguientes operaciones entre números complejos:
- Suma
- Producto
- Resta
- División
- Módulo
- Conjugado
- Conversión entre representaciones polar y cartesiano
- Retornar la fase de un número complejo.

### LIBRERÍA
```python
import math

class Complx(object):
    def __init__(self, tupl):
        self.element_1 = tupl[0]
        self.element_2 = tupl[1]

    def __str__(self):
        return "(" + str(self.element_1) + ", " + str(self.element_2) + ")"

class Cartesian(Complx):
    def __init__(self, tupl):
        self.real = tupl[0]
        self.imag = tupl[1]
        Complx.__init__(self, tupl)

    def __add__(self, other):
        return Cartesian((self.real + other.real, self.imag + other.imag))
    
    def __sub__(self, other):
        return Cartesian((self.real - other.real, self.imag - other.imag))

    def __mul__(self, other):
        return Cartesian((self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real))

    def div(self, other):
        return Cartesian( ((self.real*other.real + self.imag*other.imag)/((other.real**2)+(other.imag**2)),
                           (self.imag*other.real - self.real*other.imag)/((other.real**2)+(other.imag**2))) )

    def conj(self):
        return Cartesian((self.real, -self.imag))

    def inv(self):
        return Cartesian((-self.real, -self.imag))

    def cart_to_pol(self):
        return Pol(( (Cartesian((self.element_1, self.element_2))).mod(), phase((self.element_1, self.element_2)) ))

    def mod(self):
        return math.sqrt((self.real**2) + (self.imag**2))

class Pol(Complx):    
    def __init__(self, tupl):
        self.ratio = tupl[0]
        self.theta = tupl[1]
        Complx.__init__(self, tupl)

    def pol_to_cart(self):
        ratio = self.element_1
        theta = self.element_2*(math.pi/180)
        return Cartesian((ratio*math.cos(theta), ratio*math.sin(theta)))

def phase(tupl):
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
```

### PRUEBAS
```python
import math
import unittest
from Complx_Calculator import *

class Test_Complx_Calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(str(Cartesian((1, 4))+Cartesian((-5, -1))), "(-4, 3)")
        #EJERCICIO: (1+4i) + (-5-i)
        self.assertEqual(str(Cartesian((12.5, math.sqrt(2)))+Cartesian((math.pi, math.sqrt(2)))),
                         "(15.641592653589793, 2.8284271247461903)")
        #EJERCICIO: (12.5+(√2)i) + (π+(√2)i)

    def test_sub(self):
        self.assertEqual(str(Cartesian((2, 10))-Cartesian((1.5, -4))), "(0.5, 14)")
        #EJERCICIO: (2+10i)-(1.5-4i)
        self.assertEqual(str(Cartesian((0, -1))-Cartesian((-1, -1))), "(1, 0)")
        #EJERCICIO: (0-i)-(-1-i)

    def test_mul(self):
        self.assertEqual(str(Cartesian((1.5, math.sqrt(2)))*Cartesian((1.5, -math.sqrt(2)))), "(4.25, 0.0)")
        #EJERCICIO: (1.5+(√2)i) * (1.5-(√2)i)
        self.assertEqual(str(Cartesian((2, -2))*Cartesian((1, 1))), "(4, 0)")
        #EJERCICIO: (2-2i) * (1+i)

    def test_div(self):
        self.assertEqual(str(Cartesian((1, -10)).div(Cartesian((10, -1)))), "("+str(20/101)+", "+str(-99/101)+")")
        #EJERCICIO: (1-10i) / (10-i)
        self.assertEqual(str(Cartesian((0, -4)).div(Cartesian((-2, 0)))), "(0.0, 2.0)")
        #EJERCICIO: (0-4i) / (-2+0i)

    def test_mod(self):
        self.assertEqual(Cartesian((2, -3)).mod(), math.sqrt(13))
        #EJERCICIO: |(2, -3)|
        self.assertEqual(Cartesian((math.sqrt(2), math.sqrt(2))).mod(), 2)
        #EJERCICIO: |(√2, √2)|

    def test_conj(self):
        self.assertEqual(str(Cartesian((1.27, -34)).conj()), "(1.27, 34)")
        #COMPLEJO: 1.27-34i
        self.assertEqual(str(Cartesian((18, 0)).conj()), "(18, 0)")
        #COMPLEJO: 18+0i

    def test_phase(self):
        self.assertEqual(phase((0, 1)), 90)
        #COMPLEJO: 0+i
        self.assertEqual(phase((-11, -1)), 185.19442890773482)
        #COMPLEJO: -11-i

    def test_cart_to_pol(self):
        self.assertEqual(str(Cartesian((-4, 2)).cart_to_pol()), "(4.47213595499958, 153.43494882292202)")
        #COMPLEJO: -4+2i
        self.assertEqual(str(Cartesian((-1, -1000000)).cart_to_pol()), "(1000000.0000005, 269.9999427042205)")
        #COMPLEJO: -1-1000000i
        
if __name__ == "__main__":
    unittest.main()
```

### EJECUCIÓN DE LAS PRUEBAS
![alt text](https://github.com/Brayandres/CNYT---Cuantum-Project/blob/master/ComplexCalculator/Images/Pruebas.jpg)


## AUTOR
* **Brayan Macias** - *Develop* -(https://github.com/Brayandres)
