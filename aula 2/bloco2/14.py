letra = input('Digite uma letra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
tipo = 'Vogal' if letra in vogais else 'Consoante'
print('A letra é: ' + tipo)