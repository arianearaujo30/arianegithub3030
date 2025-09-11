# Escrever um algoritimo que mostra os
# numeros pares entre 100 120

import streamlit as st 
import time

st.title("Atividade: 1")

st.hearder("Laço de repetição: For")
st.button("Iniciar")
if st.button("INICIAR"):
    for i in range(100,121, 2):
        st.info(i)