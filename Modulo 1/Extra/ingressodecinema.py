idade= int (input('Digite a sua idade?:'))
estudante=  (input('Você é estudante?:')) 

if idade<=12:
    print ('Criança,o valor do ingresso é de R$ 8,00')
elif idade >13 and idade <64:
    print ('Adulto,o valor do ingresso é de R$ 20,00')
else:
    print('Idoso,o valor do ingresso é de R$ 10,00')
if estudante=='sim':
    print ('Estudante,o valor do ingresso é de R$ 12,00')    

