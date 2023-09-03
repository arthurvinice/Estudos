#Este jogo solicita um número inteiro de 1 a 10 ao usuário e executa o laço até o usuário acertar o número.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Chute um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, este número é muito baixo. Tente novamente!')
        elif guess > random_number:
            print('Desculpe, este número é muito alto. Tente novamente!')
        
    print(f'Parabéns, você acertou o número {random_number}!!')    

guess(10)
