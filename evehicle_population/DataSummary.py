"""
The purpose of this script is to offer a data type analysis and summary for a dataset that is derived from a CSV file.
To import the data, compute summary statistics, and identify the different types of attributes in the data,
it makes use of the Pandas library. The count of characteristics in each use case, the number of use cases in the dataset,
the data types, and the data summary are all output by the code. 
It is a helpful first step toward comprehending the features and organization of the dataset.
Kindly substitute the file path of the dataset you are utilizing for "Electric_Vehicle_Population_Data.csv."
"""

import pandas as pd



class DataSummary:
    """
    DataSummary class for handling Electric Vehicle Population Data.

    Attributes:
    - df (pd.DataFrame): DataFrame containing Electric Vehicle Population Data.

    Methods:
    - __init__(): Constructor method to initialize the DataSummary object and load data from a CSV file.
    - summary_statistics(): Method to generate summary statistics for the loaded data.
                           Returns a dictionary containing data summary, data types, use cases count,
                           and counts of attributes in each use case.
    """

    def __init__(self):
        """
        Constructor for the DataSummary class.

        Loads Electric Vehicle Population Data from a CSV file and initializes the df attribute.
        """
        self.df = pd.read_csv(
            "https://raw.githubusercontent.com/saidadi/codingscripts/main/sai/Electric_Vehicle_Population_Data%20(3).csv")

    def summary_statistics(self):
        """
        Generate summary statistics for the loaded data.

        Returns:
        dict: A dictionary containing the following information:
            - 'Data Summary': Summary statistics of the loaded data (pd.DataFrame).
            - 'Data Types': Data types of each attribute in the loaded data (pd.Series).
            - 'Use Cases': Count of use cases in the data (int).
            - 'No of Attributes in Particular Use Case': containing counts of attributes in each use case.
        """
        dfsummary = self.df.describe()
        dfdatatypes = self.df.dtypes
        uccount = len(dfsummary)
        attributecounts = [len(dfsummary[i]) for i in dfsummary]

        result = {
            "Data Summary": dfsummary,
            "Data Types": dfdatatypes,
            "Use Cases": uccount,
            "No of Attributes in Particular Use Case": attributecounts
        }

        print("\nData Types:")
        print(dfdatatypes)
        print(f"\nUse Cases: {uccount}")
        print(f"No of Attributes in Particular Use Case: {attributecounts}")

        return result

