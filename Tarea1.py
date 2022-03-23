from ast import parse
from re import A


nom = input ('Ingrese su nombre.')
ape = input ('Ingrese su apellido.')
edad = input ('Ingrese su edad.')
num1 = input ('Ingrese primero num')
num2 = input ('Ingrese segundo num')
suma = int(num1) + int(num2)
print (f'Hola: {nom}')
print (f'Apellido: {ape}')
print (f'Su edad es: {edad}')
print (f'Resultado de la suma de {num1} y {num2} es: {suma}')