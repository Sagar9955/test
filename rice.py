import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Title of the app
st.title("Rice Classification Using KNN")

# Upload dataset
data_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
if data_file:
    data = pd.read_excel(data_file)
    
    st.subheader("Dataset Preview")
    st.write(data.head())
    
    # Checking for missing and duplicate values
    st.subheader("Missing and Duplicate Values")
    st.write("Missing values per column:")
    st.write(data.isnull().sum())
    st.write(f"Total duplicate rows: {data.duplicated().sum()}")
    
    # Splitting features and target
    x = data.drop(['Class'], axis=1)
    y = data['Class']
    
    # Boxplot for feature distribution
    st.subheader("Feature Distribution (Boxplot)")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=x, ax=ax)
    st.pyplot(fig)
    
    # Normalization
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(x)
    
    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, random_state=0, test_size=0.2, stratify=y
    )
    
    # KNN Classification
    st.subheader("K-Nearest Neighbors (KNN) Model")
    k_value = st.slider("Select number of neighbors (k)", min_value=1, max_value=150, value=50)
    knn = KNeighborsClassifier(n_neighbors=k_value)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    acc = accuracy_score(y_pred, y_test)
    st.write(f"Model Accuracy with k={k_value}: {acc:.4f}")
    
    # Error rate analysis
    st.subheader("Error Rate vs. K Value")
    error = []
    for i in range(1, 150):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        error.append(np.mean(y_pred != y_test))
    
    fig, ax = plt.subplots()
    ax.plot(range(1, 150), error, marker='o')
    ax.set_xlabel("Number of Neighbors (k)")
    ax.set_ylabel("Error Rate")
    ax.set_title("K vs. Error Rate")
    st.pyplot(fig)
