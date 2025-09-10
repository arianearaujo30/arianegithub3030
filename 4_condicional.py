# Verifique a idade de uma pessoa
# Se menor que 18, mostre: Menor de idade
# Caso contrário, mostre: Maior de idade
# Usando streamlit 

import streamlit as st

st.title("Verificando a idade")

idade = st.number_input("Digite sua idade: ")

if st.button("Verificar"): 
    if idade < 18: 
        st.write ("Menor de idade")
    else: 
        st.write("Maior de idade")


else: 
    st.warning("Por favor, digite sua idade: ")