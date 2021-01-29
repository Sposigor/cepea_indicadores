from datetime import date, datetime
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def plot(titulo:str, df: pd.DataFrame):
  
  # Variaveis 
  titulo = titulo
  labels = 'US$'
  Hoje = datetime.now()
  data = df
  mode_size = 12
  line_size = 4
  x_data = data.Data
  y_data = data['Preço US$']

  # Grafico
  fig = go.Figure()

  fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines',
          name=labels,
          line=dict(color='rgb(49,130,189)', width=line_size),
          connectgaps=True,
      ))

      # Pontos Inicial e Final para marcação  
  fig.add_trace(go.Scatter(
      x=[x_data[0], x_data.iloc[-1]],
      y=[y_data[0], y_data.iloc[-1]],
      mode='markers',
      marker=dict(color='rgb(49,130,189)', size=mode_size)
      ))
  

  fig.update_layout(
      xaxis=dict(
          showline=True,
          showgrid=False,
          showticklabels=True,
          linecolor='rgb(204, 204, 204)',
          linewidth=2,
          ticks='outside',
          tickfont=dict(
              family='Arial',
              size=12,
              color='rgb(82, 82, 82)',
          ),
      ),
      yaxis=dict(
          showgrid=False,
          zeroline=False,
          showline=False,
          showticklabels=False,
      ),
      autosize=True,
      margin=dict(
          autoexpand=True,
          l=50,
          r=50,
          t=60,
      ),
      showlegend=False,
      plot_bgcolor='white'
  )

  # Variaveis
  annotations = []
  crecimento = (y_data.iloc[-1] - y_data[0])/y_data[0]

  # Ajusta o lado esquerdo do grafico
  annotations.append(dict(xref='paper', x=0.05, y=y_data[0],
                                    xanchor='right', yanchor='middle',
                                    text=labels + ' {}'.format(y_data[0]),
                                    font=dict(family='Arial',
                                              size=14),
                                    showarrow=False))
  # Ajusta o lado direito do grafico
  annotations.append(dict(xref='paper', x=0.95, y=y_data.iloc[-1],
                                    xanchor='left', yanchor='middle',
                                    text=labels +' {}'.format(y_data.iloc[-1]),
                                    font=dict(family='Arial',
                                              size=14),
                                    showarrow=False))
  # Titulo
  annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                xanchor='left', yanchor='bottom',
                                text=titulo,
                                font=dict(family='Arial',
                                          size=30,
                                          color='rgb(37,37,37)'),
                                showarrow=False))
  # Fonte
  annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                xanchor='center', yanchor='top',
                                text='Fonte: CEPEA',
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))
  # Data
  annotations.append(dict(xref='paper', yref='paper', x=1, y=-0.1,
                                xanchor='right', yanchor='top',
                                text='{}'.format(Hoje.strftime("%B %d, %Y")),
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))
  # Crescimento %
  annotations.append(dict(xref='paper', yref='paper', x=1, y=0.05,
                                xanchor='right', yanchor='top',
                                text='Crecimento de {:.2f}% em relação ao valor inicial'.format(crecimento*100),
                                font=dict(family='Arial',
                                          size=12,
                                          color='rgb(150,150,150)'),
                                showarrow=False))




  fig.update_layout(annotations=annotations)

  return  st.plotly_chart(fig, use_container_width=True)