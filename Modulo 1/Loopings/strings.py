palavra= (input('Digite uma palavra:'))
soma=0

for item in palavra:
    if item in 'aeiou':
        soma+=1
print (soma)        