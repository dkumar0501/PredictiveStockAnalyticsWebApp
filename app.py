import numpy as np    
import pandas as pd      
import matplotlib.pyplot as plt      
import yfinance as yf   
from keras.models import load_model   
import streamlit as st   
       
# Set date range   
start = '2010-01-01'  
end = '2024-12-31'  
 
# Streamlit UI 
st.title('Stock Trend Prediction')  

user_input = st.text_input('Enter Stock Ticker', 'TSLA')

# Download data
df = yf.download(user_input, start=start, end=end)

# Show data stats
st.subheader('Data from 2010 - 2024')
st.write(df.describe())

# Visualizations 
st.subheader('Closing Price Vs Time Graph')
fig = plt.figure(figsize=(12, 6))
plt.plot(df['Close'])  
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title(f"Stock Closing Price of {user_input}")
st.pyplot(fig) 

st.subheader('Closing Price Vs Time Graph with 100MA & 200MA')
ma100 = df['Close'].rolling(100).mean()  
ma200 = df['Close'].rolling(200).mean()  
fig2 = plt.figure(figsize=(12, 6))
plt.plot(ma100, label="100MA")
plt.plot(ma200, label="200MA")
plt.plot(df['Close'], label="Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.title(f"{user_input} with Moving Averages")
st.pyplot(fig2)  


# Splitting data into training and testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

print(data_training.shape)
print(data_testing.shape)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)


#load my model
model = load_model('my_model.keras')

#testing part

past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])
    
x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)
scaler = scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

#final
st.subheader('Predication vs riginal')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Prize')
plt.plot(y_predicted, 'r', label = 'Predicted Prize')
plt.xlabel('Time')
plt.xlabel('Price')
plt.legend()
st.pyplot(fig2)
