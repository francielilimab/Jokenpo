from random import randint
from time import sleep
print(f'{" Jokenpô! ":=^50}')
computador = randint(1, 3)
item = ('a', 'Pedra', 'Papel', 'Tesoura')
jogador = int(input('Suas opções: \n'
                 '(1) Pedra \n'
                 '(2) Papel \n'
                 '(3) Tesoura \n'
                 'Faça sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('-='*13)
print(f'O computador jogou: {item[computador]} \n'
      f'Jogador jogou: {item[jogador]}')
print('-='*13)
if computador == 1: #computador jogou pedra
    if jogador == 1:
        print('\033[1;36mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;34mJOGADOR VENCE!\033[m')
    elif jogador == 3:
        print('\033[1;32mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif computador == 2: #computador jogou papel
    if jogador == 1:
        print('\033[1;32mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;36mEMPATE!\033[M')
    elif jogador == 3:
        print('\033[1;34mJOGADOR VENCE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif computador == 3: #computador jogou tesoura
    if jogador == 1:
        print('\033[1;34mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;32mCOMPUTADOR VENCE!\033[m')
    elif jogador == 3:
        print('\033[1;36mEMPATE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')
