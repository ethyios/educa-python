import random

contador = 1
nivel = 0
limite: int

def compara(teste, numero):
    if teste != numero:
        if teste > numero:
            dica = 'menor'
        else:
            dica = 'maior'
    else:
        dica = 'Acertou!'

    return dica

nivel = int(input('Oi! Digite o numero do nível que quer jogar: '))

if nivel not in range(1,3+1):
    print('Esse nível não está disponível, digite um número entre 1 e 3\n')
    nivel = int(input('Digite o numero do nível que quer jogar: '))

elif nivel == 1:
    limite = 10

elif nivel == 2:
    limite = 100

elif nivel == 3:
    limite = 1000

num_aleatorio = random.randint(1, limite+1)
print(f'\nCerto, pensei em um número de 1 a {limite}.')

teste = int(input('Você consegue adivinhar?: '))
if teste not in range(1, limite+1):
    print(f'Número fora do escopo, deve ser entre 1 e {limite}, mas...')
    
dica = compara(teste, num_aleatorio)

while dica != 'Acertou!':
    teste = int(input(f'Errou! O número é {dica}! Tente novamente: '))
    if teste not in range(1, limite+1):
        print(f'Número fora do escopo, deve ser entre 1 e {limite}, mas...')
    dica = compara(teste, num_aleatorio)
    contador += 1

print(f'Acertou! Parabéns!\nVocê tentou {contador}x!')
input('\nAgora aperte ENTER para fechar a janela.')
