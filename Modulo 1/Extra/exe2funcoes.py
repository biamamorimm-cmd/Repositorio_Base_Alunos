nome= (input('Qual o seu nome?:'))
hora= (input('Período do dia:'))

def saudação(nome,hora):
    if hora=='Manhã':
        print (f'Bom dia,{nome}')
    elif hora== 'Tarde':
        print (f'Boa tarde,{nome}')    
    else:
        print (f'Boa noite,{nome}')    

saudação(nome,hora)