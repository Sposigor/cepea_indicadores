# Bibliotecas necessarias para execução da função

import streamlit as st
import pandas as pd


# streamlit cache basicamente é para manter a infomação no cache do navegador para quando houve a seleção dos indicadores não tenha que recarregar.

@st.cache()
def get_dados(): # Função para usar a API e extrair os dados e uma pequena transformação nas colunas.

    # Safras
    # Usei a função het do quandl para puxar a infomação da base de dados deles e com isso ter acesso as atualizações diarias pela API.
    Gado = pd.DataFrame(q.get('CEPEA/CATTLE', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Gado.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Bezerro = pd.DataFrame(q.get('CEPEA/CALF', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Bezerro.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Algodão = pd.DataFrame(q.get('CEPEA/COTTON', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Algodão.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Laranja_Industrial = pd.DataFrame(q.get('CEPEA/EOR_DP', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Laranja_Industrial.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Laranja_in_Natura = pd.DataFrame(q.get('CEPEA/POR_NM', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Laranja_in_Natura.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Porco = pd.DataFrame(q.get('CEPEA/PORK', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Porco.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Frango_Congelado = pd.DataFrame(q.get('CEPEA/POULTRY_C', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Frango_Congelado.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Frango_Frio = pd.DataFrame(q.get('CEPEA/POULTRY_F', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Frango_Frio.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Arroz = pd.DataFrame(q.get('CEPEA/RICE', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Arroz.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Soja = pd.DataFrame(q.get('CEPEA/SOYBEAN', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Soja.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Soja_C = pd.DataFrame(q.get('CEPEA/SOYBEAN_C', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Soja_C.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Açucar = pd.DataFrame(q.get('CEPEA/SUGAR', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Açucar.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True) 

    Trigo_P = pd.DataFrame(q.get('CEPEA/WHEAT_P', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Trigo_P.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    Trigo_R = pd.DataFrame(q.get('CEPEA/WHEAT_R', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Price US$'])
    Trigo_R.rename(columns={'Date':'Data', 'Price US$':'Preço US$'}, inplace=True)

    # Commoditys

    Café_R = pd.DataFrame(q.get('CEPEA/COFFEE_R', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Cash Price US$'])
    Café_R.rename(columns={'Date':'Data', 'Cash Price US$':'Preço US$'}, inplace=True)

    Café_A = pd.DataFrame(q.get('CEPEA/COFFEE_A', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Cash Price US$'])
    Café_A.rename(columns={'Date':'Data', 'Cash Price US$':'Preço US$'}, inplace=True)
    
    Milho = pd.DataFrame(q.get('CEPEA/CORN', authtoken="-zKjekRSoo3qjzzCVyUS", returns='numpy'), columns=['Date', 'Cash Price US$'])
    Milho.rename(columns={'Date':'Data', 'Cash Price US$':'Preço US$'}, inplace=True) 

    return Gado, Bezerro, Algodão, Laranja_Industrial, Laranja_in_Natura, Porco, Frango_Congelado, Frango_Frio, Arroz, Soja, Soja_C, Açucar, Trigo_P, Trigo_R, Café_A, Café_R, Milho
