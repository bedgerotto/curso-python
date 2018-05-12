numeros = []
for x in range(0,5):
    numeros.append(float(input('Digite o '+ str(x) +'° número: ')))

numeros.sort()
numeros.reverse()
print('O maior número é: ' + str(numeros[0]))