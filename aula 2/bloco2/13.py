letra = input('Escolha uma opção ("F" ou "M"): ')
sexo = 'Masculino' if letra == 'M' else ('Feminino' if letra == 'F' else 'Sexo inválido')
print('O sexo é: ' + sexo)