

import streamlit as st

coluna = st.columns (4) 
coluna[0].write ('1')
coluna[1].write ('2')
coluna[2].write ('3')
coluna[3].write ('4')


numero1=st.text_input ('Digite o primeiro número:')
numero2=st.text_input ('Digite o segundo número:')


with coluna [0]:
    if st.button ('SOMA'):
        resultado1= int (numero1) + int (numero2)
        st.write (f'O resultado é {resultado1}:')
      

with coluna [1]:
    if st.button ('DIVISÃO'):
        resultado2= int (numero1) / int (numero2)
        st.write (f'O resultado é {resultado2}:')
    

with coluna [2]:
    if st.button ('SUBTRAÇÃO'):
        resultado3= int (numero1) - int (numero2)
        st.write (f'O resultado é {resultado3}:')
     

with coluna [3]:
    if st.button ('MULTIPLICAÇÃO'):
        resultado4= int (numero1) * int (numero2)
        st.write (f'O resultado é {resultado4}:')
       

