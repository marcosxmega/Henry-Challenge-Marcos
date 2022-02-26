# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

from math import factorial
from operator import truediv
from re import I
from turtle import color


def ListaEnteros(inicio, tamanio):
    '''
    Esta función devuelve una lista de números enteros
    Recibe dos argumentos:
        inicio: Numero entero donde inicia la lista
        tamanio: Cantidad de números enteros consecutivos
    Ej:
        ListaEnteros(10,5) debe retornar [10,11,12,13,14]
    '''
    lista = []
    for i in range(inicio, inicio + tamanio):
        lista.append(i)
    return lista

def DividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    parte_entera = int(dividendo / divisor)
    resto = dividendo % divisor 
    return parte_entera, resto

def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    def invert(n):
        numero = 0
        while n != 0:
            numero = 10 * numero + n % 10
            n //= 10
        return numero
    num_inv = invert(numero)
    if type(numero) == int:
        if numero == num_inv:
             return True 
        else:
             return False
    else:
         return None

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    fact = 1
    
    if type (numero)==int and numero > 0:
        for i in range(1,numero+1):
            fact*=i 
        return fact
    else:
        return None        
def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    def primo(nro):
        es_primo = True
        for i in range(2,nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    if primo(actual_primo) == True:
        return min([a for a in range(actual_primo +1,actual_primo*2)if primo(a)])
    else:
        return None   

def factorizar_numero(numero):
    '''
    Esta función recibe como parámetro un número entero mayor a cero y devuelva dos listas, 
    una con cada factor común y otra con su exponente, 
    esas dos listas tienen que estar contenidas en otra lista.
    En caso de que el parámetro no sea de tipo entero y/ó mayor a cero debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se hará la factorización.
    Ej:

        factorizar_numero(12) debe retornar [[2,3],[2,1]]
        factorizar_numero(13) debe retornar [[13],[1]]
        factorizar_numero(14) debe retornar [[2,7],[1,1]]
    '''
    if (type(numero)!=int):
        return None
    if (numero < 1):
        return None
    lista_primos = []
    i = 2 
    while (i < (int(numero/2)+1)):
        primo = True 
        j=2
        while (j < i):
            if(i%j == 0):
                primo = False
                break
            j+=1
            if(primo):
                lista_primos.append(i)
                i+=1
            lista_factores = []
            lista_exponentes = []
            numero_original = numero 
            for i in lista_primos:
                j=0
                while (numero % i == 0):
                    numero=numero/i
                    if (j==0):
                        lista_factores.append(i)
                    j+=1
                if (j>0):
                    lista_exponentes.apped(j)
                if(len(lista_factores)==0):
                    return[[numero_original],[1]] 
                else:
                        return[lista_factores,lista_exponentes]          


def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    class Animal :
        def __init__(self, especie,color):
            self.especie =especie
            self.color= color
            self.edad=0
        def CumplirAnios(selft):
            selft.edad +=1
            return selft.edad
    a = Animal(especie,color)
    return a     

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    
    if type(numero) == int and numero > 0:
        return int(format(numero,"b"))
    else:
            return None