import streamlit as st

PRIMEIRO_NUMERO = 8
SEGUNDO_NUMERO = 9
TERCEIRO_NUMERO = 7

"""
 + - adicao
 * - multiplicacao
 / - divisao
 -  subtracao
"""

media_aritmetica = ( PRIMEIRO_NUMERO + SEGUNDO_NUMERO + TERCEIRO_NUMERO ) / 3

st.write(media_aritmetica)
