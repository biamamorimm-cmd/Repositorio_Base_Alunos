nota=int (input('Digite a nota:'))

while nota<0 or nota>10:
    print ('Digite um valor válido só pode ser de 0 á 10')
    nota=int (input('Valor inválido,digite novamente'))

print ('Valor válido')