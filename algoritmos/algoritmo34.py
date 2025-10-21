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
    antecessor = numero - 1
    sucessor = numero + 1
    st.write(f"O antecessor do número digitado é {antecessor}")
    st.write(f"O sucessor do número digitado é {sucessor}")
else:
    st.write("Digite um número para continuar.")