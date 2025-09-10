lista=[1,-15,50,0,25,-45,-19,]

contador_positivo=0
contador_negativo=0
contador_zero=0

for num in lista:
    if num >=1:
      print (f'{num} É positivo')
      contador_positivo+=1
    elif num ==0:
      print (f'{num} É zero')
      contador_zero+=1 
    else:  
     print (f'{num} É negativo')  
     contador_negativo+=1

print ('Relatório:')
print (f'{contador_positivo} Positivos')
print (f'{contador_negativo} Negativos')
print (f'{contador_zero} Zero')
