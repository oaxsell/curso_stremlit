# reverse()
import streamlit as st

mercado = ['Acoes', 'Opcoes', 'Futuro', 'Dolar', 'Ouro', 'Criptomoedas']

mercado.reverse()

lista_reversa_case_insensitive = sorted(mercado, key=str.lower, reverse=True)

st.write(f"Minha descrente", mercado)