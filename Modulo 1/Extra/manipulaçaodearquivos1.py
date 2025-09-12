
nome= input ('Qual o seu nome?')
idade= int (input ('Qual a sua idade?'))

try:
    with open('contatos.txt', 'a') as arquivo:
        arquivo.write(f'{nome}|{idade}\n')

except:
        with open('contatos.txt', 'x') as arquivo:
            criar = arquivo.x(f'{nome}|{idade}\n')




