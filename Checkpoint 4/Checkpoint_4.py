#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
mi_lista = ['Hola','Qué','Tal','Estás']
mi_tupla = ('a','b','c','d')
num_float = 6.8
num_integer = 10
mi_diccionario = {
    'a':[1,2,3,4],
    'b':[1,2,3,4],
    'c':[1,2,3,4]
}

from decimal import Decimal
num_decimal = Decimal(6.8)

#Exercise 2: Round your float up.
import math
print(math.ceil(num_float))

#Exercise 3: Get the square root of your float.
print(math.sqrt(num_float))

#Exercise 4: Select the first element from your dictionary.
first_element = (list(mi_diccionario.items())[0])
print(first_element)

#Exercise 5: Select the second element from your tuple.
second_element = mi_tupla[1]
print(second_element)

#Exercise 6: Add an element to the end of your list.
mi_lista.append('?')
print(mi_lista)

#Exercise 7: Replace the first element in your list.
mi_lista[0] = 'Buenos días'
print(mi_lista)

#Exercise 8: Sort your list alphabetically.
mi_lista_sorted = sorted(mi_lista,reverse=True)
print(mi_lista_sorted)

#Exercise 9: Use reassignment to add an element to your tuple.
mi_tupla = list(mi_tupla)
mi_tupla += ['otra letra']
mi_tupla = tuple(mi_tupla)
print(mi_tupla)