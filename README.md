# Predictive Stock Analytics Web App

## Overview

The Predictive Stock Analytics Web App is a machine learning-powered platform designed to forecast future stock trends based on historical market data. Built with Keras and integrated into a user-friendly Streamlit interface, the app provides real-time visual insights and predictions to assist users in making informed trading decisions.

---

## Technologies Used

- Python 3.x  
- Keras (with TensorFlow backend)  
- Streamlit  
- Pandas, NumPy  
- Matplotlib, Plotly  
- yFinance (for stock data retrieval)  
- Scikit-learn  

---

## Key Features

- Stock trend forecasting using LSTM (Long Short-Term Memory) deep learning models  
- Real-time fetching of historical stock data via yFinance  
- Interactive visualizations of stock trends  
- Simple and intuitive user interface for non-technical users  
- Modular design for scalability and further model enhancement  

---

## How It Works

1. **Data Input**:  
   The user selects a stock ticker (e.g., AAPL, TSLA) and time frame. The app retrieves historical stock price data using the yFinance API.

2. **Preprocessing**:  
   The raw data is scaled using MinMaxScaler and reshaped to fit the LSTM input format.

3. **Model Prediction**:  
   A pre-trained LSTM model (saved using Keras) processes the data to predict future stock prices.

4. **Visualization**:  
   The app displays historical and predicted stock prices using Plotly and Matplotlib charts for easy comparison.

5. **User Interaction**:  
   All functionalities are available through a clean Streamlit web interface.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/predictive-stock-analytics.git
cd predictive-stock-analytics
pip install -r requirements.txt
