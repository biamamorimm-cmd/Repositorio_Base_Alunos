import requests


prato = input ('Selecione o prato escolhido pelo cliente: Acarajé (R$ 15,00), Cuzcuz Baiano (R$ 25,00), Caldo de Mocotó (R$ 30,00), Virada à Paulista (R$ 40,00);')
bebida= input ('Selecione a bebida escolhida pelo cliente: Àgua (R$ 2,50), Água com gás (R$ 3,00), Suco de polpa (R$7,00), Soda Italiana (R$ 12,00), Refrigerante (R$ 6,00);')
sobremesa= input ('Selecione a sobremesa escolhida pelo cliente: Pudim de Leite (R$ 20,00), Petit Gateau (R$10,00), Torta Holandesa (R$ 8,00), Gelato (R$ 10,00);')

requests.post ('https://68e932b0f2707e6128cdfb28.mockapi.io/Restaurante').json()