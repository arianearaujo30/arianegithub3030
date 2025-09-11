import streamlit as st
import time 

st.title("Atividade")
st.hearder("Laço de repetição - For")
st.write("Escrever um programa de computador que solicite do usuário 5"\
    "números interos e, ao final, apresente a soma de todos os números lidos.")
soma = 0 

for i in range(1, 6): 
    numero = st.number_input(f"Digite o {i} numero", step=1, min_value=0)
    soma = soma + numero 
    time.sleep(1)

if st.button("Iniciar"):
    st.sucess(f"A soma do números é: {soma}")

else: 
    st.info("Informe um número")
