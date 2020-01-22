import dash_core_components as dcc
import dash_html_components as html
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

df['mes_ano_abertura'] = df['data_inicio_atividade'].apply(lambda x: pd.to_datetime(str(x.month)+'-'+str(x.year)))

fig1 = go.Figure()

trace1 = go.Bar(x=df['mes_ano_abertura'].value_counts().sort_index().index,
                y=df['mes_ano_abertura'].value_counts().sort_index().values,
                name="Abertas",
                marker={'color':'rgb(100,100,160)'},
                opacity=0.8,
                showlegend=True)

trace2 = go.Scatter(x=ativa['data'].value_counts().sort_index().index,
                    y=ativa['data'].value_counts().sort_index().values,
                    name="Ativa",
                    marker={'color':'red'},
                    opacity=0.8)

data1 = [trace1, trace2]

layout1 = go.Layout(width=700, height=400,
                  xaxis_range=['2015', df['mes_ano_abertura'].value_counts().index.max()],
                  yaxis_range=[0,6],
                  #title_text="Empresas Abertas e Ativas na Avenida Castelo Branco no Período de 2015-2019",
                  xaxis_title="Período",
                  yaxis_title='Quantidade de Empresas',
                  plot_bgcolor='white')

figure1 = {
    'data':data1,
    'layout':layout1
}

# grafico 2

value1 = [ativa[(ativa['ano_situacao_cadastral']==2014)&(ativa['mes_situacao_cadastral']==12)]['Freq'].sum(),
         baixada[(baixada['ano_situacao_cadastral']==2014)&(baixada['mes_situacao_cadastral']==12)]['Freq'].sum(),
         suspensa[(suspensa['ano_situacao_cadastral']==2014)&(suspensa['mes_situacao_cadastral']==12)]['Freq'].sum(),
         inapta[(inapta['ano_situacao_cadastral']==2014)&(inapta['mes_situacao_cadastral']==12)]['Freq'].sum()]

value2 = [ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==1)]['Freq'].sum(),
         baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==1)]['Freq'].sum(),
         suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==1)]['Freq'].sum(),
         inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==1)]['Freq'].sum()]

value3 = [ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==2)]['Freq'].sum(),
         baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==2)]['Freq'].sum(),
         suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==2)]['Freq'].sum(),
         inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==2)]['Freq'].sum()]

value4 = [ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==3)]['Freq'].sum(),
         baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==3)]['Freq'].sum(),
         suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==3)]['Freq'].sum(),
         inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==3)]['Freq'].sum()]

labels = ['Ativa', 'Fechada', 'Suspensa', 'Inapta']

specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]

fig2 = make_subplots(2, 2, specs=specs,
                    subplot_titles=['Dez 2014', 'Jan 2015', 'Fev 2015', 'Mar 2015'])

fig2.add_trace(go.Pie(labels=labels, 
                     values=value1, 
                     #scalegroup='one',
                     name="Dez 2014"), 1, 1)

fig2.add_trace(go.Pie(labels=labels, 
                     values=value2, 
                     #scalegroup='one',
                     name="Jan 2015"), 1, 2)

fig2.add_trace(go.Pie(labels=labels, 
                     values=value3, 
                     #scalegroup='one',
                     name="Fev 2015"), 2, 1)

fig2.add_trace(go.Pie(labels=labels, 
                     values=value4, 
                     #scalegroup='one',
                     name="Mar 2015"), 2, 2)

fig2.update_traces(hole=.0, textinfo='none')
fig2.update_layout(height=400, width=445,
                 annotations=[dict(text='Dez 2014', x=0.18, y=1, font_size=20, showarrow=False),
                              dict(text='Jan 2015', x=0.82, y=1, font_size=20, showarrow=False),
                              dict(text='Fev 2015', x=0.18, y=-0.1, font_size=20, showarrow=False),
                              dict(text='Mar 2015', x=0.82, y=-0.1, font_size=20, showarrow=False)])


# grafico 3

value1 = [ativa[(ativa['ano_situacao_cadastral']==2014)&(ativa['mes_situacao_cadastral']==12)]['Freq'].sum(),
          ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==1)]['Freq'].sum(),
          ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==2)]['Freq'].sum(),
          ativa[(ativa['ano_situacao_cadastral']==2015)&(ativa['mes_situacao_cadastral']==3)]['Freq'].sum()]

value2 = [baixada[(baixada['ano_situacao_cadastral']==2014)&(baixada['mes_situacao_cadastral']==12)]['Freq'].sum(),
          baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==1)]['Freq'].sum(),
          baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==2)]['Freq'].sum(),
          baixada[(baixada['ano_situacao_cadastral']==2015)&(baixada['mes_situacao_cadastral']==3)]['Freq'].sum()]

value3 = [suspensa[(suspensa['ano_situacao_cadastral']==2014)&(suspensa['mes_situacao_cadastral']==12)]['Freq'].sum(),
          suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==1)]['Freq'].sum(),
          suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==2)]['Freq'].sum(),
          suspensa[(suspensa['ano_situacao_cadastral']==2015)&(suspensa['mes_situacao_cadastral']==3)]['Freq'].sum()]

value4 = [inapta[(inapta['ano_situacao_cadastral']==2014)&(inapta['mes_situacao_cadastral']==12)]['Freq'].sum(),
          inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==1)]['Freq'].sum(),
          inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==2)]['Freq'].sum(),
          inapta[(inapta['ano_situacao_cadastral']==2015)&(inapta['mes_situacao_cadastral']==3)]['Freq'].sum()]

labels = ['Dez 2014', 'Jan 2015', 'Fev 2015', 'Mar 2015']

trace1 = go.Bar(x=labels,
                y=value1,
                name="Abertas",
                opacity=0.8,
                showlegend=True)
trace2 = go.Bar(x=labels,
                y=value2,
                name="Suspensa",
                opacity=0.8,
                showlegend=True)
trace3 = go.Bar(x=labels,
                y=value3,
                name="Fechada",
                opacity=0.8,
                showlegend=True)
trace4 = go.Bar(x=labels,
                y=value4,
                name="Inapta",
                opacity=0.8,
                showlegend=True)


data3 = [trace1, trace2, trace3, trace4]

layout3 = go.Layout(width=445, height=400,
                   xaxis_title="Período",
                   yaxis_title='Quantidade de Empresas',
                   plot_bgcolor='white')

figure3 = {
    'data':data3,
    'layout':layout3
}

fig3 = go.Figure(figure3)

# grafico 4

fig4 = go.Figure()
fig4.add_trace(go.Scatter(
                x=nula[nula['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().index,
                y=nula[nula['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().values,
                name="Nula",
                #line_color='deepskyblue',
                opacity=0.8))

fig4.add_trace(go.Scatter(
                x=ativa[ativa['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().index,
                y=ativa[ativa['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().values,
                name="Ativa",
                #line_color='deepskyblue',
                opacity=0.8))

fig4.add_trace(go.Scatter(
                x=suspensa[suspensa['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().index,
                y=suspensa[suspensa['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().values,
                name="Suspensa",
                #line_color='deepskyblue',
                opacity=0.8))

fig4.add_trace(go.Scatter(
                x=inapta[inapta['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().index,
                y=inapta[inapta['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().values,
                name="Inapta",
                #line_color='deepskyblue',
                opacity=0.8))

fig4.add_trace(go.Scatter(
                x=baixada[baixada['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().index,
                y=baixada[baixada['data']>=pd.to_datetime('2015')]['data'].value_counts().sort_index().values,
                name="Fechada",
                #line_color='deepskyblue',
                opacity=0.8))

# Use date string to set xaxis range
fig4.update_layout(width=700, height=400,
				   xaxis_range=['2015', '31-12-2019'],
                   plot_bgcolor='white')

##########################################

layout = html.Div(className='root', children=[

	html.Div(className='header', children=[
		html.H1('Header')
	]),

	html.Div(className='div-1', children=[

		html.Div(className='graph-1', children=[
			html.H6(
				'Situação 2015-2019'
			),
			dcc.Graph(
				figure=figure1
			),
			dcc.Graph(
				figure=fig4
			)
		]),
		html.Div(className='data-1', children=[
			html.Div([
				dcc.Graph(
					figure=fig2
				),
				dcc.Graph(
					figure=fig3
				)
			], style={'position':'relative', 'display': 'inline-block', 'height':'100%'})
		])

	]),
])