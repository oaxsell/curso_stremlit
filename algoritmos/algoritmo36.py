import streamlit as st

"""
    Ler dois numeros inteiros
    Soma
    Mostrar a soma (personalizada) - f-strings
"""
# Entrada
entrada_primeiro_numero = st.text_input("Digite um número inteiro:")
entrada_segundo_numero = st.text_input("Digite outro número inteiro:")

# Processamento
# (evitar erro do streamlit quando a entrada estiver vazia)
if entrada_primeiro_numero and entrada_segundo_numero:
    primeiro_numero = int(entrada_primeiro_numero)
    segundo_numero = int(entrada_segundo_numero)
    soma = primeiro_numero + segundo_numero
    st.write(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
else:
    st.write("Digite um número para continuar.")