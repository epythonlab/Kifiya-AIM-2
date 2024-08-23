# scripts/plot.py

# import the ploting libraries
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

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


def correlation_heatmap(df, columns, method="heatmap", title="Correlation Heatmap"):
    """
    Visualize the correlations between solar radiation components (GHI, DNI, DHI) 
    and temperature measures (TModA, TModB) using heatmaps or pair plots.
        
    Parameters:
    - df: DataFrame containing the data.
    - method: Visualization method ("heatmap" or "pairplot").
    - title: Title of the heatmap.
    """

    if method == "heatmap":
        corr = df[columns].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
        plt.title(title)
        plt.show()
    
    elif method == "pairplot":
        sns.pairplot(df[columns], corner=True)
        plt.suptitle(title)
        plt.show()
    
    else:
        raise ValueError("Method must be 'heatmap' or 'pairplot'")
    

def scatter_matrix(df, columns, title="Scatter Matrix"):
    """
    Generate a scatter matrix to visualize relationships between the specified variables.
    
    Parameters:
    - df: DataFrame containing the data.
    - columns: List of column names to include in the scatter matrix.
    - title: Title of the scatter matrix.
    """
    sns.pairplot(df[columns], corner=True)
    plt.suptitle(title)
    plt.show()


def plot_wind_polar(df, ws_column, wd_column, title):
    """
    Plot a polar plot to analyze wind speed and direction distribution.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing wind data.
    ws_column (str): The name of the column for wind speed.
    wd_column (str): The name of the column for wind direction.
    
    Returns:
    None: Displays a polar plot showing wind speed and direction distribution.
    
    Example:
    >>> plot_wind_polar(df, 'WS', 'WD')
    """
    # Convert wind direction from degrees to radians
    wd_rad = np.deg2rad(df[wd_column])
    
    # Create polar plot
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2.0)
    
    # Plot the wind speed and direction
    scatter = ax.scatter(wd_rad, df[ws_column], alpha=0.75, cmap='viridis')
    
    # Add color bar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label(ws_column)
    
    plt.title(title)
    plt.show()

def temperature_analysis(df, columns, plot_type='heatmap', title="Togo"):
    """
    Analyze the relationship between relative humidity (RH) and temperature readings (Tamb) 
    and solar radiation components (GHI, DNI, DHI).

    Parameters:
    - df: DataFrame containing the dataset.
    - plot_type: Type of plot to generate ('heatmap' or 'scatter').
    - columns: List of columns to include in the analysis (default includes RH, Tamb, GHI, DNI, DHI).

    Returns:
    - A correlation matrix and visualizations of the relationships between RH, Tamb, and solar radiation components.
    """

    # Correlation analysis
    correlation_matrix = df[columns].corr()

    if plot_type == 'heatmap':
        # Heatmap visualization
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap of '+title )
        plt.show()
    elif plot_type == 'scatter':
        # Scatter plot visualization
        sns.pairplot(df[columns], kind='reg', diag_kind='kde')
        plt.suptitle('Scatter Plot Matrix of Temperature, Solar Radiation, and Humidity', y=1.02)
        plt.show()
    else:
        raise ValueError("Invalid plot_type. Choose 'heatmap' or 'scatter'.")

def plot_histograms(dataframes, variables, region_names, bins=30):
    """
    Plot histograms for the specified variables across multiple regions.

    Parameters:
    -----------
    dataframes : list of pd.DataFrame
        List of DataFrames, each containing data for a specific region.
    variables : list of str
        List of variable names (columns) to plot histograms for.
    region_names : list of str
        List of names of the regions corresponding to each DataFrame.
    bins : int, optional
        Number of bins for the histograms. Default is 30.

    Returns:
    --------
    None
    """
    for var in variables:
        plt.figure(figsize=(15, 8))
        
        for df, region in zip(dataframes, region_names):
            sns.histplot(df[var], bins=bins, kde=True, label=region, element="step")
        
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.legend(title='Region')
        plt.grid(True)
        plt.show()
   