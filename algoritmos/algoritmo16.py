import streamlit as st

mercado = ['Acoes', 'Opcoes', 'Futuro', 'Dolar', 'Ouro', 'Criptomoedas']

mercado[0:2] = ['tesouro', 'titulos']

st.write(mercado)