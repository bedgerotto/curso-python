while True:
    nota = float(input('Insira uma nota de 1 a 10: '))
    if (nota > 10 or nota < 0):
        print('Inválido, tente novamente')
    else:
        print('Válido. Nota: ' + str(nota))
        break