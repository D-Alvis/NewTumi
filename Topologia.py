routers=["AR_1", "AR_HUB", "AR_3", "AR_2"]
S3=["AC1"]
Switches=["ASw11", "ASw12", "ASw31", "ASw32", "ASw2", "AP1"]
ipaddressR= {"AR_1":"192.168.1.1/23", "AR_HUB":"130.0.0.253/30", "AR_3":"131.0.0.254/30", "AC1":"200.0.0.1/28", "AR_2":"200.0.0.6/28"}
ipaddressR["AR_1"]=["192.168.1.1/23","172.16.0.1/20","130.0.0.254/30","200.0.0.3/28"]
ipaddressR["AR_HUB"]=["130.0.0.253/30","131.0.0.253/30","200.0.0.4/28"]
ipaddressR["AR_3"]=["131.0.0.254/30","192.168.10.1/25","10.0.0.1/27"]
ipaddressR["AC1"]=["200.0.0.1/28","200.0.0.2/28","200.0.0.5/28"]
ipaddressR["AR_2"]=["200.0.0.6/28","172.16.10.1/25"]
ipaddressS={"ASw11":"192.168.1.11" , "ASw12":"172.16.0.11/24", "ASw31":"192.168.10.11", "ASw32":"10.0.0.11/27", "ASw2":"172.16.10.11", "AP1":"172.16.10.12"}
userREQ=input("¿Escoge Que dispositivo quieres ver su IP: ROUTERS, SWITCHES: ")
if userREQ == "ROUTERS":
    print(ipaddressR)
elif userREQ == "SWITCHES":
    print(ipaddressS)
else:
    print("ESTE ES UN DISPOSITIVO INVÁLIDO, INTENTELO MÁS TARDE")
