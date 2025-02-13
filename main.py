import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import serial
import time

# Initialize serial port for hardware connection
serial_port = 'COM14'  # Update with the correct serial port
try:
    ser = serial.Serial(serial_port, 9600, timeout=1)
    st.success(f"Serial port {serial_port} connected successfully.")
except Exception as e:
    ser = None
    st.error(f"Error: Could not open serial port {serial_port}. Please check the connection.")

# Function to fetch GPS data with limited attempts
def get_gps_data(max_attempts=5):
    if ser:
        for attempt in range(max_attempts):
            try:
                # Read the data from the serial port
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                st.write(f"Raw GPS Data: {line}")  # Debugging line
                if line.startswith('$GPGGA'):
                    gps_data = line.split(',')
                    if gps_data[2] and gps_data[4]:  # Ensure valid latitude and longitude data
                        latitude = float(gps_data[2]) / 100  # Convert to decimal
                        longitude = float(gps_data[4]) / 100  # Convert to decimal
                        return latitude, longitude
                time.sleep(1)  # Wait before retrying
            except Exception as e:
                st.warning(f"Attempt {attempt + 1}: Error reading GPS data: {e}")
        st.error("Failed to fetch GPS data after multiple attempts.")
    else:
        st.error(f"Serial port {serial_port} is not available.")
    return None, None

# Function to fetch parking data (example)
def get_parking_data():
    occupied = 10  # Simulated data
    total = 20
    vacant = total - occupied
    return vacant, total

# Streamlit App Title
st.title("Smart Parking Tracker")

# Fetch GPS Location
st.write("### Fetching Location")
latitude, longitude = get_gps_data()
if latitude and longitude:
    st.write(f"Current Location: Latitude {latitude}, Longitude {longitude}")
else:
    st.write("Error fetching GPS data. Using default location for demonstration.")
    latitude, longitude = 13.394968, 77.728851  # Default coordinates
    st.warning("Using default coordinates (13.394968, 77.728851)")

# Display Location on Map
st.write("### Map View of Your Location")
m = folium.Map(location=[latitude, longitude], zoom_start=15)
folium.Marker([latitude, longitude], popup="Your Location").add_to(m)
st_folium(m, width=700, height=500)

# Fetch Parking Data
vacant, total = get_parking_data()
st.write(f"Vacant Parking Spaces: {vacant}/{total}")

# Send Data to IoT System
iot_endpoint = st.text_input("Enter IoT Endpoint URL:", "https://example-iot-cloud.com/api/coordinates")
if st.button("Send Location to IoT"):
    try:
        data = {"latitude": latitude, "longitude": longitude, "vacant_spaces": vacant}
        response = requests.post(iot_endpoint, json=data)
        if response.status_code == 200:
            st.success("Location sent successfully!")
            st.write("Response:", response.json())
        else:
            st.error(f"Failed to send location. Status code: {response.status_code}")
            st.write("Response:", response.text)
    except Exception as e:
        st.error("Error sending location to IoT system.")
        st.write(e)

