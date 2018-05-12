n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

ordenado = sorted([n1, n2, n3])
ordenado.reverse()
print('O maior número é: ' + str(ordenado[0]) + ' e o menor número é: ' + str(ordenado[2]))