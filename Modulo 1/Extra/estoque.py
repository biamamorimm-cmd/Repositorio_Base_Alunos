estoque = 500
mostre= 0

while True:

  menu= print ('(1) Adicionar unidades ao estoque,(2) Remover unidades do estoque,(3) Verificar estoque atual,(4) Sair')
  mostre=int(input('Escolha uma opção:'))
  if mostre==1:
    adicionar=int (input('Quantas unidades você gostaria de adicionar ao estoque?'))
    estoque -= adicionar
    print (estoque)
  elif mostre ==2:
    remover=int (input('Quantas unidades serão removidas do estoque?'))
    estoque+= remover
    print (estoque) 
  elif mostre ==4:
    break
  else:
    print (estoque)   