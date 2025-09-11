# Escreva um algoritmo

import streamilt as st
import time 

st.title("Atividade")

st.("Laçp de repetição - For"):

st.write("EScrever um algoritmo que solicita ao usuário e"\ 
"faça a contagem regressiva a partir do número informado até o número 1,"\
    "aguardando um segundo para exibir cada número.")

numero = st.number_input("Digite um número: ", step=1, min_value=0)
if st.button("Iniciar"):
    for i in range(numero, 0, -1):
         st.warning(i)
         time.sleep(1)
        st.hearder("FIM")
else: 
    st.info("Informe um número")