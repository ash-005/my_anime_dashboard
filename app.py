import pandas as pd
import numpy as np
import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px

filename = 'cleaned_data.csv'
df = pd.read_csv(filename)
df.head()

df['completion_rate'] = (df['my_watched_episodes'] / df['series_episodes']).fillna(0) * 100
series_type_counts = df['series_type'].value_counts().reset_index()
series_type_counts.columns = ['series_type', 'count']

app = dash.Dash(__name__)
app.title = "Ash's Anime Dashboard"
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1("Anime Progress Dashboard", style={"textAlign": "center"}),
        html.Div([
            html.Div([
                html.H4("Total Episodes Watched"),
                html.P(df['my_watched_episodes'].sum())
            ], className="metric"),
            html.Div([
                html.H4("Completion Rate (%)"),
                html.P(f"{df['completion_rate'].mean():.2f}")
            ], className="metric"),
            html.Div([
                html.H4("Most Common Series Type"),
                html.P(df['series_type'].mode()[0])
            ], className="metric"),
        ], className="metrics-row")
    ], className="header"),

    html.Div([
        html.Div([
            dcc.Graph(
                id='status-pie-chart',
                figure=px.pie(
                    df,
                    names='my_status',
                    title="Status Distribution",
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.RdBu
                )
            )
        ], className="chart"),

    html.Div([
    html.H3('Series Type Distribution'),
    dcc.Graph(
        id='type-bar-chart',
        figure=px.bar(
            series_type_counts,
            x='series_type',
            y='count',
            title='Anime Series Type Distribution',
            labels={'series_type': 'Series Type', 'count': 'Count'},
            color='series_type'
               )
            )
        ], className="chart"),
    ], className="visualizations"),

    html.Div([
        dcc.Graph(
            id='completion-scatter',
            figure=px.scatter(
                df,
                x='series_episodes',
                y='my_watched_episodes',
                color='my_status',
                size='series_episodes',
                hover_data=['series_title'],
                title="Completion Progress",
                labels={"series_episodes": "Total Episodes", "my_watched_episodes": "Watched Episodes"}
            )
        )
    ], className="chart"),

    html.Div([
        html.H4("Top Incomplete Anime"),
        dash_table.DataTable(
            id='top-incomplete-table',
            columns=[
                {"name": "Title", "id": "series_title"},
                {"name": "Total Episodes", "id": "series_episodes"},
                {"name": "Watched Episodes", "id": "my_watched_episodes"},
                {"name": "Completion Rate (%)", "id": "completion_rate"}
            ],
            data=df.sort_values("completion_rate").head(10).to_dict("records"),
            style_table={'overflowX': 'auto'},
            style_cell={
                'textAlign': 'left',
                'padding': '5px'
            },
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        )
    ], className="table-section"),

    html.Div([
        html.H4("Browse All Series"),
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            filter_action="native",
            sort_action="native",
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={
                'textAlign': 'left',
                'padding': '5px'
            },
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        )
    ], className="table-section")
], className="container")

if __name__ == "__main__":
    app.run_server(debug=True)
