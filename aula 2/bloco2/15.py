n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
mensagem = 'Aprovado com distinção' if media == 10 else ( 'Aprovado' if media >= 7 else 'Reprovado' )
print(mensagem + ' - Média: ' + str(media))