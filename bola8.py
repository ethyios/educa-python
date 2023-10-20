# Bola8Mágica
import random as r

# respostas
ans= [
    'Vai com tudo!',
    'Nem a pau, Juvenal.',
    'Sei não, chapa. Tenta perguntar de novo.',
    'O medo do desconhecido nos aprisiona.',
    'Só você pode salvar o mundo, soldado!',
    'Diz \'alô\' para a Democracia!',
    'Pra mim tanto faz como tanto fez.',
    'Já olhou para uma pessoa e pensou: O que passa na cabeça dela?\nNem eu, quem pensa assim?',
]

nome = input('Olá! Qual o seu nome? Digite e pressione ENTER\n')

print(f'\n\n\nBem vindo, {nome}! Eu sou a Bola Mágica de 8 respostas.')

pergunta = input('Me faça uma pergunta e pressione ENTER para chacoalhar.\n')

print('Hmm, deixe-me pensar...\n')

cont = int(input('Quantas respostas quer?\n'))

for i in range(cont):
    resposta = ans[r.randint(0,7)]
    print(resposta)

input(f'\nObrigado por brincar comigo, {nome}! Para terminar, pressione ENTER...')
