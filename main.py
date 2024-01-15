import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobacion",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
            
word = input("¡Hola! Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("El significado es:", meme_dict[word])
else:
    print("Esta palabra no se encuentra en el diccionario, lo lamento :c")
