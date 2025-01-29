import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Set Streamlit page configuration
st.set_page_config(page_title="Rice Classification", page_icon="🌾", layout="wide")

# Custom HTML & CSS for styling
st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px;}
        h1 {color: #4CAF50; text-align: center;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 20px; width: 100%;}
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown("<h1>🌾 Rice Classification using KNN</h1>", unsafe_allow_html=True)

# Upload file section
uploaded_file = st.file_uploader("Upload an Excel File", type=["xlsx"])

if uploaded_file:
    # Read the uploaded data
    data = pd.read_excel(uploaded_file)

    # Display raw data if checkbox is checked
    if st.checkbox("Show Raw Data"):
        st.write(data.head())

    # Handle missing and duplicate values
    st.write("🧐 Checking for missing & duplicate values...")
    st.write(f"Missing Values:\n{data.isnull().sum()}")
    st.write(f"Duplicate Rows: {data.duplicated().sum()}")

    # Separate Features and Target
    x = data.drop(['Class'], axis=1)
    y = data['Class']

    # Display target value counts
    st.write(f"Target value counts:\n{y.value_counts()}")

    # Boxplot for features
    st.write("📊 Boxplot for Features")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=x, ax=ax)
    st.pyplot(fig)

    # Remove Outliers using IQR
    Q3 = x.quantile(0.75)
    Q1 = x.quantile(0.25)
    IQR = Q3 - Q1
    x_filtered = x[~((x < (Q1 - 1.5 * IQR)) | (x > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Align y with filtered x
    y_filtered = y[x_filtered.index]

    # Scale the data
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(x_filtered)

    # Train-Test Split
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_filtered, random_state=0, test_size=0.2, stratify=y_filtered)

    # Train KNN Model
    knn = KNeighborsClassifier(n_neighbors=97)
    knn.fit(x_train, y_train)

    # Make predictions and calculate accuracy
    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_pred, y_test)
    st.write(f"🎯 Model Accuracy: {accuracy:.2f}")

    # Save the model and scaler
    joblib.dump(knn, 'Rice_Cammeo_Osmancik.pkl')
    joblib.dump(scaler, 'Rice_Cammeo_Osmancik_scaler.pkl')

    # Plot error rate for different K values
    error = []
    for i in range(1, 150):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        error.append(np.mean(y_pred != y_test))

    st.write("📈 Error Rate for Different K values")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, 150), error, color='red', marker='o')
    ax.set_xlabel('K Value')
    ax.set_ylabel('Error Rate')
    ax.set_title('KNN Error Rate Analysis')
    st.pyplot(fig)

    # Load model and scaler for future use
    knn_model = joblib.load('Rice_Cammeo_Osmancik.pkl')
    scaler_model = joblib.load('Rice_Cammeo_Osmancik_scaler.pkl')

    # Input new data for prediction
    st.write("🔮 Make Predictions")
    input_data = []
    for column in x.columns:
        value = st.number_input(f"Enter value for {column}", min_value=float(x[column].min()), max_value=float(x[column].max()), step=0.1)
        input_data.append(value)

    if st.button('Predict'):
        # Preprocess the input data
        input_data_scaled = scaler_model.transform([input_data])

        # Make prediction
        prediction = knn_model.predict(input_data_scaled)
        st.write(f"Predicted Class: {prediction[0]}")

# Footer with animation
st.markdown("""
    <script>
        setTimeout(() => {
            alert("🚀 Welcome to Rice Classification App!");
        }, 1000);
    </script>
""", unsafe_allow_html=True)
