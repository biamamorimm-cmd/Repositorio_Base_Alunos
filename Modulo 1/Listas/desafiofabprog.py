agenda = ['Alex','Nathálya','Bruno','Bianca','Luca','Josué']

while True:
    menu=print ("[1] Cadastrar pessoas\n[2] Listar pessoas \n[3] Excluir pessoas\n[4] Sair ")
    opc= int (input('Escolha uma opção:'))

    if opc ==1:
     adc=input ('Digite o nome que você deseja adicionar:')
     agenda .append (adc)
    elif opc==2:
       print (agenda)
    elif opc ==3:
     rmv= input ('Digite o nome da pessoa que você deseja remover:')      
     agenda.remove(rmv)
    else:
      print("="*50)
      break