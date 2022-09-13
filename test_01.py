"""Game using pure Python to Learn the base of the language"""
print('*******************************')
print('Bem-vindo ao Jogo da Adivinhacao')
print('*******************************')

NUMERO_CORRETO = int(21)
NUMERO_DIGITADO = (input('Insira o numero : '))


if NUMERO_DIGITADO == NUMERO_CORRETO:
    print('Parabéns vc acertou o número', NUMERO_CORRETO)
    if (NUMERO_DIGITADO != int):
        print('Precisa digitar Um número inteiro')
else:
    print(NUMERO_DIGITADO, ' Número incorreto, Tente outra vez!')
