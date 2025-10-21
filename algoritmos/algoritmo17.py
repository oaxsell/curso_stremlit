# Use a funcao count() para contar quantas vezes apareceu a palavra dolar

import streamlit as st

mercado = ['Acoes', 'Opcoes', 'Futuro', 'Dolar', 'Ouro', 'Criptomoedas']
mercado.append('Dolar')
st.write(mercado)
st.write(f"Quantidade de ocorrencias do 'Dolar' na lista e: {mercado.count('Dolar')}")