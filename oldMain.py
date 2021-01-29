# Importas bibliotecas necessarias

import streamlit as st
import pandas as pd
import numpy as np
import quandl as q
import base64
import plotly.express as px
from graf import plot, plotC
from datetime import date, datetime

# Listas para as tabelas e os dataframes

API = ['CEPEA/CALF','CEPEA/CALF_C','CEPEA/CATTLE','CEPEA/COTTON', 'CEPEA/EOR_DP','CEPEA/MILK',
       'CEPEA/POR_DP','CEPEA/POR_NM','CEPEA/PORK','CEPEA/POULTRY_C', 'CEPEA/POULTRY_F','CEPEA/RICE',
       'CEPEA/SOYBEAN','CEPEA/SOYBEAN_C','CEPEA/SUGAR','CEPEA/SUGAR_C',
       'CEPEA/WHEAT_P','CEPEA/WHEAT_R']

Commoditys = ['CEPEA/CORN_C', 'CEPEA/COTTON_D', 'CEPEA/COFFEE_R', 'CEPEA/COFFEE_A', 'CEPEA/CORN']

Nome1 = ['Milho_C', 'Algodão_D', 'Café_R', 'Café_A', 'Milho']

Nome = ['Bezerro','Bezerro_C','Gado', 'Algodão', 'Laranja_Industrial','Leite',
        'Laranaja_Industria_Precoce','Laranja_in_Natura','Porco','Frango_Congelado'
       ,'Frango_Frio','Arroz','Soja','Soja_C','Açucar','Açucar_C', 'Trigo_P', 'Trigo_R']


# Dados

@st.cache
def get_dados():
    for (data_in_API, nome) in zip(API, Nome):
        df = pd.DataFrame(q.get(data_in_API, authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
        df.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)
        df_name = nome
        globals()[df_name] = pd.DataFrame(df)
        
    for (data_in_API, nome) in zip(Commoditys, Nome1):
        df = pd.DataFrame(q.get(data_in_API, authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Cash Price US$'])
        df.rename(columns={'Date':'Data', 'Cash Price US$':'Valor da ação US$'}, inplace=True)
        df_name = nome
        globals()[df_name] = pd.DataFrame(df)

get_dados()


# Sobre
st.title('CEPEA')
with st.beta_expander("Sobre"):
            st.write(
                """
Indicadores agropecuários.
* **Bibliotecas python:** streamlit, pandas, plotly, numpy, quandl e base64.
* **Fonte:** [**CEPEA**](https://www.cepea.esalq.usp.br/br)

Um simples demostrativo da capacidade de uso do streamlit, escrito em linguagem Python,
 e com foco de visualizar alguns indicadores da CEPEA.
""")

# Caixas de interação 
tipo = st.radio('Filtro',['Safras', 'Commoditys'], index = 1)

def dados():
    if tipo == 'Safras':
        s = st.selectbox("Indicador", globals()['Nome'], index = 0)
        return s
    else:
        x = st.selectbox("Indicador", globals()['Nome1'], index = 0)
        return x

dados()

    
if 'Safras' == True:
    fig = plot(s, s)
else:
    fig = plotC(x, x)


st.plotly_chart(fig)


st.markdown('____')
st.markdown('Por [Igor Esposito](https://github.com/Sposigor)')
