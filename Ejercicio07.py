# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre
#  (la parte delantera de la arroba @) pero con dominio ceu.es.

strEmail = input("Introduce un correo electrónico: ")
print(strEmail[:strEmail.find('@')] + '@ceu.es')