import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# Streamlit App Title
st.title("Smart Parking Tracker")

# Function to fetch geolocation data using IP
def get_location_by_ip():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data['lat'], data['lon']
    except Exception as e:
        st.error(f"Failed to fetch location: {e}")
        return 0.0, 0.0

# Section: Get Current Location
if st.button("Get Current Location"):
    st.write("Fetching location...")
    latitude, longitude = get_location_by_ip()
    if latitude and longitude:
        st.success(f"Current Location: Latitude {latitude}, Longitude {longitude}")
    else:
        st.error("Unable to fetch location. Using default coordinates.")
        latitude, longitude = 0.0, 0.0

# Section: Display Location on Map
st.write("### Map View of Your Location")
m = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker([latitude, longitude], popup="Your Location").add_to(m)
st_folium(m, width=700, height=500)
