import streamlit as st 
import pandas as pd 
import numpy as np 

st.header('Dashboard Streamlit Testes Genéricos', divider='rainbow')

if st.sidebar.button('Exemplo Gráfico de Barras'):
    st.header('Preço Médio do Litro da Gasolina por Estado (UF) em :blue[2021]')
    df= pd.read_csv('Csv_files/gasolina_etanol_2021.csv', sep=';')
    df['Valor de Venda'] = df['Valor de Venda'].replace(',','.',regex=True)
    df['Valor de Venda'] = pd.to_numeric(df['Valor de Venda'])
    df1 = df.groupby(by=['Estado - Sigla']).mean(numeric_only=True).reset_index()
    df1['Valor de Venda'] = df1['Valor de Venda'].round(3)
    df1.rename(columns={'Estado - Sigla':'UF', 'Valor de Venda':'Valor Médio de Venda'},inplace=True)
    st.bar_chart(df1[['UF', 'Valor Médio de Venda']], x='UF', y='Valor Médio de Venda', color='#008000', use_container_width=True)

opcao = st.radio(
    'Selecionar uma opcao: ',
    ('Opção 1', 'Opção 2')
)

if opcao == 'Opção 1':
    st.write('Selecionado a opção 1')
elif opcao == 'Opção 2':
    st.write('Selecionado a opção 2')