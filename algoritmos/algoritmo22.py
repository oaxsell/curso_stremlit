# remove()

import streamlit as st

mercado = ['Acoes', 'Opcoes', 'Futuro', 'Dolar', 'Ouro', 'Criptomoedas']

mercado.remove('Ouro')

st.write(mercado)