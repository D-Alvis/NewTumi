company=input("¿Nombre de la compañia?: ")
cotizador=int(input("¿Cuantos cotizadores?: "))
web=("https://adminsoft.tumi-soft.com/login")
dominio=(".com")
admin=("admin@"+company+dominio)
contador=("contador@"+company+dominio)
ventas=("ventas@"+company+dominio)
password=("tumipos2022")
cotizador1=("cotizador@"+company+dominio)
cotizador2=("cotizador2@"+company+dominio)
cotizador3=("cotizador3@"+company+dominio)
print(""
 "")
print("CREDENCIALES: ")
print(" ")
print("WEB: "+web)
print(" ")
print("ADMINISTRADOR = "+admin)
print("CONTADOR = "+contador)
print("VENTAS = "+ventas)
if cotizador == 1:
    print("COTIZADOR =" +cotizador1)
if cotizador == 2:
    print("COTIZADOR1 = "+ cotizador1)
    print("COTIZADOR2 = "+ cotizador2)
if cotizador ==3:
    print("COTIZADOR1 = "+ cotizador1)
    print("COTIZADOR2 = "+ cotizador2)
    print("COTIZADOR3 = "+ cotizador3)
else:
    False
print(" ")
print("CONTRASEÑA TODOS LOS USUARIOS: ", password)

    


