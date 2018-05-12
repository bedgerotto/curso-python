numeros = []
for x in range(0,5):
    numeros.append(float(input('Digite o '+ str(x) +'° número: ')))

media = sum(numeros)  / 5
print('A soma dos números é: ' + str(sum(numeros)) + ' e a média é: ' + str(media) )