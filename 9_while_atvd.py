import streamlit as st 

st.title("Laço de Repetição - while" )

QUANTIDADES_NOTAS = 2
soma = 0

for i in range(QUANTIDADES_NOTAS):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    soma = soma + nota
    media = soma / QUANTIDADES_NOTAS

    if st.button("Mostrar resultados"):
        if nota <= 0 or nota >= 10:
            st.warning("A nota deve estar entre 0 e 10.")
        st.info(f"Média: {media}")
    
    
