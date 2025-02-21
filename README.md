# Anime Progress Dashboard

A simple web application built using [Dash](https://dash.plotly.com/) to track and visualize anime watching progress. The dashboard provides detailed metrics, visualizations, and tables to make tracking anime progress more interactive and insightful. The web app is deployed using Render on [here](https://my-anime-dashboard-9.onrender.com/).

---

## Features

- **Summary Metrics**: Displays total episodes watched, completion rate, and the most common series type.
- **Interactive Charts**: 
  - Status distribution pie chart.
  - Series type distribution bar chart.
  - Scatter plot of episodes watched vs total episodes.
- **Top Incomplete Anime**: A table highlighting anime with the lowest completion rate.
- **Full Data Table**: Browse and filter all available anime series data.

---

## Requirements

To run this application, you need the following Python modules installed:

```plaintext
dash
dash-table
dash-bootstrap-components
plotly
pandas
numpy
gunicorn
