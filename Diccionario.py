import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": " una respuesta a una broma",
            "SHEESH": "una ligera desaprobación",
            "CREEPY": "algo que es aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
while True:            
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("perdon no se encuentra esa palabra en nuestro extenso diccionario")
        # ¿Qué hacer si no se encuentra la palabra?
    continuar = input("¿quieres continuar? si/no")
    if continuar == "si":
        time.sleep(1.5)
    elif continuar == "no":
        print("ok. Vete humano")
        break
    else:
        print("solo eran dos letra y las escribes mal. Hasta la vista baby")
        break
    
print("fin, ya no hay nada mas aquí")
time.sleep(5)
print("porque sigues aquí")
time.sleep(10)
print("me aburro te dejo ya, hasta nunca")
