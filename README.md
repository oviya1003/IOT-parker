# Smart Parking Tracker
![WhatsApp Image 2025-02-13 at 22 03 17](https://github.com/user-attachments/assets/894fc264-7b7e-4b75-8e96-a046cfc80366)



## Project Overview

This project is a Smart Parking Tracker that uses GPS and IoT integration to provide real-time parking availability and user location tracking. It is built using Streamlit, Folium, and IoT connectivity.

------------



## Features

- **Streamlit Web App (`app.py` & `main.py`)**
    - Fetches user location via IP-based geolocation or GPS module.
    - Displays real-time location on an interactive map.
    - Retrieves real-time parking availability.
    - Sends location and parking data to an IoT system.

- **IoT Integration (`if st.button(Send Location to IoT).txt`)**
    - Sends location coordinates to an IoT endpoint for further processing.
    - Handles API responses and errors effectively.

- UI Styling (`styles.css`)
   - Responsive and visually appealing frontend.
   - Background customization and interactive map display.

------------



## Installation

1. Clone the repository:

```bash
git clone <repo_link>
cd project_directory
```

2 . Install dependencies:

`pip install streamlit folium requests pyserial`

3 . Ensure a valid IoT Endpoint URL is available for data transmission.


------------


## Usage

- Run the Streamlit App:
`streamlit run main.py`

- Test GPS Functionality:
`python main.py`

------------



## Data Flow

1. User Location Retrieval:
    - By IP-based API (`app.py`).
    - By GPS module via serial connection (`main.py`).

2. Display on Map:
     - Uses `folium` to plot the location dynamically.

3. Send to IoT:
     - Posts data to an IoT server via API (`if st.button(Send Location to IoT).txt`).


------------



## Future Enhancements

- Improve location accuracy using mobile GPS.
- Implement user authentication for secured tracking.
- Expand IoT functionality for real-time parking slot reservations.
