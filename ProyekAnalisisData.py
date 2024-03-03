import streamlit as st
import pandas as pd
import seaborn as sns

df_day = pd.read_csv('day.csv')

# Function to create bike rental demand by month visualization
def monthly_demand_chart():
    # Grouping data by 'mnth' (month) and aggregating the sum of 'cnt' (total rental bikes)
    monthly_demand = df_day.groupby('mnth')['cnt'].sum().reset_index()

    # Plotting the demand by month using Seaborn
    st.bar_chart(monthly_demand.set_index('mnth'))

# Function to create distribution of casual vs. registered users by weekday visualization
def user_distribution_chart():
    # Grouping data by 'weekday' and aggregating the sum of 'casual' and 'registered' counts
    user_distribution = df_day.groupby('weekday')[['casual', 'registered']].sum().reset_index()

    # Plotting the distribution using Seaborn
    st.bar_chart(user_distribution.set_index('weekday'))

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
