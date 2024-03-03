import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_day = pd.read_csv('day.csv')

# Function to create bike rental demand by month visualization
def monthly_demand_chart():
    # Grouping data by 'mnth' (month) and aggregating the sum of 'cnt' (total rental bikes)
    monthly_demand = df_day.groupby('mnth')['cnt'].sum().reset_index()

    # Plotting the demand by month using Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='mnth', y='cnt', data=monthly_demand, palette='viridis', ax=ax)

    plt.title('Bike Rental Demand by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Rental Bikes')
    st.pyplot(fig)

# Function to create distribution of casual vs. registered users by weekday visualization
def user_distribution_chart():
    # Grouping data by 'weekday' and aggregating the sum of 'casual' and 'registered' counts
    user_distribution = df_day.groupby('weekday')[['casual', 'registered']].sum().reset_index()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.barplot(x='weekday', y='casual', data=user_distribution, color='blue', ax=axes[0])
    axes[0].set_title('Distribution of Casual Users by Weekday')
    axes[0].set_xlabel('Weekday')
    axes[0].set_ylabel('Casual User Count')

    sns.barplot(x='weekday', y='registered', data=user_distribution, color='orange', ax=axes[1])
    axes[1].set_title('Distribution of Registered Users by Weekday')
    axes[1].set_xlabel('Weekday')
    axes[1].set_ylabel('Registered User Count')

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit App
def main():
    st.title('Bike Sharing Data Dashboard')

    # Sidebar for selecting visualizations
    st.sidebar.title('Select Visualization')
    selected_chart = st.sidebar.selectbox('Choose a visualization:', ['Monthly Demand', 'User Distribution'])

    # Display selected visualization
    if selected_chart == 'Monthly Demand':
        monthly_demand_chart()
    elif selected_chart == 'User Distribution':
        user_distribution_chart()

if __name__ == '__main__':
    main()