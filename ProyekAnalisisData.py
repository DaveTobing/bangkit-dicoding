import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_day = pd.read_csv('clean_day.csv')
df_hour = pd.read_csv('clean_hour.csv')

# Function to create distribution of casual vs. registered users by weekday visualization
def user_distribution_chart(data):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

    sns.barplot(x='weekday', y='casual', data=data, color='blue', ax=axes[0])
    axes[0].set_title('Distribution of Casual Users by Weekday')
    axes[0].set_xlabel('Weekday')
    axes[0].set_ylabel('Casual User Count')

    sns.barplot(x='weekday', y='registered', data=data, color='orange', ax=axes[1])
    axes[1].set_title('Distribution of Registered Users by Weekday')
    axes[1].set_xlabel('Weekday')
    axes[1].set_ylabel('Registered User Count')

    st.pyplot(fig)

# Function to create monthly demand visualization
def monthly_demand_chart(data, title, tipe):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=tipe, y='cnt', data=data, ax=ax)

    ax.set_title(title)
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Rental Bikes')

    st.pyplot(fig)

# Streamlit App
def main():
    st.title('Bike Sharing Data Dashboard')

    # Sidebar for selecting visualizations
    st.sidebar.title('Select Visualization')
    selected_chart = st.sidebar.selectbox('Choose a visualization:', ['User Distribution (Day)', 'User Distribution (Hour)', 'Monthly Demand (Day)', 'Hourly Demand (Hour)'])

    # Display selected visualization
    if selected_chart == 'User Distribution (Day)':
        user_distribution_chart(df_day.groupby('weekday')[['casual', 'registered']].sum().reset_index())
    elif selected_chart == 'User Distribution (Hour)':
        user_distribution_chart(df_hour.groupby('weekday')[['casual', 'registered']].sum().reset_index())
    elif selected_chart == 'Monthly Demand (Day)':
        monthly_demand_chart(df_day.groupby('mnth')['cnt'].sum().reset_index(), 'Bike Rental Demand by Month (Day)', 'mnth')
    elif selected_chart == 'Hourly Demand (Hour)':
        monthly_demand_chart(df_hour.groupby('hr')['cnt'].sum().reset_index(), 'Bike Rental Demand by Hour (Hour)', 'hr')

if __name__ == '__main__':
    main()