import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Talking Rabbitt – Talk to Your Data",
    page_icon="🐰",
    layout="wide"
)

# Session states
if "df" not in st.session_state:
    st.session_state.df = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:

    st.title("🐰 Talking Rabbitt")

    st.markdown("""
Upload a dataset and ask questions in plain English.

Example questions:

Show revenue by region  
Show revenue by quarter  
Compare revenue by product
""")

# Main Title
st.title("🐰 Talking Rabbitt – Talk to Your Data")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

col1, col2 = st.columns(2)

# Load sample data
with col1:

    if st.button("Load Sample Sales Data"):

        if os.path.exists("sample_sales_data.csv"):

            df = pd.read_csv("sample_sales_data.csv")
            st.session_state.df = df
            st.success("Sample dataset loaded successfully")

        else:

            st.error("sample_sales_data.csv not found")

# Show dataset info
with col2:

    if st.session_state.df is not None:

        df = st.session_state.df
        st.info(f"Dataset Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# Handle upload
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.session_state.df = df
    st.success("Dataset uploaded successfully")

# If dataset loaded
if st.session_state.df is not None:

    df = st.session_state.df

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("💬 Ask Questions About Your Data")

    # Show chat history

    for i, msg in enumerate(st.session_state.chat_history):

        if msg["role"] == "user":

            st.markdown(f"**You:** {msg['content']}")

        else:

            st.markdown(f"**🐰 Rabbitt:** {msg['content']}")

            if msg["chart"] is not None:

                st.plotly_chart(
                    msg["chart"],
                    use_container_width=True,
                    key=f"chart_{i}"
                )

    question = st.text_input("Ask a question")

    col1, col2 = st.columns([1,4])

    with col1:
        ask_button = st.button("Ask")

    with col2:
        clear_button = st.button("Clear Chat")

    if clear_button:

        st.session_state.chat_history = []
        st.rerun()

    if ask_button and question:

        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        answer = ""
        chart = None

        q = question.lower()

        try:

            # REGION ANALYSIS
            if "region" in q and "revenue" in q:

                result = df.groupby("Region")["Revenue"].sum()

                fig = px.bar(
                    x=result.index,
                    y=result.values,
                    title="Revenue by Region",
                    labels={"x": "Region", "y": "Revenue"}
                )

                answer = "Here is the revenue comparison by region."
                chart = fig

            # QUARTER ANALYSIS
            elif "quarter" in q:

                result = df.groupby("Quarter")["Revenue"].sum()

                fig = px.line(
                    x=result.index,
                    y=result.values,
                    title="Revenue by Quarter",
                    labels={"x": "Quarter", "y": "Revenue"},
                    markers=True
                )

                answer = "Here is the revenue trend by quarter."
                chart = fig

            # PRODUCT ANALYSIS
            elif "product" in q:

                result = df.groupby("Product")["Revenue"].sum()

                fig = px.bar(
                    x=result.index,
                    y=result.values,
                    title="Revenue by Product",
                    labels={"x": "Product", "y": "Revenue"}
                )

                answer = "Here is the product revenue comparison."
                chart = fig

            else:

                answer = "Try asking about Region, Quarter or Product revenue."

        except Exception as e:

            answer = f"Error analyzing data: {str(e)}"

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer,
            "chart": chart
        })

        st.rerun()

else:

    st.info("Upload a CSV dataset or load sample data to start.")

st.markdown("---")
st.markdown("🐰 Talking Rabbitt | Data Conversation Demo")