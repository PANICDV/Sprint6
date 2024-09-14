import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")
st.header("Cuadro de Mandos de Anuncios de Vehículos")

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para precio vs. año')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

