import random, time
caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    longitud = int(input("¿cuantos caracteres quieres para tu contraseña?"))
    time.sleep(1)
    password = ""
    print("generando contraseña")
    time.sleep(2)
    for i in range(longitud):
        caracter_random = random.choice(caracter)
        password += caracter_random
    print("contraseña genereda de manera random:", password)
    continuar = {}
    continuar[1] = "si"
    continuar[2] = "no"
    print(continuar)
    continuar = int(input("quieres generar otra contraseña: "))
    if continuar == 1:
        print("ok") 
        time.sleep(1)  
        print("volviendo al incio...")
        time.sleep(2)  
    elif continuar == 2:
        print("espero que te sirva mi contraseña, un placer haberte ayudado, adios")
        break
    else:
        print("ERROR370.2:solo tenias que poner un numero")
        time.sleep(2)
        print("ordenador en peligro por procesamiento erroneo")
        time.sleep(3)
        print("PC eliminado, hasta nunca Bye")
        break
        
time.sleep(30)
print("dije que adios")
