# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase
#  pero con la vocal introducida en mayúscula.

strFrase = input("Introduce una frase: ")
strVocal = input("Introduce una vocal:  ")
print(strFrase.replace(strVocal, strVocal.upper()))