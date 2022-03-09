import os
import random
import sys

def read():
    words = []
    with open("./Files/words.txt", "r", encoding="utf-8") as f:
        words = [word.upper().replace('\n','') for word in f]
    word = wordRandom(words)
    return word

def wordRandom(listWords):
    randomNumber = random.randint(0, len(listWords)-1)
    return listWords[randomNumber]

def recorrerPalabra(wordRecorrer,intentos, diccionario):
    while intentos > 0:
        os.system("clear")
        for k,v in diccionario.items():
            print(' '+v+' ',end='')
        print('')
        print('*********************************')
        print(f"Tiene un total de intentos de: {intentos}")
        print('*********************************')
        print('')
        
        try:
            inputLetter = input("Ingrese una letra: ").upper()
            assert inputLetter.isalpha(), "Debes Digitar SOLO una LETRAS"
            assert len(inputLetter) == 1, "Digita UNA letra"
        except AssertionError as ae:
            print(ae)
        for key,value in enumerate(wordRecorrer):
            if value == inputLetter:
                diccionario[key] = inputLetter
        actual = intentos
        contador = 0
        for value_ in diccionario.values():
            if inputLetter == value_:
                # intentos = intentos + 1
                intentos = actual + 1
            if ' ___ ' == value_:
                contador = contador + 1
        if contador > 0:
            intentos = intentos - 1
        else:
            return 1
        
        print('')

WORDGLOBAL = read()

def run(WORD):
    intentos = len(WORD)
    print(WORD)
    showLetter = {}
    for i in range(0, intentos):
        showLetter[i] = ' ___ '
    fin = recorrerPalabra(WORD,intentos, showLetter)
    if fin != 1:
        print("CHAO, SE MURIO")
        print("Se te acabaron los intentos: 0")
        print(f"Respuesta correcta: {WORD}")
        return
    print("FELICIDADESSSS!!!!!!")
    print(f"Respuesta correcta: {WORD}")
    

if __name__ == "__main__":
    run(WORDGLOBAL)