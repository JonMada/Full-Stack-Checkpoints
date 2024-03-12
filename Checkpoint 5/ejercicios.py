# Cree un bucle For de Python.
nums = range(1,100)
lista_numeros_impares = [num for num in nums if num % 2 != 0 ]
print(lista_numeros_impares)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma (num1,num2,num3):
    return(num1 + num2 + num3)


resultado = suma(1,10,2)
print(resultado)

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
resultado = lambda num1,num2,num3: num1 + num2 + num3

def suma(result):
    print(result)


suma(resultado(1,10,2))

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for nombre_en_lista in lista_nombre:
    if nombre_en_lista == nombre:
        print(f'La variable con valor {nombre} coincide con algún elemento de la lista')
        break
else:
    print (f'La variable {nombre} no coincide con ningún elemento de la lista')