import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_auth import BasicAuth
from prophet import Prophet

# Carregar o DataFrame com os dados
df = pd.read_csv('dados_padaria.csv')

# Criar uma nova coluna no DataFrame para o mês e o ano das vendas
df['Data'] = pd.to_datetime(df['Data'])
df['Ano_Mes'] = df['Data'].dt.strftime('%Y-%m')

# Criar uma lista de meses e anos únicos para a navegação no storytelling
meses_anos = df['Ano_Mes'].unique().tolist()

# Criar layout do dashboard
app = dash.Dash(__name__, external_stylesheets=['styles.css'])

# Definir informações de autenticação
VALID_USERNAME_PASSWORD_PAIRS = [
    ['123', '123']
]
auth = BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# Cores gradiente de fundo
gradient_image = "https://via.placeholder.com/1000x600.png?text=Gradient+Background"

app.layout = html.Div(
    children=[
        html.Img(src="https://content.epadoca.com/images/padaria/padaria-rivera/icon_637509014078982364.png",
                 style={'width': '300px', 'margin': 'auto', 'display': 'block'}),
        html.H1(children='Dashboard de Vendas e Desperdício da Padaria', style={'textAlign': 'center'}),
        html.Div(children='Um histórico sobre as vendas e o desperdício de produtos da padaria',
                 style={'textAlign': 'center'}),

        # Dropdown para selecionar o mês e o ano
        dcc.Dropdown(
            id='dropdown-mes-ano',
            options=[{'label': mes_ano, 'value': mes_ano} for mes_ano in meses_anos],
            value=meses_anos[0],
            style={'width': '200px', 'margin': 'auto'}
        ),

        # Visualização da quantidade vendida por produto
        html.Div(
            children=[
                html.H2(children='Quantidade vendida por produto', style={'textAlign': 'center'}),
                dcc.Graph(id='graph-quantidade-vendida'),
            ],
            style={'backgroundColor': 'white', 'border': '1px solid gray', 'border-radius': '5px', 'margin': '20px',
                   'padding': '20px'}
        ),

        # Visualização da quantidade vendida por categoria
        html.Div(
            children=[
                html.H2(children='Quantidade vendida por categoria', style={'textAlign': 'center'}),
                dcc.Graph(id='graph-quantidade-vendida-categoria'),
            ],
            style={'backgroundColor': 'white', 'border': '1px solid gray', 'border-radius': '5px', 'margin': '20px',
                   'padding': '20px'}
        ),

        # Visualização do total vendido e desperdiçado
        html.Div(
            children=[
                html.H2(children='Total vendido e desperdiçado', style={'textAlign': 'center'}),
                dcc.Graph(id='graph-total-vendido-desperdicado'),
            ],
            style={'backgroundColor': 'white', 'border': '1px solid gray', 'border-radius': '5px', 'margin': '20px',
                   'padding': '20px'}
        ),

        # Visualização do desperdício de produtos
        html.Div(
            children=[
                html.H2(children='Desperdício de produtos', style={'textAlign': 'center'}),
                dcc.Graph(id='graph-desperdicio-produtos'),
            ],
            style={'backgroundColor': 'white', 'border': '1px solid gray', 'border-radius': '5px', 'margin': '20px',
                   'padding': '20px'}
        ),

        # Visualização da previsão de demanda futura
        html.Div(
            children=[
                html.H2(children='Previsão de demanda futura', style={'textAlign': 'center'}),
                dcc.Graph(id='graph-previsao-demanda'),
            ],
            style={'backgroundColor': 'white', 'border': '1px solid gray', 'border-radius': '5px', 'margin': '20px',
                   'padding': '20px'}
        ),

        # Texto narrativo
        html.Div(id='storytelling-text', style={'margin': '20px'})
    ],
    style={
        'background-image': f"url('{gradient_image}')",
        'background-size': 'cover',
        'background-position': 'center',
        'height': '100vh',
        'padding': '20px'
    }
)


@app.callback(
    dash.dependencies.Output('graph-quantidade-vendida', 'figure'),
    dash.dependencies.Output('graph-quantidade-vendida-categoria', 'figure'),
    dash.dependencies.Output('graph-total-vendido-desperdicado', 'figure'),
    dash.dependencies.Output('graph-desperdicio-produtos', 'figure'),
    dash.dependencies.Output('storytelling-text', 'children'),
    dash.dependencies.Output('graph-previsao-demanda', 'figure'),
    [dash.dependencies.Input('dropdown-mes-ano', 'value')]
)
def update_graphs(mes_ano):
    # Filtrar o DataFrame pelo mês e ano selecionado
    df_mes_ano = df[df['Ano_Mes'] == mes_ano]

    # Verificar se o DataFrame filtrado tem pelo menos 2 linhas não nulas
    if df_mes_ano.dropna().shape[0] < 2:
        empty_figure = px.scatter()  # Figura vazia
        return empty_figure, empty_figure, empty_figure, empty_figure, '', empty_figure

    # Criar a visualização da quantidade vendida por produto
    fig_quantidade_vendida = px.bar(df_mes_ano, x='Produto', y='Quantidade Vendida', color='Categoria',
                                    title=f'Quantidade vendida por produto - {mes_ano}')

    # Criar a visualização da quantidade vendida por categoria
    fig_quantidade_vendida_categoria = px.bar(df_mes_ano, x='Categoria', y='Quantidade Vendida', color='Categoria',
                                              title=f'Quantidade vendida por categoria - {mes_ano}')

    # Calcular o total vendido e desperdiçado
    total_vendido = df_mes_ano['Quantidade Vendida'].sum()
    total_desperdicado = df_mes_ano['Quantidade Desperdiçada'].sum()

    # Criar a visualização do total vendido e desperdiçado
    fig_total_vendido_desperdicado = px.pie(names=['Vendido', 'Desperdiçado'], values=[total_vendido, total_desperdicado],
                                            title=f'Total vendido e desperdiçado - {mes_ano}')

    # Criar a visualização do desperdício de produtos (gráfico de rosca)
    fig_desperdicio_produtos = px.pie(df_mes_ano, names='Produto', values='Quantidade Desperdiçada',
                                      title=f'Desperdício de produtos - {mes_ano}', hole=0.5)

    # Calcular estatísticas sobre as vendas e o desperdício
    taxa_desperdicio = total_desperdicado / total_vendido * 100

    # Texto narrativo sobre as vendas e o desperdício
    storytelling_text = f"No mês de {mes_ano}, foram vendidos um total de {total_vendido} produtos na padaria. " \
                        f"Infelizmente, {total_desperdicado} produtos foram desperdiçados, resultando em uma taxa " \
                        f"de desperdício de {taxa_desperdicio:.2f}%."

    # Filtrar o DataFrame pelo mês e ano selecionado e agrupar por dia
    df_mes_ano_daily = df_mes_ano.groupby('Data').sum().reset_index()

    # Verificar se o DataFrame filtrado tem pelo menos 2 linhas não nulas para a previsão de demanda futura
    if df_mes_ano_daily.dropna().shape[0] < 2:
        empty_figure = px.scatter()  # Figura vazia
        return fig_quantidade_vendida, fig_quantidade_vendida_categoria, fig_total_vendido_desperdicado, \
               fig_desperdicio_produtos, storytelling_text, empty_figure

    # Preparar os dados para o modelo Prophet
    data_prophet = df_mes_ano_daily[['Data', 'Quantidade Vendida']].rename(columns={'Data': 'ds', 'Quantidade Vendida': 'y'})

    # Criar o modelo Prophet e ajustar aos dados
    model = Prophet()
    model.fit(data_prophet)

    # Criar DataFrame com datas futuras para fazer a previsão
    future_dates = model.make_future_dataframe(periods=30)  # Previsão para os próximos 30 dias
    future_dates = future_dates[future_dates['ds'].dt.month == pd.to_datetime(mes_ano).month]  # Filtrar pelo mês selecionado

    # Fazer a previsão de demanda futura
    forecast = model.predict(future_dates)

    # Criar a visualização da previsão de demanda futura
    fig_previsao_demanda = px.line(df_mes_ano_daily, x='Data', y='Quantidade Vendida',
                                   title=f'Previsão de demanda futura - {mes_ano}')
    fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Previsão')
    fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Limite Inferior')
    fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Limite Superior')

    return fig_quantidade_vendida, fig_quantidade_vendida_categoria, fig_total_vendido_desperdicado, \
           fig_desperdicio_produtos, storytelling_text, fig_previsao_demanda


# Executar o dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
