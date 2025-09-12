
nome = input('Digite o seu nome: ')
telefone = input('Digite o seu número de telefone: ')
email = input('Digite o e-mail: ')

with open('contatos.txt', 'a') as arquivo:
    arquivo.write(f'{nome}|{telefone}|{email}\n')

with open('contatos.txt', 'r') as arquivo:
    content = arquivo.read()
    print(content) 
    