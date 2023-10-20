import random

num_aleatorio = random.randint(1,100)

def compara(teste, numero):
    if teste != numero:
        if teste > numero:
            dica = 'menor'
        else:
            dica = 'maior'
    else:
        dica = 'Acertou!'

    return dica

print('Oi! Pensei em um número de 1 a 100.')

teste = int(input('Você consegue adivinhar?: '))
if teste>100 or teste<1:
    print('Muito burro, era pra ser entre 1 e 100, mas...')
    
dica = compara(teste, num_aleatorio)

while dica != 'Acertou!':
    teste = int(input(f'Errou! O número é {dica}! Mas tente novamente: '))
    if teste>100 or teste<1:
        print('Muito burro, era pra ser entre 1 e 100, mas...')
    dica = compara(teste, num_aleatorio)

input('Acertou!\nParabéns!\nAgora aperte ENTER para fechar a janela.')

