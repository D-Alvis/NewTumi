Puertos=int(input("¿Que puerto utilizas? "))
if Puertos >=0 and Puertos <=1023:
    print("Este es un puerto conocido. ")
elif Puertos >=1024 and Puertos <=49151:
    print("Este es un puerto registrado. ")
elif Puertos >=49152 and Puertos <=65535:
    print("Este es un puerto privado")
else:
    print("El puerto indicado no existe")