import streamlit as st

mercado = ['Acoes', 'Opcoes', 'Futuro', 'Dolar', 'Ouro', 'Criptomoedas']

mercado.insert(2, 'Fundo de Investimento')

st.write(mercado)