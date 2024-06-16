import streamlit as st
import folium
from streamlit_folium import folium_static
import os

# Page 1: Funnews Home Page
def home_page():
    st.title("Funnews")
    st.markdown("## Global Issues, Gamified!")
    
    image_path = "global_map_image.jpg"
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True)
    else:
        st.error(f"Image not found at path: {image_path}")

# Page 2: Interactive Global Map
def interactive_map(option):
    st.title("Interactive Global Map")
    if option == "Peaceful Diplomat":
        conflicts = {
            "Ukraine": [48.3794, 31.1656],
            "Gaza": [31.5, 34.47],
            "South Sudan": [6.877, 31.307],
            "Yemen": [15.5527, 48.5164]
        }
    elif option == "Green Activist":
        conflicts = {
            "Arctic": [66.33, -18.82],
            "New York": [40.7128, -74.0060],
            "Brazil Flood": [-14.2350, -51.9253]
        }
    elif option == "Welfare Economist":
        conflicts = {
            "Major Economic Event 1": [35.6895, 139.6917],
            "Major Economic Event 2": [51.5074, -0.1278]
        }

    map_center = [20, 0]
    folium_map = folium.Map(location=map_center, zoom_start=2)

    for location, coords in conflicts.items():
        folium.Marker(coords, popup=location, icon=folium.Icon(color="red")).add_to(folium_map)

    folium_static(folium_map)

# Page 3: Detailed View
def detailed_view(location):
    st.title(f"Details about {location}")
    # Add animation logic here (simplified example)
    if location == "Gaza":
        image_path = "images/animated_explosion.gif"
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.error(f"Image not found at path: {image_path}")
        st.markdown("### Current Events in Gaza")
        st.write("Details and news articles about the current situation in Gaza...")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Interactive Map", "Details"])

if page == "Home":
    home_page()
elif page == "Interactive Map":
    option = st.sidebar.selectbox("Choose your role:", ["Peaceful Diplomat", "Green Activist", "Welfare Economist"])
    interactive_map(option)
elif page == "Details":
    location = st.sidebar.selectbox("Choose a location:", ["Gaza", "Ukraine", "South Sudan", "Yemen"])
    detailed_view(location)

