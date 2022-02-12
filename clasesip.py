name = input("Cual es tu primer nombre? ")
lastname = input("Cual es tu apellido? ")
peso = int(input("¿Cuanto estas pesando? "))
age = int(input("Cuantos años tienes? "))
type=str(peso)
type=str(age)
if age >= 17 and peso >= 75:
    print("Hola " + name, lastname, "tu peso no es el ideal para tu edad")
else:
    print("Tu peso es el correcto para tu edad")
