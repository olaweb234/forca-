
from random import randint

palavras = ['papaia', 'mula', 'adulto', 'criança']
pc = randint(0, 3)
palavra_secreta = palavras[pc]
letra_usu = []
chances = 4
ganhou = False

while True:
    for letra in palavra_secreta:
        if letra in letra_usu:
            print(letra, end=' ')
        else:
            print("-", end=' ')

    print(f'Você ainda tem {chances} chances.')
   
    tentativa = str(input('Escolha sua letra: '))
    
    letra_usu.append(tentativa)
    if tentativa not in palavra_secreta:
        chances -= 1

    ganhou = True

    for letra in palavra_secreta:
        if letra not in letra_usu:
            ganhou = False
            break

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Você ganhou e a palavra era {palavra_secreta}.")
else:
    print(f'Você perdeu e a palavra era {palavra_secreta}.')

        