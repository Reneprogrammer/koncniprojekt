import streamlit as st
from geopy.geocoders import Nominatim
import folium

# Create a function to geocode the location
def geocode_location(location_text):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(location_text)
    return (location.latitude, location.longitude)

# Create the Streamlit app
def main():
    st.title("Text Location Mapper")

    # Create a text input for the user to enter the location
    location_text = st.text_input("Enter the location text:")

    # Check if the user has entered a location
    if location_text:
        # Geocode the location
        latitude, longitude = geocode_location(location_text)

        # Create a map using Folium and pinpoint the location
        my_map = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=location_text).add_to(my_map)

        # Display the map in the Streamlit app
        st.write("Location:", location_text)
        st.write("Latitude:", latitude)
        st.write("Longitude:", longitude)
        st.write("Map:")
        st.write(my_map)

# Run the Streamlit app
if __name__ == "__main__":
    main()
