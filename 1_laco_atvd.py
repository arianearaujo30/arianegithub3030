import streamlit as st
import time

st.title("Verificando números pares e impares")

for i in range(1,5):
    numero = st.number_input("Digite o {i}:", step=1)
    if numero % 2 == 0: 
        pares = pares + 1
    else:
        impares = impares + 1
        
        if st.button("Verificar"): 
            st.info(f"Quantidade de pares: {pares}")
            st.info(f"Quantidade de impares: {impares}")
            