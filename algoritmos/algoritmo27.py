import streamlit as st

ibov = ['PETR4', 'BBAS3', 'USIMS', 'GGBR4', 'VALE3']

# o elemento de indices 2 ao indice 3
st.write(ibov[2:4])
# o elemento do indice 1 ate o ultimo
st.write(ibov[1:])
# Do elemento inicial (zero) ao elemento 2
st.write(ibov[:3])
# Do elemento inicial ao ultimo saltando de 2 em 2
st.write(ibov[0:5:2])
# Selecionar os tresm ultimos elementos da lista
st.write(ibov[-3:])
# Selecionar os 2 primeiros elementos da lista
st.write(ibov[:-3])