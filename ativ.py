# Escrever um algoritimo que mostra os
# numeros pares entre 100 121

import streamlit as st
import time

st.title("Atividade: 01")

st.header("Repetição: for")

if st.button("INICIAR"):
    for i in range(100,121, 2):
        st.info(i)
        time.sleep(1)
    st.success("FIM")