"""Test for type"""

print('************************************************')
print('************* Jogo da Adivinhacao **************')

NUMERO_SECRETO = 42

NUMERO_DIGITADO = int(input('Digite o número secreto :'))

# print(type(NUMERO_DIGITADO))

if (NUMERO_SECRETO == NUMERO_DIGITADO):
    print(NUMERO_DIGITADO, ' Parabéns vc acertou ')
else:
    print(NUMERO_DIGITADO, ' Nao foi hoje,  vc Errou ')
