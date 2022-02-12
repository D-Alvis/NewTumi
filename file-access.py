file=open('devices.txt', 'a')
while True:
    NewItem = input('Ingresa nuevo dispositvo: ')
    if NewItem == "q":
        print("Todo listo!")
        break
    file.write(NewItem + '\n')
file.close()



   