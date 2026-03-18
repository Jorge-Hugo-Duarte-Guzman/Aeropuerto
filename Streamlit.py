import pandas as pd
import streamlit as st

#********* CARGA DE LOS DATOS *********
ruta = 'https://raw.githubusercontent.com/Jorge-Hugo-Duarte-Guzman/practica-github/refs/heads/main/Operaciones_a%C3%A9reas_acumuladas_en_Colombia_20260304.csv'
df = pd.read_csv(ruta)

#*********ANÁLISIS Y PROCESAMIENTO *********
df_tipo_vuelo = df['TIPO_VUELO'].value_counts().reset_index()
estadisticos = df_tipo_vuelo['count'].describe()
maximo = estadisticos['max']
minimo = estadisticos['min']
media = estadisticos['mean']

#********* VISUALIZACION DE LOS DATOS *********
st.title('Datos Operaciones')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Mínimo', f'{minimo:.0f}', border=True)
with col2:
    st.metric('Media', f'{media:.0f}', border=True)
with col3:
    st.metric('Máximo', f'{maximo:.0f}', border=True)


st.dataframe(df.head(5))