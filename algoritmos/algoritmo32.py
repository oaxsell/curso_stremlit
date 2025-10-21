import streamlit as st

"""
    Ler um numero inteiro e imprimi-lo.
"""
# Entrada
entrada = st.text_input("Digite um número inteiro:")

# Processamento
# (evitar erro do streamlit quando a entrada estiver vazia)
if entrada:
    numero = int(entrada)
    st.write(f"O número digitado é {numero}")
else:
    st.write("Digite um número para continuar.")
