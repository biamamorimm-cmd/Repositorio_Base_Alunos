classificar_numeros= int (input('Digite um numero:'))

if classificar_numeros <0:
    print ('Número negativo')
elif classificar_numeros >=0 and classificar_numeros <=10:
    print ('Entre 0 e 10')
elif classificar_numeros >10 and classificar_numeros <=100:
    print ('Entre 10 e 100')    
else:
    print ('Maior que 100')

  
    