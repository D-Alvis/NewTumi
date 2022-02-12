ip=int(input("¿Escribe tu primera IP?:"))
if ip >=0 and ip <128:
    print("CLASE A")
if ip >=128 and ip <192:
    print("CLASE B")
if ip >=192 and ip <224:
    print("CLASE C")
elif ip >=224 and ip <240:
    print("CLASE D")
elif ip >=240 and ip <=255:
    print("CLASE E")
else:
    print("IP NO VALIDA")
