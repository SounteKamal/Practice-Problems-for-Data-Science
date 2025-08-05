# GrowwX-Level Stock Price Predictor App
# Filename: growwx_stock_predictor.py

import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import datetime
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from ta.momentum import RSIIndicator

# ----------------------------- App Title -----------------------------
st.set_page_config(page_title="GrowwX Stock Predictor", layout="wide")
st.title("📈 GrowwX Stock Market Predictor")
st.markdown("Predict Tomorrow's Stock Price with Advanced LSTM + Buy/Sell Signals")

# ----------------------------- Sidebar Inputs -----------------------------
st.sidebar.header("User Input")
stock = st.sidebar.text_input("Enter Stock Symbol (e.g. RELIANCE.NS):", "RELIANCE.NS")
interval = st.sidebar.selectbox("Select Time Range:", ["1 Week", "1 Month", "6 Months", "Max"], index=2)

# ----------------------------- Date Handling -----------------------------
end = datetime.date.today()
if interval == "1 Week":
    start = end - datetime.timedelta(days=7)
elif interval == "1 Month":
    start = end - datetime.timedelta(days=30)
elif interval == "6 Months":
    start = end - datetime.timedelta(days=180)
else:
    start = datetime.date(2010, 1, 1)

# ----------------------------- Data Download -----------------------------
st.subheader(f"Showing data for: {stock}")
data_load_state = st.text("Fetching data...")
data = yf.download(stock, start=start, end=end)
data.dropna(inplace=True)
data_load_state.text("✅ Data loaded successfully!")

# ----------------------------- Feature Engineering -----------------------------
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()
data['RSI'] = RSIIndicator(data['Close'].squeeze()).rsi()


# ----------------------------- Plot Candlestick -----------------------------
st.subheader("📊 Stock Price Chart")
fig = go.Figure()
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'], high=data['High'],
                             low=data['Low'], close=data['Close'],
                             name='Candlestick'))
fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1), name='MA20'))
fig.add_trace(go.Scatter(x=data.index, y=data['MA50'], line=dict(color='orange', width=1), name='MA50'))
fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

# ----------------------------- Prepare Data for LSTM -----------------------------
scaler = MinMaxScaler(feature_range=(0, 1))
close_data = data['Close'].values.reshape(-1, 1)
scaled_data = scaler.fit_transform(close_data)

lookback = 60
X, y = [], []
for i in range(lookback, len(scaled_data)):
    X.append(scaled_data[i-lookback:i, 0])
    y.append(scaled_data[i, 0])

X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# ----------------------------- LSTM Model -----------------------------
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, y, batch_size=1, epochs=1, verbose=0)

# ----------------------------- Predict Tomorrow -----------------------------
last_60_days = scaled_data[-60:]
X_test = []
X_test.append(last_60_days[:, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_price = model.predict(np.array(X_test[-1:]))[0][0]
predicted_price = scaler.inverse_transform([[predicted_price]])[0][0]


# ----------------------------- Show Prediction -----------------------------
st.subheader("📍 Tomorrow's Predicted Price")
st.success(f"Predicted Close Price: ₹ {predicted_price:.2f}")

# ----------------------------- Buy/Sell Signal -----------------------------
st.subheader("🟢 Buy / 🔴 Sell / ⚪ Hold Signal")
latest_close = data['Close'].iloc[-1:]
# Ensure both are scalar values (floats)
predicted_price_value = float(predicted_price.item())
latest_close_value = float(latest_close.iloc[0])

# Now the condition will work perfectly
if predicted_price_value > latest_close_value * 1.01:
    st.info("📈 Suggestion: BUY (Expected price increase)")
elif predicted_price_value < latest_close_value * 0.99:
    st.info("📉 Suggestion: SELL (Expected price drop)")
else:
    st.info("🤝 Suggestion: HOLD (Minor change expected)")

# ----------------------------- Download Option -----------------------------
st.download_button(label="Download Data as CSV", data=data.to_csv().encode(), file_name=f'{stock}_data.csv', mime='text/csv')
