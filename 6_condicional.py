import streamlit as st

st.title("Atividade")

primeiro_numero = st.number_input("Digite o primeiro número")
segundo_numero = st.number_input("Digite o segundo número")

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

if st.button("Verificar"): 
    if primeiro_numero and segundo_numero:
      st.write(f"Soma: {soma}")
      st.write(f"Produto: {produto}")
      st.write(f"Média: {media}")
      st.write(f"Maior: {maior}")
      st.write(f"Menor: {menor}")

else: 
    st.info("Informe os números.")

  
