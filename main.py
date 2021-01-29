# Importas bibliotecas necessarias

import streamlit as st
import pandas as pd
import numpy as np
import quandl as q
import base64
import plotly.express as px
from graf import plot
from datetime import date, datetime
from dados import get_dados

# Listas para as tabelas as tabelas

Tabela = ['Açucar Cristal', 'Algodão em Pluma', 'Arroz em Casca', 'Bezerro', 'Café Arábica', 'Café Robusta', 'Frango Congelado', 'Frango Frio', 'Laranja Indústria', 'Laranja Pera in Natura', 'Milho', 'Porco', 'Soja - Paraná', 'Soja - Paranaguá', 'Trigo Paraná', 'Trigo RS']

Gado, Bezerro, Algodão, Laranja_Industrial, Laranja_in_Natura, Porco, Frango_Congelado, Frango_Frio, Arroz, Soja, Soja_C, Açucar, Trigo_P, Trigo_R, Café_A, Café_R, Milho = get_dados()

# Sobre

st.title('CEPEA')
with st.beta_expander("Sobre"):
            st.write(
                """
Indicadores agropecuários.
* **Bibliotecas python:** streamlit, pandas, plotly, numpy, quandl e base64.
* **Fonte:** [**CEPEA**](https://www.cepea.esalq.usp.br/br)

Um simples demostrativo da capacidade de uso do streamlit, escrito em linguagem Python
 e com foco na visualização de alguns indicadores da CEPEA.
""")

# Caixas de interação 

s = st.selectbox("Indicador", Tabela, index = 0)

def filtro(): 
    if s == 'Boi Gordo':
        fig = plot('Boi Gordo', Gado)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Boi Gordo](https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx) é vendindo em arroba de 15kg.
2. Boi Gordo considerado para o indicador: bovinos machos,  com  16 (dezesseis) arrobas líquidas ou mais de carcaça e idade máxima de 42 (quarenta  e  dois)  meses,  de  acordo  com  as  especificações  do  contrato futuro de boi gordo da B3.
3. Região de origem: região onde está localizado o animal transacionado. Para o indicador, são cinco: Araçatuba, Presidente Prudente, Bauru, São José do Rio Preto e Vale do Paraíba.""")
    elif s == 'Algodão em Pluma':
        fig = plot('Algodão em Pluma', Algodão)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Algodão em Pluma](https://www.cepea.esalq.usp.br/br/indicador/algodao-a-vista.aspx) é vendindo centavos de dolar á vista.
2. Algodão em Pluma considerado para o indicador: Algodão tipo 41, folha 4 - cor estritamente abaixo da média (strict low middling) – (antigo tipo 6, fibra 30/32 mm, sem característica).
3. Negócios feitos nas principais regiões produtoras e consumidoras de algodão do Brasil, entre elas: Santa Catarina, Rio de Janeiro, São Paulo, Rio Grande do Norte, Pernambuco, Alagoas, Paraíba, Ceará, Goiás, Bahia, Minas Gerais, Paraná, Tocantins, Mato Grosso e Mato Grosso do Sul.""")
    elif s == 'Açucar Cristal':
        fig = plot('Açucar Cristal', Açucar)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Açucar Cristal](https://www.cepea.esalq.usp.br/br/indicador/acucar.aspx) é vendindo pelo saco de 50kg.
2. Açúcar Cristal considerado par  o indicador: com mínimo de polarização de 99,7 graus, máximo de 0,10% de umidade, cor ICUMSA mais freqüente 130 - 180, máximo de 0,07% de cinzas, ensacado em sacas novas de polipropileno, destinado ao mercado interno.
3. Negócios feitos no Estado de SP, dividido em seis regiões: Piracicaba, Ribeirão Preto, Jaú, Assis, São José do Rio Preto e Araçatuba.""")
    elif s == 'Bezerro':
        fig = plot('Bezerro', Bezerro)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Bezerro](https://www.cepea.esalq.usp.br/br/indicador/bezerro.aspx) é vendindo pelo animal vivo (cabeça).
2. Bezerro considerado para o indicador: bezerro desmamado, macho, nelore, com idade entre 8 e 12 meses; valores coletados se referem a negócios realizados no mercado físico – preços ao produtor.
3. Negócios feitos no Estado de MS, dividido em cinco regiões: Três Lagoas, Campo Grande, Dourados, Pantanal e Cassilândia.""")
    elif s == 'Arroz em Casca':
        fig = plot('Arroz em Casca', Arroz)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Arroz](https://www.cepea.esalq.usp.br/br/indicador/arroz.aspx) é vendindo pelo saco de 50kg.
2. Arroz considerado para o indicador: Arroz em casca, posto indústria, com rendimento do grão de 57% maior e 58% (menor, igual e maior) de grãos inteiros, com cerca de 10% de grãos quebrados por 100 gramas. 
3. Produção em cada uma das regiões (conjuntos de municípios) de destino do arroz em casca para beneficiamento no estado do Rio Grande do Sul, quais sejam: Campanha, Depressão Central, Fronteira Oeste, Zona Sul, Planície Costeira Interna e Planície Costeira Externa. As regiões são definidas de acordo com a divisão administrativa do Instituto Rio-Grandense do Arroz – IRGA""")
    elif s == 'Café Arábica':
        fig = plot('Café Arábica', Café_A)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Café Arábica](https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx) é vendindo pelo saco de 60kg.
2. Café Arábica considerado para o indicador: Café arábica tipo 6, bebida dura para melhor, bem preparado, com até 86 defeitos por amostra de 300 gramas; Indicador refere-se a negócios no mercado de lotes. 
3. Produção no Cerrado e Sul de Minas Gerais, Mogiana (SP), Garça (SP) e noroeste do Paraná posto na cidade de SP""")
    elif s == 'Café Robusta':
        fig = plot('Café Robusta', Café_R)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Café Robusta](https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx) é vendindo pelo saco de 60kg.
2. Café Robusta considerado para o indicador: Café robusta tipo 6, peneira 13 cima, com 86 defeitos; Indicador refere-se a negócios no mercado de lotes. 
3. Produção no Colatina/ES e São Gabriel da Palha/ES""")
    elif s == 'Laranja Indústria':
        fig = plot('Laranja Indústria', Laranja_Industrial)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Laranja Indústria](https://www.cepea.esalq.usp.br/br/indicador/citros.aspx) é vendindo pela caixa de 40,8kg; exceções: poncã e tahiti: caixa de 27kg.
2. Laranja considerada para o indicador: há dois grupos: um que abrange pera e tardias e outro de precoces (hamlin, westin, valência americana, etc); ambos negociados nas modalidades spot e em contratos para uma safra; até 24 de julho de 2012, os valores “indústria” consideravam apenas negócios spot. 
3. Produção no estado de São Paulo""")
    elif s == 'Laranja Pera in Natura':
        fig = plot('Laranja Pera in Natura', Laranja_in_Natura)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Laranja Pera in Natura](https://www.cepea.esalq.usp.br/br/indicador/citros.aspx) é vendindo pela caixa de 40,8kg; exceções: poncã e tahiti: caixa de 27kg.
2. Laranja considerada para o indicador: há dois grupos: um que abrange pera e tardias e outro de precoces (hamlin, westin, valência americana, etc); ambos negociados nas modalidades spot e em contratos para uma safra; até 24 de julho de 2012, os valores “indústria” consideravam apenas negócios spot. 
3. Produção no estado de São Paulo""")
    elif s == 'Frango Congelado':
        fig = plot('Frango Congelado', Frango_Congelado)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Frango Congelado](https://www.cepea.esalq.usp.br/br/indicador/frango.aspx) é vendindo pelo frango inteiro abatido.
2. Produção no estados do Rio Grande do Sul, Santa Catarina, Paraná, São Paulo e Minas Gerais. No total, são nove praças: Porto Alegre (RS), Erechim (RS), Chapecó (SC), Francisco Beltrão (PR), Toledo (PR), Pará de Minas (MG), Descalvado (SP), São José do Rio Preto (SP) e Grande São Paulo.""")
    elif s == 'Frango Frio':
        fig = plot('Frango Frio', Frango_Frio)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Frango Frio](https://www.cepea.esalq.usp.br/br/indicador/frango.aspx) é vendindo pelo frango inteiro abatido.
2. Produção no estados do Rio Grande do Sul, Santa Catarina, Paraná, São Paulo e Minas Gerais. No total, são nove praças: Porto Alegre (RS), Erechim (RS), Chapecó (SC), Francisco Beltrão (PR), Toledo (PR), Pará de Minas (MG), Descalvado (SP), São José do Rio Preto (SP) e Grande São Paulo.""")
    elif s == 'Milho':
        fig = plot('Milho', Milho)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Milho](https://www.cepea.esalq.usp.br/br/indicador/milho.aspx) é vendindo pelo saco de 60kg.
2. Milho amarelo semi-duro, tipo 2, de odor e aspectos normais, em bom estado de conservação, livre de bagas de mamona e outras sementes prejudiciais e insetos vivos, duro ou semiduro, com umidade de até 14%, teor de impurezas máximo de 1% na peneira 3mm, máximo de 6% de grãos ardidos ou brotados e livre de grãos mofados e até 12% de grãos quebrados, partidos ou chochos. 
3. Produção em Campinas, no estado de São Paulo""")
    elif s == 'Porco':
        fig = plot('Porco', Porco)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. O [Porco](https://www.cepea.esalq.usp.br/br/indicador/suino.aspx) é vendindo quilo vivo.
2. Suíno vivo pronto para abate (animal terminado, macho ou fêmea, entre 80 e 120 quilos); preço ao produtor, são considerados apenas negócios realizados (não entram na amostra os valores nominais). 
3. RS: Erechim, Santa Rosa, Serra Gaúcha e Vale do Taquari; SC: Braço do Norte e Oeste Catarinense; PR: Arapoti, Norte do Paraná e Sudoeste Paranaense; SP: Avaré, São José do Rio Preto e SP-5 (Bragança Paulista, Campinas, Piracicaba, São Paulo e Sorocaba); MG: Belo Horizonte, Ponte Nova, Patos de Minas e Sul de Minas""")
    elif s == 'Soja - Paraná':
        fig = plot('Soja - Paraná', Soja)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Soja - Paraná](https://www.cepea.esalq.usp.br/br/indicador/soja.aspx) é vendinda pelo saco de 60kg.
2. Soja em grão a granel, tipo exportação, conforme padrão Concex: até 14% de umidade, até 2% de impurezas, e limites máximos de 8% para grãos avariados (até 5% de ardidos) e 30% de grãos quebrados. 
3. O percentual de participação de cada região é determinado pela sua capacidade instalada de esmagamento segundo informações da Abiove (1997): Porto de Paranaguá (19,13%), Ponta Grossa (25,49%), Norte (34,72%), Oeste (9,73%), Sudoeste (10,93%).""")
    elif s == 'Soja - Paranaguá':
        fig = plot('Soja - Paranaguá', Soja_C)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Soja - Paranaguá](https://www.cepea.esalq.usp.br/br/indicador/soja.aspx) é vendinda pelo saco de 60kg.
2. Soja em grão a granel, tipo exportação, conforme padrão Concex: até 14% de umidade, até 2% de impurezas, e limites máximos de 8% para grãos avariados (até 5% de ardidos) e 30% de grãos quebrados. 
3. Produto posto no porto de Paranaguá, estado do Paraná, nas condições DAP no pátio ou FAS em armazéns/silos que efetuem carregamento de navios via corredor de exportação no Porto de Paranaguá.""")
    elif s == 'Trigo Paraná':
        fig = plot('Trigo Paraná', Trigo_P)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Trigo Paraná](https://www.cepea.esalq.usp.br/br/indicador/trigo.aspx) é vendinda pelo saco de 60kg.
2. Trigo Tipo 1; pH 78; teor de matérias estranhas e impurezas, no máximo 1%; grãos danificados por insetos, no máximo 0,50%; grãos danificados pelo calor, mofados e ardidos, no máximo 0,50%; grãos chocos, triguilhos e quebrados, no máximo 1,5% e total de defeitos, no máximo 2%, de acordo com a Instrução Normativa 38/2010, do Ministério da Agricultura, Pecuária e Abastecimento. 
3. Negociações do produto posto ou a retirar em regiões do estado do Paraná, divididas em: Centro-Oeste, Centro-Sul, Curitiba, Noroeste, Norte Central, Norte Pioneiro, Norte, Oeste, Paranaguá, Ponta Grossa, Prudentópolis, Sudeste e Sudoeste.""")
    elif s == 'Trigo RS':
        fig = plot('Trigo RS', Trigo_R)
        with st.beta_expander("Detalhes"):
            st.markdown("""1. A [Trigo RS](https://www.cepea.esalq.usp.br/br/indicador/trigo.aspx) é vendinda por tonelada.
2. Trigo Tipo 1; pH 78; teor de matérias estranhas e impurezas, no máximo 1%; grãos danificados por insetos, no máximo 0,50%; grãos danificados pelo calor, mofados e ardidos, no máximo 0,50%; grãos chocos, triguilhos e quebrados, no máximo 1,5% e total de defeitos, no máximo 2%, de acordo com a Instrução Normativa 38/2010, do Ministério da Agricultura, Pecuária e Abastecimento. 
3. Negociações do produto posto ou a retirar em regiões do estado do Rio Grande do Sul, divididas em: Camaquã, Campanha Central, Campanha Meridional, Campanha Ocidental, Caxias do Sul, Centro Ocidental, Centro Oriental, Guaporé, Ijuí, Metropolitana de Porto Alegre, Noroeste, Passo Fundo, Rio Grande, Pelotas, Santa Rosa, Serra de Sudeste, Sudeste, Vacaria.""")



filtro()


st.markdown(' ')
st.markdown('Feito por [Igor Esposito](https://github.com/Sposigor)')
