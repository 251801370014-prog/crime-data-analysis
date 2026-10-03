import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Crime Data Analysis",
    page_icon="🚨",
    layout="wide"
)

# Title
st.title("🚨 Crime Data Analysis and Visualization")
st.write("Analyze and visualize crime data using Python.")

st.divider()

# Upload CSV
st.subheader("📂 Upload Crime Dataset")

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # Dataset preview
    st.subheader("📋 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    # Basic information
    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", len(df))

    with col2:
        st.metric("Total Columns", len(df.columns))

    with col3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    st.divider()

    # Column selection
    columns = df.columns.tolist()

    st.subheader("📈 Visualization")

    # Select columns
    x_column = st.selectbox(
        "Select a column for analysis",
        columns
    )

    # Count values
    value_counts = df[x_column].value_counts().head(15)

    if len(value_counts) > 0:

        chart_data = pd.DataFrame({
            x_column: value_counts.index.astype(str),
            "Count": value_counts.values
        })

        fig = px.bar(
            chart_data,
            x=x_column,
            y="Count",
            title=f"Crime Distribution by {x_column}"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Numeric columns
    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    if numeric_columns:

        st.subheader("📊 Numerical Data Analysis")

        selected_numeric = st.selectbox(
            "Select numerical column",
            numeric_columns
        )

        fig2 = px.histogram(
            df,
            x=selected_numeric,
            title=f"Distribution of {selected_numeric}"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # Statistics
    st.subheader("📌 Statistical Summary")

    st.dataframe(
        df.describe(include="all").T,
        use_container_width=True
    )

else:

    st.info("👆 Please upload your crime_data.csv file to start analysis.")

    st.subheader("🔍 Project Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("📊 **Data Analysis**")
        st.write("Analyze crime records and statistics.")

    with col2:
        st.write("📈 **Data Visualization**")
        st.write("Create interactive charts and graphs.")

    with col3:
        st.write("📋 **Dataset Summary**")
        st.write("View records, columns and missing values.")

st.divider()

st.caption("Crime Data Analysis Project | Python + Pandas + Plotly + Streamlit")