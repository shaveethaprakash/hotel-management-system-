import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(
    page_title="Hotel Management System",
    page_icon="🏨",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏨 Hotel Dashboard")
menu = st.sidebar.radio(
    "Navigation",
    ["Book Room", "Booking History"]
)

st.title("Luxury Hotel Management System")

# ---------------- BOOK ROOM PAGE ----------------
if menu == "Book Room":

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Customer Details")
        name = st.text_input("Enter Customer Name")
        phone = st.text_input("Phone Number")

    with col2:
        st.subheader("Room Selection")
        room = st.selectbox(
            "Select Room Type",
            ["Standard Room", "Deluxe Room", "Suite", "Presidential Suite"]
        )

        days = st.number_input("Number of Days", min_value=1, max_value=30, value=1)

    st.markdown("---")

    if st.button("Book Room", use_container_width=True):

        response = requests.post(
            "http://127.0.0.1:8000/book",
            params={
                "name": name,
                "room": room
            }
        )

        st.success("✅ " + response.json()["message"])
        st.info(f"Booked for {days} day(s)")

    st.markdown("---")

    st.subheader("Hotel Highlights")
    col3, col4, col5 = st.columns(3)

    with col3:
        st.info("🛏️ Luxury Rooms")

    with col4:
        st.info("🍽️ Free Breakfast")

    with col5:
        st.info("📶 Free WiFi")

# ---------------- HISTORY PAGE ----------------
if menu == "Booking History":

    st.subheader("All Bookings")

    if os.path.exists("bookings.csv"):
        df = pd.read_csv("bookings.csv")

        st.dataframe(df, use_container_width=True)

        st.success(f"Total Bookings: {len(df)}")

    else:
        st.warning("No bookings found yet.")