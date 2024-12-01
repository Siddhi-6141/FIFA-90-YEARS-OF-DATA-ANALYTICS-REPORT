
import streamlit as st

# Set the title of the app
st.title("Simple Streamlit Web Application with Sidebar")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the menu below to navigate:")

# Sidebar options
page = st.sidebar.radio("Go to", ["Home", "Data", "Settings", "About"])

# Display content based on the selected page
if page == "Home":
    st.header("Welcome to the Home Page!")
    st.write("This is the home page of your Streamlit app.")
elif page == "Data":
    st.header("Data Page")
    st.write("Here you could display data, charts, or any other data-related content.")
elif page == "Settings":
    st.header("Settings Page")
    st.write("This is where settings can be adjusted.")
elif page == "About":
    st.header("About Page")
    st.write("This app is created using Streamlit. It's a simple template with a sidebar navigation feature.")

# Footer
st.write("---")
st.write("Streamlit Web App Example")

