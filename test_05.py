"""Testing conditions"""

numero_secreto = int(42)

numero_digitado = int(input('Digite um número: '))

numero_correto = numero_secreto == numero_digitado
numero_maior = numero_digitado > numero_secreto
numero_menor = numero_digitado < numero_digitado

if (numero_correto):
    print('Parabéns vc acertou o número')
else:
    if (numero_maior):
        print('O número digitado foi maior', numero_digitado)
    else:
        print('o numero foi menor')
