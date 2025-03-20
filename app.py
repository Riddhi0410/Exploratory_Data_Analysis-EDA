import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from graph import *


st.set_page_config(layout='wide')

df = pd.read_csv("SampleSuperstore.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y", errors='coerce')
years = sorted(df['Order Date'].dt.year.dropna().unique())


def home():
    st.title("🏠 Welcome to the Dashboard")
    st.markdown("<br>", unsafe_allow_html=True)

    st.write(" ### This application provides a comprehensive analysis of sales data from a superstore.")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
    """
    <p style="font-size:20px; color:#4CAF50;">
        Select an option from the sidebar to get started. 
        Each option will provide you with visualizations and insights based on the sales data.
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("### DATASET")
    st.dataframe(df, height=550)

st.markdown(
    """
    <style>
    .st-emotion-cache-a6qe2i {
        padding: 0px 0rem 0rem !important;
    }
    [data-testid="stSidebar"] {
        background-color: black;
        border-radius: 0px !important; /* Removes border-radius from sidebar */
    }
    [data-testid="stSidebarContent"] {
        padding-top: 0px;
    }
    .css-1d391kg {  
        border-radius: 0px !important; /* Removes border-radius from the option menu container */
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Dictionary mapping menu options to functions
menu_options = {
    "HOME": home,
    "Sales by Category": category,
    "Sub Category": sub_category,
    "Top Customers": top_customers,
    "Region": region,
    "Top 10 state": top10_state,
    "Ship Duration": ship_duration,
    "Customer Segment": customer_segment,
    "Repeat Customer": repeat_customer,
    "Monthly Sales": lambda: monthly_sales(st.selectbox("SELECT YEAR", options=years))
}

menu_icons = [
    "house",  # Home
    "cart",  # Sales by Category
    "grid",  # Sub Category
    "people",  # Top Customers
    "globe",  # Region
    "map",  # Top 10 State
    "truck",  # Ship Duration
    "person-lines-fill",  # Customer Segment
    "person-check",  # Repeat Customer
    "calendar",  # Monthly Sales
]

with st.sidebar:

    st.image("logo2.png", use_container_width=True)

    # st.markdown("<br>", unsafe_allow_html=True)
    
    selected = option_menu("", list(menu_options.keys()), icons=menu_icons ,styles={
        "container": {"background-color": "black", "border-radius": "0px"},  # No border-radius on the menu container
        "icon": {"color": "white", "font-size": "20px"}, })
    

if selected : 
    menu_options[selected]() 
else:
    home()
