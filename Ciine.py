from ast import Return
from calendar import c
from re import A


print ("Bienvenido a CineDuoc.")
print ("\t\t\t\t\t\t\t\t")
print ("¿Usted es funcionario o estudiante de Duoc UC?")
print ("\t\t\t\t\t\t\t\t")
respuesta = input ("SI / NO: ")
print ("\t\t\t\t\t\t\t\t")
if respuesta=="SI" or respuesta=="si":
    print ("Usted si pertenece a la institución, por favor muestre su identificación.")
else: 
    print ("Usted no pertenece a la institución.")
print ("\t\t\t\t\t\t\t\t")
print ("¿Que entrada desea?, las entradas disponibles son:")
print ("\t\t\t\t\t\t\t\t")
print ("Normal -> $2.900")
print ("Estreno -> $4.800")
print ("\t\t\t\t\t\t\t\t")
entrada = input ("Normal / Estreno: ")
print ("\t\t\t\t\t\t\t\t")
if entrada=="Normal" or entrada=="normal":
    print("Usted escogió entrada normal. ")
else:
    print("Usted escogió entrada estreno. ")
print ("\t\t\t\t\t\t\t\t")
cantidad = input ("¿Cuántas entradas desea? ")
print ("\t\t\t\t\t\t\t\t")
if int (cantidad) <= 1:
    print(f"Usted escogió {cantidad} entrada.")
else:
    print (f"Usted escogió {cantidad} entradas.")
    print ("\t\t\t\t\t\t\t\t")
palomitas = input ("¿Desea agregar palomitas de maíz a su pedido?. ")
print ("\t\t\t\t\t\t\t\t")
if palomitas=="SI" or palomitas=="si":
    print ("Tenemos disponibles las siguientes palomitas: ")
    print ("\t\t\t\t\t\t\t\t")
    print ("Palomitas Pequeñas -> $2.500")
    print ("\t\t\t\t\t\t\t\t")
    print ("Palomitas Medianas -> $4.500")
    print ("\t\t\t\t\t\t\t\t")
    print ("Palomitas Grandes -> $7.800")
    print ("\t\t\t\t\t\t\t\t")
    tipopalomita = input ("¿Cuál de las 3 desea?: ")
    print ("\t\t\t\t\t\t\t\t")
    if tipopalomita=="Pequeñas" or tipopalomita=="Pequeña" or tipopalomita=="pequeñas" or tipopalomita=="pequeña":
        cantidadpalomitas = input ("¿Cuántas palomitas pequeñas desea?: ")
    if tipopalomita=="Medianas" or tipopalomita=="Mediana" or tipopalomita=="medianas" or tipopalomita=="mediana":
        cantidadpalomitas = input ("¿Cuántas palomitas medianas desea?: ")
    if tipopalomita=="Grandes" or tipopalomita=="Grande" or tipopalomita=="grandes" or tipopalomita=="grande":
        cantidadpalomitas = input ("¿Cuántas palomitas grandes desea?: ")
    print ("\t\t\t\t\t\t\t\t")
    pregunta = input ("¿Desea agregar más palomitas?: ")
    if pregunta=="SI" or pregunta=="si":
        def return_47():
            return 47