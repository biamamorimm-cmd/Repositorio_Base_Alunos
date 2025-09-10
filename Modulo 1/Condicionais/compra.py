valor=float (input('Digite o valor da compra:'))
desconto= valor*0.10

if valor >=100:
    print(f'Valor final { valor - desconto}') 
else:    
    print(f'Valor final {valor}')
    
