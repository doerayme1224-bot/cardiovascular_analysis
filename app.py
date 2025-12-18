# YOUR APP HERE!
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = "Cardiovascular Disease Data Exploration")

page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis"])

# Load dataset
df = pd.read_csv('data/heart.csv')

# Home Page
if page == "Home":
    st.title("Cardiovascular Disease Dataset")
    st.subheader("Welcome to my Analysis of the Cardiovascular Disease Dataset")
    st.write("""
        This app provides an interactive platform to explore the heart dataset. 
        You can visualize the distribution of data, and explore relationships between features.
        Use the sidebar to navigate through the sections.
    """)


# Data Overview
elif page == "Data Overview":
    st.title("Data Overview")

    st.subheader("About the Data")
    st.write("""
        The Cardiovascular Disease dataset is a dataset that I found interesting for my analysis because heart disease 
        is somewhat prevelant in my family. It contains 14 attributes and 1025 instances relating to conditions of the heart.
        Each patient can be put into two categories, ones that didn't have heart disease and ones that did.
    """)

    # Dataset Display
    st.subheader("Quick Glance at the Data")
    if st.checkbox("Show DataFrame"):
        st.dataframe(df)
    

    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")


# Exploratory Data Analysis (EDA)
elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect("Visualization Options", ['Histograms','Scatterplots', 'Count Plots'])

    obj_cols = df.columns.to_list(df['target'])
    num_cols = df.columns.to_list(df.drop('target', axis = 1))

    if 'Histograms' in eda_type:
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for the histogram:", num_cols)
        if h_selected_col:
            chart_title = f"Distribution of {h_selected_col.title().replace('_', ' ')}"
            if st.checkbox("Show by Presence of Heart Disease"):
                st.plotly_chart(px.histogram(df, x=h_selected_col, color='target', title=chart_title, barmode='overlay'))
            else:
                st.plotly_chart(px.histogram(df, x=h_selected_col, title=chart_title))

    if 'Scatterplots' in eda_type:
        st.subheader("Scatterplots - Visualizing Relationships")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols)
        if selected_col_x and selected_col_y:
            chart_title = f"{selected_col_x.title().replace('_', ' ')} vs. {selected_col_y.title().replace('_', ' ')}"
            st.plotly_chart(px.scatter(df, x=selected_col_x, y=selected_col_y, color='target', title=chart_title))

    if 'Count Plots' in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox("Select a categorical variable:", obj_cols)
        if selected_col:
            chart_title = f'Distribution of {selected_col.title()}'
            st.plotly_chart(px.histogram(df, x=selected_col, color='species', title=chart_title))
