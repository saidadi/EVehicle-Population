'''
This code uses an Electric_Vehicle_Population_Data dataset to do exploratory data analysis (EDA). After importing the dataset, the EDA chooses a subset of information pertinent to the study, paying particular attention to the attributes "Make," "Model," and "Electric Range." It eliminates rows with missing values to guarantee the completeness of the data.
The code then uses Seaborn and Matplotlib to build scatterplots that show the electric range distribution by vehicle make. The scatterplots, which have an alpha of 0.3 to accommodate for overlapping spots, shed light on how the electric range varies amongst various car makes.
We can potentially identify patterns or trends in the data by using this analysis to better understand the relationship between the 'Make' and 'Electric Range' parameters. 

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Inference:
    """
    Inference class for analysis and visualization of Electric Vehicle Population Data.

    Attributes:
    - df (pd.DataFrame): DataFrame containing Electric Vehicle Population Data.
    - subset_df (pd.DataFrame): Subset of the original data with selected columns for analysis.

    Methods:
    - __init__(): Constructor method to initialize the Inference object, load data, and prepare a subset for analysis.

    - distribution_of_electric_range_matplotlib():
        Visualizes the distribution of electric range by vehicle make using Matplotlib.

        Returns:
        None. Displays a scatterplot.

    - distribution_of_electric_range_seaborn():
        Visualizes the distribution of electric range by vehicle make using Seaborn.

        Returns:
        None. Displays a scatterplot.
    """

    def __init__(self):
        """
        Constructor for the Inference class.

        - Loads Electric Vehicle Population Data from a CSV file.
        - Creates a subset of the data containing 'Make', 'Model', and 'Electric Range'.
        - Filters out rows with missing values.
        """
        self.df = pd.read_csv(
            'https://raw.githubusercontent.com/saidadi/codingscripts/main/sai/Electric_Vehicle_Population_Data%20(3).csv')

        # Subset the data for analysis
        self.subset_df = self.df[['Make', 'Model', 'Electric Range']]

        # Filter out rows with missing values
        self.subset_df = self.subset_df.dropna()

    def distribution_of_electric_range_matplotlib(self):
        """
        Visualizes the distribution of electric range by vehicle make using Matplotlib.

        Returns:
        None. Displays a scatterplot.
        """
        plt.figure(figsize=(10, 6))
        plt.title("Electric Range by Vehicle Make (Matplotlib)")
        plt.scatter(self.subset_df['Make'], self.subset_df['Electric Range'], alpha=0.3)
        plt.xlabel("Make")
        plt.ylabel("Electric Range (miles)")
        plt.xticks(rotation=90)
        output = plt.show()
        return output

    def distribution_of_electric_range_seaborn(self):
        """
        Visualizes the distribution of electric range by vehicle make using Seaborn.

        Returns:
        None. Displays a scatterplot.
        """
        plt.figure(figsize=(10, 6))
        plt.title("Electric Range by Vehicle Make (Seaborn)")
        sns.scatterplot(data=self.subset_df, x='Make', y='Electric Range', alpha=0.3)
        plt.xlabel("Make")
        plt.ylabel("Electric Range (miles)")
        plt.xticks(rotation=90)
        output = plt.show()
        return output



