try:
  file = open('nomes.txt', 'r')
  newFile = open('nomeSeparados.txt', 'w')

  for line in file:
    newFile.write('|'+'|'.join(list(line.upper())))
    
except FileNotFoundError:
  print('Deu ruim.')
  
finally:
    file.close()
    newFile.close()
    print('Sucesso.')