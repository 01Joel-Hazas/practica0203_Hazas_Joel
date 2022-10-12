# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

strFecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")

def mostrarDiaMesAño(strFecha:str):
    dia = strFecha[:2]
    mes = strFecha[3:5]
    año = strFecha[6:]
    return "El dia de tu fecha de nacimiento es " + dia + " con mes " + mes + " y año " + año
print(mostrarDiaMesAño(strFecha))