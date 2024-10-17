import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingRegressor      

model = joblib.load('xg_boost.pkl')
st.title('Temperature Prediction(max)')


sunrise = st.number_input('Sunrise in 24hours', min_value=0.0, max_value=24.0, value=10.0)
sunset = st.number_input('Sunset in 24hours', min_value=0.0, max_value=24.0, value=10.0)
sun_hours=sunset-sunrise
humidity = st.slider('Humidity (%)', min_value=0, max_value=100, value=60)
precipitation = st.slider('Precipitation', min_value=0, max_value=13, value=2)
pressure = st.slider('pressure', min_value=900, max_value=1000, value=970)
uv_index = st.slider('UV_index',min_value=4,max_value=10, value=5)
dew_point = st.number_input('Dew Point (C)', value=20)


input_data = pd.DataFrame({
        'sun_hours': [sun_hours],
        'uvIndex': [uv_index],
        'DewPointC': [dew_point],
        'precipMM': [precipitation],
        'humidity': [humidity],
        'pressure': [pressure]
    },index=[0])

if st.button('Predict'):    
    prediction = model.predict(input_data)
    st.success(f'Predicted Max Temperature: {prediction[0]:.2f} °C')
    
