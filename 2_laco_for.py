# Escrever um algaritimo que mostre os 
# numeros impares entre 1 e 20

import streamlit as st 
import time 

st.title("Atividade: 2")

st.header("Repetição: For")
if st.button("Iniciar"):
    for i in range(1,21, 2):
         st.info(i)
         