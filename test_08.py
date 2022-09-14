"""Test Python using IF AND ELSE"""

print('**********************************')
print('********Jogo da Adivinhacao*******')
print('**********************************')

NUMERO_SECRETO = 42
CONTADOR = 1


while (CONTADOR <= 3):
    PALPITE_STR = input('Digite seu palpite: ')
    print('Seu palpite foi o ', PALPITE_STR)
    PALPITE_CONV = int(PALPITE_STR)

    NUMERO_IGUAL = PALPITE_CONV == NUMERO_SECRETO
    NUMERO_MAIOR = PALPITE_CONV > NUMERO_SECRETO
    NUMERO_MENOR = PALPITE_CONV < NUMERO_SECRETO

    if (NUMERO_IGUAL):
        print('Parabéns vc acertou em cheio! ')
        CONTADOR = 4
    else:
        if (NUMERO_MAIOR):
            print('O Numero que vc digitou é maior que o secreto! ')
        elif (NUMERO_MENOR):
            print('O Numeto que vc digitou é menor que o secreto! ')
        CONTADOR += 1
