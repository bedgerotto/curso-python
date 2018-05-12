nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: '))
while (idade < 0 or idade > 150):
    idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salário: '))
while salario <= 0:
    salario = float(input('Digite seu salário: '))

sexo = input('Digite seu sexo (f ou m): ')
while not sexo in ['f', 'm']:
    sexo = input('Digite seu sexo: ')

estado_civil = input('Digite seu estado civil (s, v, c, d): ')
while not estado_civil in ['s', 'v', 'c', 'd']:
    estado_civil = input('Digite seu estado civil: ')

print('Nome: ' + nome)
print('Idade: ' + str(idade))
print('Salário: ' + str(salario))
print('Sexo: ' + sexo)
print('Estado civil: ' + estado_civil)