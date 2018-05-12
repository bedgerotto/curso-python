n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = sorted([n1, n2, n3])
maior.reverse()
print('O maior número é: ' + str(maior[0]))