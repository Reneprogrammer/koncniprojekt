import streamlit as st
from PIL import Image
import pytesseract
import folium

# Function to extract text from image
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Function to display map with marker
def show_map(location):
    m = folium.Map(location=location, zoom_start=10)
    folium.Marker(location=location, popup='Text Location').add_to(m)
    return m

def main():
    st.title('Text Location Mapper')

    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        text = extract_text(image)
        st.write('Extracted Text:', text)

        if st.button('Map Text Location'):
            # For demonstration purposes, using a hardcoded location (latitude, longitude)
            # You can replace this with your logic to extract location from the text
            location = (40.7128, -74.0060)  # Example location (New York City)
            st.write('Location Coordinates:', location)
            st.write('Mapping Location on Global Map...')
            map_obj = show_map(location)
            st.write(map_obj._repr_html_(), unsafe_allow_html=True)

if __name__ == '__main__':
    main()
