# verificando a média 
# Solicite ao usuário a média do aluno
# Se maior ou igual a 7, mostre como aprovado
# Caso contrário, mostre como reprovado.

import streamlit as st

st.write("Verificando a média")

media = st.number_input("Digite a média do aluno: ")
if st.button("Verificar"): 
   if media  >= 7:
        st.write("Aprovado")
   else: 
        st.write("Reprovado")
else: 
 st.warning("Informe a média")