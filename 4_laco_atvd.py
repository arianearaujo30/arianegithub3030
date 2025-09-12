import streamlit as st 
import time

st.title("Laço de Repetição - For")

QUANTIDADES_NOTAS = 3
soma = 0 

for i in range(4):
    nota = st.number_input(f"Digite a {i+1}ª nota:")
    soma = soma + nota 

    media = soma / QUANTIDADES_NOTAS  
    
    if st.button("Mostrar resultado"):
        st.info(f"Média: {media}")
        if media >= 7:
            st.success("Aprovado")
        elif media >= 4:
            st.warning("Recuperação")
        else: 
            st.error("Reprovado")