# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el 
# número de céntimos del precio introducido.

floatPrecio = input("Introduce el precio de un producto con dos decimales: ")
# Antes de la coma son los Euros
strEuros = floatPrecio[:floatPrecio.find('.')] 
# Depues de la coma son los Centimos
strCentimos = floatPrecio[floatPrecio.find('.')+1:]
print( "El producto vale, " +strEuros, 'euros y',strCentimos , 'céntimos.')
