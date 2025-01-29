import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


st.set_page_config(page_title="Rice Classification", page_icon="🌾", layout="wide")


st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px;}
        h1 {color: #4CAF50; text-align: center;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 20px; width: 100%;}
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>🌾 Rice Classification using KNN</h1>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload an Excel File", type=["xlsx"])

if uploaded_file:
    data = pd.read_excel(uploaded_file)

 
    if st.checkbox("Show Raw Data"):
        st.write(data.head())

    
    st.write("🧐 Checking for missing & duplicate values...")
    st.write(f"Missing Values:\n{data.isnull().sum()}")
    st.write(f"Duplicate Rows: {data.duplicated().sum()}")

    x = data.drop(columns=['Class'])
    y = data['Class']

   
    # Handle Outliers
    rows_before = len(x)
    Q1 = x.quantile(0.25)
    Q3 = x.quantile(0.75)
    IQR = Q3 - Q1
    x = x[~((x < (Q1 - 1.5 * IQR)) | (x > (Q3 + 1.5 * IQR))).any(axis=1)]
    rows_after = len(x)
    st.write(f"Rows removed due to outliers: {rows_before - rows_after}")


   
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(x)

    
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, stratify=y, random_state=0)

   
    knn = KNeighborsClassifier(n_neighbors=50)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)

    
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"🎯 **Model Accuracy: {accuracy:.2f}**")

   
    error = []
    for i in range(1, 150):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        error.append(np.mean(y_pred != y_test))

   
    st.write("📈 **Error Rate for Different K values**")
    fig, ax = plt.subplots()
    ax.plot(range(1, 150), error, color='red', marker='o')
    ax.set_xlabel('K Value')
    ax.set_ylabel('Error Rate')
    ax.set_title('KNN Error Rate Analysis')
    st.pyplot(fig)


st.markdown("""
    <script>
        setTimeout(() => {
            alert("🚀 Welcome to Rice Classification App!");
        }, 1000);
    </script>
""", unsafe_allow_html=True)
