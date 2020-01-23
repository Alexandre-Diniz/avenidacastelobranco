import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

path = 'data/casteloBranco.csv'
df = pd.read_csv(path, low_memory=False)
# grafico 1
df['data_inicio_atividade'] = pd.to_datetime(df['data_inicio_atividade'])
df['data_situacao_cadastral'] = pd.to_datetime(df['data_situacao_cadastral'])

df['mes_inicio_atividade'] = df['data_inicio_atividade'].apply(lambda x: x.month)
df['ano_inicio_atividade'] = df['data_inicio_atividade'].apply(lambda x: x.year)

df['mes_situacao_cadastral'] = df['data_situacao_cadastral'].apply(lambda x: x.month)
df['ano_situacao_cadastral'] = df['data_situacao_cadastral'].apply(lambda x: x.year)

df['data'] = df['data_situacao_cadastral'].apply(lambda x: pd.to_datetime(str(x.month)+'-'+str(x.year)))

nula = df[df['situacao_cadastral']==1][['mes_situacao_cadastral', 'ano_situacao_cadastral', 'data']].sort_values(by=['ano_situacao_cadastral','mes_situacao_cadastral'])
ativa = df[df['situacao_cadastral']==2][['mes_situacao_cadastral', 'ano_situacao_cadastral', 'data']].sort_values(by=['ano_situacao_cadastral','mes_situacao_cadastral'])
suspensa = df[df['situacao_cadastral']==3][['mes_situacao_cadastral', 'ano_situacao_cadastral', 'data']].sort_values(by=['ano_situacao_cadastral','mes_situacao_cadastral'])
inapta = df[df['situacao_cadastral']==4][['mes_situacao_cadastral', 'ano_situacao_cadastral', 'data']].sort_values(by=['ano_situacao_cadastral','mes_situacao_cadastral'])
baixada = df[df['situacao_cadastral']==8][['mes_situacao_cadastral', 'ano_situacao_cadastral', 'data']].sort_values(by=['ano_situacao_cadastral','mes_situacao_cadastral'])

nula['cumFreq'] = np.array([1]*nula.shape[0]).cumsum()
ativa['cumFreq'] = np.array([1]*ativa.shape[0]).cumsum()
suspensa['cumFreq'] = np.array([1]*suspensa.shape[0]).cumsum()
inapta['cumFreq'] = np.array([1]*inapta.shape[0]).cumsum()
baixada['cumFreq'] = np.array([1]*baixada.shape[0]).cumsum()

nula['Freq'] = np.array([1]*nula.shape[0])
ativa['Freq'] = np.array([1]*ativa.shape[0])
suspensa['Freq'] = np.array([1]*suspensa.shape[0])
inapta['Freq'] = np.array([1]*inapta.shape[0])
baixada['Freq'] = np.array([1]*baixada.shape[0])

################## Gráfico 1 ##################

trace1_1 = go.Scatter(x=df['mes_ano_abertura'].value_counts().sort_index().index,
                y=df['mes_ano_abertura'].value_counts().sort_index().values,
                name="Abertas",
                marker={'color':'blue'},
                opacity=0.8,
                showlegend=True)

trace1_2 = go.Scatter(x=baixada['data'].value_counts().sort_index().index,
                    y=baixada['data'].value_counts().sort_index().values,
                    name="Fechada",
                    marker={'color':'red'},
                    opacity=0.8)

trace1_3 = go.Scatter(x=ativa['data'].value_counts().sort_index().index,
                    y=ativa['data'].value_counts().sort_index().values,
                    name="Ativa",
                    marker={'color':'green'},
                    opacity=0.8)

data1 = [trace1_1, trace1_2, trace1_3]

layout1 = go.Layout(width=700, height=300,
                  xaxis_range=['2014-10','2015-04'],#, df['mes_ano_abertura'].value_counts().index.max()],
                  yaxis_range=[0,60],
                  #xaxis_title="Período",
                  #yaxis_title='Quantidade de Empresas',
                  plot_bgcolor='green',
                  paper_bgcolor="LightSteelBlue",
                  margin=dict(l=20, r=20, t=20, b=20))

figure1 = {
    'data':data1,
    'layout':layout1
}

fig1 = go.Figure(figure1)

################## Gráfico 2 ##################

a = df[(pd.to_datetime(df['mes_ano_abertura'])>=pd.to_datetime('10-2014'))&(pd.to_datetime(df['mes_ano_abertura'])<=pd.to_datetime('04-2015'))]['mes_ano_abertura'].value_counts().values.sum()
b = baixada[(baixada['data']>=pd.to_datetime('10-2014'))&(baixada['data']<=pd.to_datetime('04-2015'))]['data'].value_counts().values.sum()
c = ativa[(ativa['data']>=pd.to_datetime('10-2014'))&(ativa['data']<=pd.to_datetime('04-2015'))]['data'].value_counts().values.sum()

bar_data = [a,b,c]
bar_label = ['Aberta', 'Fechada', 'Ativa']

colors = ['blue', 'red', 'green']

trace2_1 = go.Pie(labels=bar_label, values=bar_data, hole=.3,
               opacity=0.8)
data2_1 = [trace2_1]
layout2_1 = go.Layout(width=300, 
                  height=300,
                  margin=dict(l=20, r=20, t=20, b=20))
figure2_1 = {
    'data':data2_1,
    'layout':layout2_1
}
fig2 = go.Figure(figure2_1)
fig2.update_traces(textinfo='value', textfont_size=20, textfont=dict(color='black'),
                  marker=dict(colors=colors, line=dict(color='black', width=2)))