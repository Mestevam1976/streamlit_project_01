import streamlit as st 
import pandas as pd 
import numpy as np 

if st.sidebar.button('Exibir Mensagem'):
    df= pd.DataFrame(
        np.random.rand(10,3),
        columns=['Preço', 'Taxa de ocupação', 'Taxa predial']
    )
    st.bar_chart(df)

opcao = st.radio(
    'Selecionar uma opcao: ',
    ('Opção 1', 'Opção 2')
)

if opcao == 'Opção 1':
    st.write('Selecionado a opção 1')
elif opcao == 'Opção 2':
    st.write('Selecionado a opção 2')