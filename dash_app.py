import pandas as pd
import plotly.express as px
from prophet import Prophet
import streamlit as st

# Carregar o DataFrame com os dados
df = pd.read_csv('dados_padaria.csv')

# Criar uma nova coluna no DataFrame para o mês e o ano das vendas
df['Data'] = pd.to_datetime(df['Data'])
df['Ano_Mes'] = df['Data'].dt.strftime('%Y-%m')

# Criar uma lista de meses e anos únicos para a navegação no storytelling
meses_anos = df['Ano_Mes'].unique().tolist()

# Ordenar em ordem decrescente
meses_anos = sorted(meses_anos, reverse=True)

# Título e descrição do dashboard
st.image("https://content.epadoca.com/images/padaria/padaria-rivera/icon_637509014078982364.png", width=500)
st.title('Dashboard de Vendas e Desperdício da Padaria')
st.markdown('Um histórico sobre as vendas e o desperdício de produtos da padaria')

# Dropdown para selecionar o mês e o ano
mes_ano_selecionado = st.selectbox('Selecione o mês e o ano', meses_anos)

# Filtrar o DataFrame pelo mês e ano selecionado
df_mes_ano = df[df['Ano_Mes'] == mes_ano_selecionado]

# Verificar se o DataFrame filtrado tem pelo menos 2 linhas não nulas
if df_mes_ano.dropna().shape[0] < 2:
    st.warning('Não há dados suficientes para exibir as visualizações.')
else:
    # Criar a visualização da quantidade vendida por produto
    fig_quantidade_vendida = px.bar(df_mes_ano, x='Produto', y='Quantidade Vendida', color='Categoria',
                                    title=f'Quantidade vendida por produto - {mes_ano_selecionado}')
    st.plotly_chart(fig_quantidade_vendida)

    # Criar a visualização da quantidade vendida por categoria
    fig_quantidade_vendida_categoria = px.bar(df_mes_ano, x='Categoria', y='Quantidade Vendida', color='Categoria',
                                              title=f'Quantidade vendida por categoria - {mes_ano_selecionado}')
    st.plotly_chart(fig_quantidade_vendida_categoria)

    # Calcular o total vendido e desperdiçado
    total_vendido = df_mes_ano['Quantidade Vendida'].sum()
    total_desperdicado = df_mes_ano['Quantidade Desperdiçada'].sum()

    # Criar a visualização do total vendido e desperdiçado
    fig_total_vendido_desperdicado = px.pie(names=['Vendido', 'Desperdiçado'], values=[total_vendido, total_desperdicado],
                                            title=f'Total vendido e desperdiçado - {mes_ano_selecionado}')
    st.plotly_chart(fig_total_vendido_desperdicado)

    # Criar a visualização do desperdício de produtos (gráfico de rosca)
    fig_desperdicio_produtos = px.pie(df_mes_ano, names='Produto', values='Quantidade Desperdiçada',
                                      title=f'Desperdício de produtos - {mes_ano_selecionado}', hole=0.5)
    st.plotly_chart(fig_desperdicio_produtos)

    # Calcular estatísticas sobre as vendas e o desperdício
    taxa_desperdicio = total_desperdicado / total_vendido * 100

    # Texto narrativo sobre as vendas e o desperdício
    storytelling_text = f"No mês de {mes_ano_selecionado}, foram vendidos um total de {total_vendido} produtos na padaria. " \
                        f"Infelizmente, {total_desperdicado} produtos foram desperdiçados, resultando em uma taxa " \
                        f"de desperdício de {taxa_desperdicio:.2f}%."
    st.markdown(storytelling_text)

    # Filtrar o DataFrame pelo mês e ano selecionado e agrupar por dia
    df_mes_ano_daily = df_mes_ano.groupby('Data').sum().reset_index()

    # Verificar se o DataFrame filtrado tem pelo menos 2 linhas não nulas para a previsão de demanda futura
    if df_mes_ano_daily.dropna().shape[0] < 2:
        st.warning('Não há dados suficientes para fazer a previsão de demanda futura.')
    else:
        # Preparar os dados para o modelo Prophet
        data_prophet = df_mes_ano_daily[['Data', 'Quantidade Vendida']].rename(columns={'Data': 'ds', 'Quantidade Vendida': 'y'})

        # Criar o modelo Prophet e ajustar aos dados
        model = Prophet()
        model.fit(data_prophet)

        # Criar DataFrame com datas futuras para fazer a previsão
        future_dates = model.make_future_dataframe(periods=30)  # Previsão para os próximos 30 dias
        future_dates = future_dates[future_dates['ds'].dt.month == pd.to_datetime(mes_ano_selecionado).month]  # Filtrar pelo mês selecionado

        # Fazer a previsão de demanda futura
        forecast = model.predict(future_dates)

        # Criar a visualização da previsão de demanda futura
        fig_previsao_demanda = px.line(df_mes_ano_daily, x='Data', y='Quantidade Vendida',
                                       title=f'Previsão de demanda futura - {mes_ano_selecionado}')
        fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Previsão')
        fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Limite Inferior')
        fig_previsao_demanda.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Limite Superior')
        st.plotly_chart(fig_previsao_demanda)

# EXECUTAR NO TERMINAL O COMANDO 
# streamlit run dash_app.py