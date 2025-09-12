import streamlit as st 

st.title("Lógica de programação")

st.header("Laço de repetição - For")

soma = 0 

for i in range(4):
    nota = st.number_input(f"Digite a {i+1}ª nota:")
    soma = soma + nota
   
    media = soma / 4
    
    if st.button("Mostrar resultado"):
        st.info(f"Média: {media}")