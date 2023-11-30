"""
The code that is provided analyzes a dataset pertaining to electric vehicles using exploratory data analysis, or EDA. The dataset is loaded first, then its structure is examined. To guarantee data completeness, null values are checked and rows with null values in the "County," "Legislative District," and "Vehicle Location" columns are eliminated.
The code then uses Matplotlib and Seaborn for comparison to create histograms for different properties. Postal code, model year, electric range, base MSRP, legislative district, DOL vehicle ID, and 2020 census tract are among the data sets for which histograms are made.
Understanding the distribution of each attribute within the dataset is made easier with the aid of these visualizations, which also shed light on possible trends and other features of the data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class EDA:
    """
    EDA class for handling Electric Vehicle Population Data visualization.

    Attributes:
    - df (pd.DataFrame): DataFrame containing Electric Vehicle Population Data.

    - __init__(): Constructor method to initialize the EDA object and load data from a CSV file."""

    def __init__(self):
        """
        Loads Electric Vehicle Population Data from a CSV file and initializes the df attribute.
        """
        self.df = pd.read_csv('https://raw.githubusercontent.com/saidadi/codingscripts/main/sai/Electric_Vehicle_Population_Data%20(3).csv')
        self.df.head()
        self.df.isnull().sum()
        self.df.info()
        self.df.describe()
        self.df.dropna(subset=['County'], inplace=True)
        self.df.dropna(subset=['Legislative District'], inplace=True)
        self.df.dropna(subset=['Vehicle Location'], inplace=True)
        self.df.isnull().sum()

    def postal_code_matplotlib(self):
        """- postal_code_matplotlib():
        Visualizes the distribution of Postal Code using Matplotlib.

        Returns:
        Displays a histogram of Postal Code.
"""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Postal Code'], bins=20, edgecolor='k')
        plt.title('Histogram of Postal Code (Matplotlib)')
        plt.xlabel('Postal Code')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def postal_code_seaborn(self):
        """-
         postal_code_seaborn():
        Visualizes the distribution of Postal Code using Seaborn.

        Returns:
        Displays a histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['Postal Code'], bins=20, kde=True)
        plt.title('Histogram of Postal Code (Seaborn)')
        plt.xlabel('Postal Code')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def Model_year_matplotlib(self):
        """- Model_year_matplotlib():
        Visualizes the distribution of Model Year using Matplotlib.

        Returns:
        Displays a histogram of Model Year."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Model Year'], bins=20, edgecolor='k')
        plt.title('Histogram of Model Year (Matplotlib)')
        plt.xlabel('Model Year')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def Model_year_seaborn(self):
        """- Model_year_seaborn():
        Visualizes the distribution of Model Year using Seaborn.

        Returns:
        Displays a histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['Model Year'], bins=20, kde=True)
        plt.title('Histogram of Model Year (Seaborn)')
        plt.xlabel('Model Year')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def Electric_range_matplotlib(self):
        """ - Electric_range_matplotlib():
        Visualizes the distribution of Electric Range using Matplotlib.

        Returns:
        Displays a histogram of Electric Range."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Electric Range'], bins=20, edgecolor='k')
        plt.title('Histogram of Electric Range (Matplotlib)')
        plt.xlabel('Electric Range')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def Electric_range_seaborn(self):
        """- Electric_range_seaborn():
        Visualizes the distribution of Electric Range using Seaborn.

        Returns:
        displays a histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['Electric Range'], bins=20, kde=True)
        plt.title('Histogram of Electric Range (Seaborn)')
        plt.xlabel('Electric Range')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def base_msrp_matplotlib(self):
        """- base_msrp_matplotlib():
                Visualizes the distribution of Base MSRP using Matplotlib.

                Returns:
                Displays a histogram of Base MSRP."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Base MSRP'], bins=20, edgecolor='k')
        plt.title('Histogram of Base MSRP (Matplotlib)')
        plt.xlabel('Base MSRP')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def base_msrp_seaborn(self):
        """- base_msrp_seaborn():
        Visualizes the distribution of Base MSRP using Seaborn.

        Returns:
        Displays a histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['Base MSRP'], bins=20, kde=True)
        plt.title('Histogram of Base MSRP (Seaborn)')
        plt.xlabel('Base MSRP')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def legislative_district_matplotlib(self):
        """- legislative_district_matplotlib():
        Visualizes the distribution of Legislative District using Matplotlib.

        Returns:
        Displays a histogram of Legislative District."""

        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Legislative District'], bins=20, edgecolor='k')
        plt.title('Histogram of Legislative District (Matplotlib)')
        plt.xlabel('Legislative District')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def legislative_district_seaborn(self):
        """- legislative_district_seaborn():
        Visualizes the distribution of Legislative District using Seaborn.

        Returns:Displays a histogram with a kernel density estimate"""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['Legislative District'], bins=20, kde=True)
        plt.title('Histogram of Legislative District (Seaborn)')
        plt.xlabel('Legislative District')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def dol_vehicleid_matplotlib(self):
        """ - dol_vehicleid_matplotlib():
        Visualizes the distribution of DOL Vehicle ID using Matplotlib.

        Returns:
        Displays a histogram of DOL Vehicle ID."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['DOL Vehicle ID'], bins=20, edgecolor='k')
        plt.title('Histogram of DOL Vehicle ID (Matplotlib)')
        plt.xlabel('DOL Vehicle ID')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def dol_vehicleid_seaborn(self):
        """- dol_vehicleid_seaborn():
        Visualizes the distribution of DOL Vehicle ID using Seaborn.

        Returns:
        Displays a histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['DOL Vehicle ID'], bins=20, kde=True)
        plt.title('Histogram of DOL Vehicle ID (Seaborn)')
        plt.xlabel('DOL Vehicle ID')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def censustract_matplotlib(self):
        """- censustract_matplotlib():
        Visualizes the distribution of 2020 Census Tract using Matplotlib.

        Returns:
    Displays a histogram of 2020 Census Tract."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['2020 Census Tract'], bins=20, edgecolor='k')
        plt.title('Histogram of 2020 Census Tract (Matplotlib)')
        plt.xlabel('2020 Census Tract')
        plt.ylabel('Frequency')
        output = plt.show()
        return output

    def censustract_seaborn(self):
        """
        -Visualizes the distribution of 2020 Census Tract using Seaborn.

        Returns:
        Histogram with a kernel density estimate."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df['2020 Census Tract'], bins=20, kde=True)
        plt.title('Histogram of 2020 Census Tract (Seaborn)')
        plt.xlabel('2020 Census Tract')
        plt.ylabel('Frequency')
        output = plt.show()
        return output



