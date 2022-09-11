import streamlit as st
import requests
import datetime

st.markdown("""#TaxiFareWebsite""")

pickup_date = st.date_input("Enter Date")
pickup_time = st.time_input("Enter time 24hr:mm")
pickup_datetime = str(pickup_date) + " " + str(pickup_time) #2012-10-06 12:10:20
pickup_longitude = st.number_input("Enter Pickup longtitude", format="%.7f")
pickup_latitude = st.number_input("Enter Pickup latitude", format="%.7f")
dropoff_longitude = st.number_input("Enter Drop off longtitude",format="%.7f")
dropoff_latitude = st.number_input("Enter Drop off latitude",format="%.7f")
passenger_count = st.number_input("Number of Passengers")

# st.write(pickup_datetime,pickup_longitude)
params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": int(passenger_count)
        }

print(params)
url = 'https://taxifare.lewagon.ai/predict?'
print('getting fare...')
response = requests.get(url, params=params).json()
print('responce',response)

st.write("fare",response['fare'])

"""
2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156
&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
"""
