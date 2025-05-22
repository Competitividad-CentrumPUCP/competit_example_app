import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Configuracion de la página
st.set_page_config(page_title="Dashboard", layout="wide")

#Título Principal
st.title("Data Visualization Dashboard")
st.markdown("### Explorando diferentes bibliotecas de visualizacion en Python")

#1. Introduccion

with st.expander("Introducción", expanded=True):
    st.markdown("""
    Esta aplicación demuestra el uso de diferentes bibliotecas de visualización en Python:
    * **Matplotlib**: Biblioteca base para visualización
    * **Seaborn**: Visualizaciones estadísticas de alto nivel
    * **Plotly**: Gráficos interactivos
    * **Streamlit**: Framework para la aplicación de datos
    """)

try:
    prog_df = pd.read_excel("dash_data.xlsx", sheet_name="Programming_Languagues")
    iris_df = pd.read_excel("dash_data.xlsx", sheet_name="Hoja2")
    st.success("Datos cargados exitosamente")

    # 3. Visualizaciones con Matplotlib
    st.header("Visualizaciones con Matplotlib")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gráfico de Dispersión")
            fig, ax = plt.subplots(figsize=(8,6))
            languages = prog_df['language'].head(5)
            popularity = prog_df['popularity'].head(5)
            ax.scatter(languages, popularity, color = 'blue', alpha = 0.6)
            plt.xticks(rotation=45)
            plt.title('Popularidad de Lenguajes de Programación')
            plt.xlabel('Lenguaje')
            plt.ylabel('Popularidad')
            st.pyplot(fig)
            plt.close() 
        with col2:
            st.subheader("Gráfico de Barras")
            fig, ax = plt.subplots(figsize=(8,6))
            languages =  prog_df['language'].head(5)
            popularity = prog_df['popularity'].head(5)
            ax.bar(languages, popularity, color = 'skyblue')
            plt.xticks(rotation=45)
            plt.title('Comparación de Popularidad')
            plt.xlabel('Lenguaje')
            plt.ylabel('Popularidad')
            st.pyplot(fig)
            plt.close() 

    # 4. Visualizaciones con Seaborn
    st.header("Visualizaciones con Seaborn")
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Gráfico de Violin")
            fig, ax = plt.subplots(figsize=(8,6))
            sns.violinplot(data=iris_df, x='species', y='sepal_lenght')
            plt.xticks(rotation=45)
            plt.title('Distribución de Longitud del Sepalo por Especie')
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("Gráfico de Caja")
            fig, ax = plt.subplots(figsize = (8,6))
            sns.boxplot(data=iris_df, x='species', y='petal_length')
            plt.xticks(rotation=45)
            plt.title('Estadísticas de Longitud del Pétalo por Especie')
            st.pyplot(fig)
            plt.close()

    # 5. Visualizaciones interactivas con Plotly
    st.header("Visualizaciones Interactivas con Plotly")
    with st.container():
        # Gráfico de línea interactivo
        fig = px.line(prog_df, x='language', y='popularity',
                      title='Tendencia de Popularidad',
                      markers=True)
        st.plotly_chart(fig, use_container_width=True)

        # Gráfico de Pastel o Torta
        fig = px.pie(prog_df, values='popularity', names='language',
                     title='Distribución de Popularidad')
        st.plotly_chart(fig, use_container_width=True)

    # 6. Sección Interactiva
    st.header("Sección Interactiva")

    #Selector de dataset
    dataset_choice = st.radio("Selecciona el conjunto de datos",
                              ["Lenguajes de Programación", "Iris Dataset"])
    
    if dataset_choice == "Lenguajes de Programación":
        df = prog_df
    else:
        df = iris_df

    #Selector de visualización
    chart_type = st.selectbox("Selecciona el tipó de gráfico",
                              ["Barras", "Dispersión", "Linea"])
    
    # Selector de datos
    x_axis = st.selectbox("Selecciona el eje X", df.columns)
    y_axis = st.selectbox("Selecciona el eje Y", df.columns)

    # Generar el gráfico seleccionado
    if chart_type == "Barras":
        fig = px.bar(df, x = x_axis, y = y_axis)
    elif chart_type == "Dispersión":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    else:
        fig = px.line(df, x = x_axis, y = y_axis)
    st.plotly_chart(fig, use_container_width=True)

    # 7. Conclusiones
    st.header("Conclusiones")
    st.markdown("""
    ### Coomparación de Bibliotecas
    1. **Matplotlib** 
    * Biblioteca base para visualización
    * Mayor control sobre los detalles del gráfico
    * Curva de aprendizaje más pronunciada
    
    2. **Seaborn**
    * Construida sobre Matplotlib
    * Excelente para visualización de estadísticas
    * Estilos prdefinidos atractivos
    
    3. **Plotly**
    * Gráfico interactivos
    * Excelente para dashboards web
    * Integración perfecta con otras bibliotecas
    * Desarrollo rápido de prototipos                
                """)

    # Footer
    st.markdown("---")
    st.markdown("Desarrollado con Python y Streamlit")


except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    st.error("Por favor, verifica que los archivos existan en la carpeta 'data' y tengan el formato correcto.") 




    #2.35.30