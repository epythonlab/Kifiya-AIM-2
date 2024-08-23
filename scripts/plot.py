# scripts/plot.py

# import the ploting libraries
import seaborn as sns
import matplotlib.pyplot as plt

def plot_time_series(df, title):
    """
    Plots time series data for specified columns using Seaborn.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the time series data.
    - columns (list): List of column names to plot.
    - title (str): Title for the plot.
    """
    # Plotting the line graphs for GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(14, 8))
    # Plot GHI
    sns.lineplot(data=df, x=df.index, y='GHI', label='GHI', color='blue')
    # Plot DNI
    sns.lineplot(data=df, x=df.index, y='DNI', label='DNI', color='orange')
    # Plot DHI
    sns.lineplot(data=df, x=df.index, y='DHI', label='DHI', color='green')
    # Plot Tamb
    sns.lineplot(data=df, x=df.index, y='Tamb', label='Tamb (°C)', color='red')

    # Customize the plot
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.gcf().autofmt_xdate()
    # Display the plot
    plt.show()

def plot_cleaning_impact(df, sensor_columns, title):
    plt.figure(figsize=(12, 8))
    for column in sensor_columns:
        sns.lineplot(data=df, x='Timestamp', y=column, hue='Cleaning', marker=None)
    plt.xlabel('Time')
    plt.ylabel('Sensor Reading')
    plt.title(title)
    plt.legend(title='Cleaning Event')
    plt.grid(True)
    plt.gcf().autofmt_xdate()
    plt.show()


