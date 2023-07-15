# Analise_de_Dados_Padaria_Rivera
Como o Dashboard de Vendas e Desperdício da Padaria Rivera está revolucionando a gestão de negócios

## Case
Um dia comentei com um amigo que tem uma padaria, que os dados poderiam ajudar muito até na pequena padaria dele, ele não estava muito confiante, pois ele tinha apenas algumas planilhas de excel, então decidi ajudá-lo, ele está enfrentando um alto índice de desperdício de alimentos e gostaria de encontrar maneiras de aumentar as vendas e reduzir o desperdício.


# Dashboard de Vendas e Desperdício da Padaria

![Padaria](https://content.epadoca.com/images/padaria/padaria-rivera/icon_637509014078982364.png)

Um dashboard interativo que analisa as vendas e o desperdício de produtos em uma padaria. O dashboard oferece visualizações detalhadas, previsões de demanda futura e insights valiosos para ajudar na gestão estratégica e tomada de decisões e tudo isso usando apenas uma ferramenta o Python.

## Visão Geral
O Dashboard de Vendas e Desperdício da Padaria é uma aplicação web que utiliza a biblioteca Dash para criar uma interface interativa. Ele permite explorar os dados de vendas da padaria, incluindo a quantidade vendida por produto e por categoria, o total vendido e desperdiçado, e o desperdício de produtos em formato de gráfico de rosca. Além disso, o dashboard também apresenta a previsão de demanda futura usando o modelo Prophet, proporcionando insights valiosos para o planejamento estratégico.

## Recursos
- Visualização da quantidade vendida por produto em formato de gráfico de barras.
- Visualização da quantidade vendida por categoria em formato de gráfico de barras.
- Visualização do total vendido e desperdiçado em formato de gráfico de pizza.
- Visualização do desperdício de produtos em formato de gráfico de rosca.
- Previsão de demanda futura com base nos dados históricos de vendas usando o modelo Prophet.
- Texto narrativo com estatísticas sobre as vendas e o desperdício.

## Pré-requisitos
- Python 3.10
- Bibliotecas Python: pandas, plotly, dash, dash-core-components, dash-html-components, dash-auth, prophet

## Como usar
1. Faça o clone deste repositório para o seu ambiente local.
2. Instale as bibliotecas necessárias listadas nos pré-requisitos.
3. Execute o arquivo `dashboard.py` para iniciar o dashboard.
4. Acesse o dashboard no navegador usando o link `http://localhost:8050`.
5. Digite o Login 123 e Senha 123
6. Selecione o mês e o ano desejados no dropdown para visualizar as informações atualizadas.

## O arquivo dash_app.py
- É o arquivo dash_app.py que está hospedado no Streamlit ele foi preparado para ser colocado em Produção

## Para acessar o arquivo dash_app.py no Streamlit clique no link abaixo
https://dash-padaria.streamlit.app/


## Insights

om base na análise de dados realizada e nos insights obtidos, podemos extrair algumas informações relevantes que podem subsidiar a tomada de decisão para melhorar as vendas e reduzir o desperdício na padaria. Aqui estão alguns insights que podem ser considerados:

Identificar os produtos mais vendidos: Analisar os dados de quantidade vendida por produto e categoria pode ajudar a identificar quais produtos têm maior demanda. Com base nisso, a padaria pode priorizar o estoque e o abastecimento desses itens para garantir que não faltem nas prateleiras.

Analisar a sazonalidade das vendas: Verificar os padrões de vendas ao longo do tempo, considerando meses e anos, pode revelar sazonalidades. Por exemplo, se houver um aumento nas vendas de sorvetes e picolés durante os meses mais quentes, a padaria pode adaptar seu estoque e promoções para atender a essa demanda sazonal.

Avaliar o desperdício de produtos: Analisar os dados de desperdício de produtos pode revelar quais itens estão sendo mais desperdiçados. Identificar as causas do desperdício, como prazo de validade vencido, demanda insuficiente ou problemas de armazenamento, permitirá tomar medidas para reduzir o desperdício, como ajustar as quantidades produzidas ou melhorar as práticas de armazenamento.

Explorar oportunidades de cross-selling: Analisar a correlação entre as categorias de produtos vendidos pode revelar oportunidades de cross-selling. Por exemplo, se for observada uma forte correlação entre a venda de pães e laticínios, a padaria pode criar promoções combinando esses produtos para incentivar os clientes a comprarem ambos.

Monitorar a rentabilidade por categoria: Além de analisar as vendas, é importante considerar a rentabilidade dos produtos. A padaria pode calcular a margem de lucro por categoria e identificar quais categorias são mais rentáveis. Isso pode ajudar na tomada de decisão sobre o mix de produtos e as estratégias de precificação.

Realizar análise de demanda futura: Com base nos dados históricos de vendas, é possível realizar previsões de demanda futura usando técnicas de análise de séries temporais. Isso pode ser útil para planejar o estoque, as compras de ingredientes e até mesmo para desenvolver promoções direcionadas.

Esses insights podem servir como base para tomar decisões estratégicas para aumentar as vendas e reduzir o desperdício na padaria. É importante envolver os diferentes departamentos da padaria, como produção, estoque e marketing, para implementar as ações necessárias com base nessas informações. A análise de dados contínua e a monitoração dos resultados também são fundamentais para ajustar as estratégias e garantir a eficácia das decisões tomadas.

## Autor
- Jonatan (@Jonatan-Oliveira) - https://github.com/Jonatan-Oliveira


