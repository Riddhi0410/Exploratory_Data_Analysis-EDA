import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

df = pd.read_csv("SampleSuperstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y", errors='coerce')
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y", errors='coerce')



def category():

    st.write("## 📊 TOTAL SALES BY CATEGORY")

    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis", ax=ax)

    ax.set_xlabel("Category")
    ax.set_ylabel("Total Sales")
    ax.grid(axis="y")
    
    st.pyplot(fig)

    with st.container():
        st.table(category_sales.to_frame())


def sub_category():

    st.write("## 📈 TOTAL SALES BY SUB CATEGORY")

    subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=subcategory_sales.index, y=subcategory_sales.values, palette="coolwarm", ax=ax)

    ax.set_xlabel("Sub-Category")
    ax.set_ylabel("Total Sales")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.grid(axis="y")

    st.pyplot(fig)

    with st.container():
        st.table(subcategory_sales.to_frame())


def region():

    st.write("## 🌍 TOTAL SALES BY REGION")
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

    fig,ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=region_sales.index, y=region_sales.values, palette="pastel", ax =ax)
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales")
    ax.grid(axis="y")

    st.pyplot(fig)

    with st.container():
        st.table(region_sales.to_frame())


def top10_state():

    st.write("## 🏅 TOP 10 STATES BY SALES")
    state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state_sales.index, y=state_sales.values, palette="magma", ax=ax)
    ax.set_xlabel("State")
    ax.set_ylabel("Total Sales")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.grid(axis="y")
    
    st.pyplot(fig)
    
    with st.container():
        st.table(state_sales.to_frame())


def ship_duration():

    st.write("## 🚛 AVERAGE SHIPPING DURATION BY SHIP MODE")

    df["Shipping Duration"] = (df["Ship Date"] - df["Order Date"]).dt.days
    shipping_mode_duration = df.groupby("Ship Mode")["Shipping Duration"].mean().sort_values()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=shipping_mode_duration.index, y=shipping_mode_duration.values, palette="Blues_r", ax =ax)
    
    ax.set_xlabel("Ship Mode")
    ax.set_ylabel("Average Shipping Time (Days)")
    ax.grid(axis="y")

    st.pyplot(fig)
    
    with st.container():
        st.table(shipping_mode_duration.to_frame())

   
def top_customers():

    st.write("## 🏆 TOP 10 CUSTOMERS BY TOTAL SALES")

    top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(x=top_customers.values, y=top_customers.index, palette="viridis")
    
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Customer Name")
    plt.grid(axis="x")
    
    st.pyplot(fig)
    
    with st.container():
        st.table(top_customers.to_frame())


def customer_segment():

    st.write("## 👥 TOTAL SALES BY CUSTOMER SEGMENT ")
    segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=segment_sales.index, y=segment_sales.values, palette="coolwarm", ax =ax)
    
    ax.set_xlabel("Customer Segment")
    ax.set_ylabel("Total Sales")
    plt.grid(axis="y")
    st.pyplot(fig)
    
    with st.container():
        st.table(segment_sales.to_frame())


def repeat_customer():

    customer_order_count = df.groupby("Customer Name").size().sort_values(ascending=False)
    repeat_customers = customer_order_count[customer_order_count > 1]
    
    st.write("## 🔄 DISTRIBUTION OF REPEAT CUSTOMER ORDERS")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(repeat_customers, bins=30, kde=True, color="purple", ax=ax)
    
    ax.set_xlabel("Number of Orders")
    ax.set_ylabel("Number of Customers")
    plt.grid(axis="y")

    st.pyplot(fig)


def monthly_sales(year):

        df_year = df[df["Order Date"].dt.year == year]

        monthly_sales = df_year.groupby(df_year["Order Date"].dt.month)["Sales"].sum()
        st.write(f"## 📅 MONTHLY SALES OF {year}")

        # Ensure all months are represented
        monthly_sales = monthly_sales.reindex(range(1, 13), fill_value=0)

        # Map numeric months to names
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthly_sales.index = month_names

        # Plot
        fig, ax = plt.subplots(figsize=(10, 5))
        monthly_sales.plot(marker="o", linestyle="-", color="b", ax=ax)
        
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.grid(True)

        # Display in Streamlit
        st.pyplot(fig)

        # Show sales data as a table
        st.table(monthly_sales.to_frame())