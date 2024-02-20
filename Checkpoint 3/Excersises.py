#Excercise 1: Create a string, number, list, and boolean, each stored in their own variable.
string_variable = "Esto es un string"
number_variable = 6
list_variable = ['rojo','verde','amarillo','azul', 6, True]
boolean_variable = True

#Exercise 2:  Use an index to grab the first 3 letters in your string, store that in a variable. 
string_variable  = "Esto es un string"
three_letter_of_string_variable = string_variable[0:3]
print(three_letter_of_string_variable)

#Exercise 3: Use an index to grab the first element from your list.
list_variable = ['rojo','verde','amarillo','azul', 6, True]
firt_element_of_list_variable = list_variable[0]
print(firt_element_of_list_variable)

# Exercise 4: Create a new number variable that adds 10 to your original number.
number_variable_two = number_variable + 10
print(number_variable_two)

#Exercise 5: Use an index to get the last element in your list.
list_variable = ['rojo','verde','amarillo','azul', 6, True]
last_element_of_list_variable = list_variable[-1]
print(last_element_of_list_variable)

#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')
print(list_of_names)

'''
Exercise 7: Get the first word from your string using indexes. 
Use the upper function to transform the letters into uppercase. 
Create a new string that takes the uppercase word and the rest of the original string.
'''
string_variable = "Esto es un string"
first_word = string_variable[0:4]
first_word = first_word.upper()
new_string = first_word + string_variable[4:]
print(new_string)

#Exercise 7.1: Dynamic behavior
string_variable = "Externo es un string"
primera_palabra, _, resto_frase = string_variable.partition(' ')
new_string = primera_palabra.upper() + _ + resto_frase
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
number_variable = 6
string_interpolation_example = f'Esto es una ejemplo de string interpolation en el que introducimos el número {number_variable}'
print(string_interpolation_example)

#Exercise 9: Print “hello world”.
print('hello world')
