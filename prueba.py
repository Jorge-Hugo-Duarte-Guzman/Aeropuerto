import streamlit as st
import pandas as pd
ruta = 'https://github.com/Jorge-Hugo-Duarte-Guzman/practica-github/raw/refs/heads/main/BD%20Pax%20febrero%202026.csv'
df = pd.read_csv(ruta, sep=';', encoding='latin1')
st.title("Mi segunda app con Streamlit")
st.write("Este es un párrafo de prueba para la clase.")
st.dataframe(df.head(5))
st.subheader("Gráfico de pasajeros por tipo de aviación")

df['Total'] = df['Pax Nac. Entrados'] + df['Pax Int. Entrados']
total_pasajeros = df['Total'].sum()
st.write(f"El total de pasajeros es: {total_pasajeros}")

df_grafico = df.groupby('Aviacion')['Total'].sum().reset_index()
st.bar_chart(
    data=df_grafico, 
    x='Aviacion', 
    y='Total')


df_tipo_vuelo = df['Aviacion'].value_counts().reset_index()
st.dataframe(df_tipo_vuelo)