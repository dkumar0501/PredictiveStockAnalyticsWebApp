# Predictive Stock Analytics Web App 
 
## Overview 
 
The Predictive Stock Analytics Web App is a machine learning-powered platform designed to forecast future stock trends based on historical market data. Built with Keras and integrated into a user-friendly Streamlit interface, the app provides real-time visual insights and predictions to assist users in making informed trading decisions.
 
---   
   
## Technologies Used   
  
- Python 3.13.3   
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

1. **Data Input**: User selects a stock and time frame; the app fetches historical data via yFinance.

2. **Preprocessing**: The raw data is scaled using MinMaxScaler and reshaped to fit the LSTM input format.

3. **Model Prediction**: A pre-trained LSTM model (saved using Keras) processes the data to predict future stock prices.

4. **Visualization**: The app displays historical and predicted stock prices using Plotly and Matplotlib charts for easy comparison.

5. **User Interaction**: All functionalities are available through a clean Streamlit web interface.

## Project Working Screenshots

![Screenshot 2025-06-29 233131](https://github.com/user-attachments/assets/5ca55030-636d-4d76-ac46-2a5ce9c19c94)

![Screenshot 2025-06-29 233827](https://github.com/user-attachments/assets/4634a39e-9372-4a5a-9992-6935cdb98d13)

![Screenshot 2025-06-29 232740](https://github.com/user-attachments/assets/b9bbcc44-31b9-4d02-beb8-7de223eb0d9b)

![Screenshot 2025-06-29 232754](https://github.com/user-attachments/assets/ace890dd-bc6e-4fa8-9829-d084872911a1)

![Screenshot 2025-06-29 232806](https://github.com/user-attachments/assets/95891bea-e28a-4407-a9fb-8f5c63fe8983)

--- 
## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/predictive-stock-analytics.git
cd predictive-stock-analytics
pip install -r requirements.txt
