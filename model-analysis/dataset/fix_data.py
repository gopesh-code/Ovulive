# the dataset has some columns where only the first row for a certain client has values and the rest are empty
# this script fills in the missing values with the values from the first row

import pandas as pd

INPUT_FILE = "./FedCycleData071012 (2).csv"
OUTPUT_FILE = "./FedCycleData071012 (2)_new_fixed.csv"
# COLUMNS_TO_FIX = ['MeanCycleLength', 'MeanMensesLength', 'MeanBleedingIntensity', 'Age', 'Religion', 'Ethnicity', 'Height', 'Weight', ]

COLUMNS_TO_FIX = ["MeanCycleLength","MeanMensesLength","MeanBleedingIntensity","Age","AgeM","Maristatus","MaristatusM","Yearsmarried","Wedding","Religion","ReligionM","Ethnicity","EthnicityM","Schoolyears","SchoolyearsM","OccupationM","IncomeM","Height","Weight","Reprocate","Numberpreg","Livingkids","Miscarriages","Abortions","Medvits","Medvitexplain","Gynosurgeries","LivingkidsM","Boys","Girls","MedvitsM","MedvitexplainM","Urosurgeries","Breastfeeding","Method","Prevmethod","Methoddate","Whychart","Nextpreg","NextpregM","Spousesame","SpousesameM","Timeattemptpreg","BMI"]
# empty space " " should be replaced with NaN
df = pd.read_csv(INPUT_FILE, na_values=[' '])

# def fix_column(column_name):
#     # Find the value of the column in the first row for each client
#     first_row = df.groupby('ClientID').first()
#     fill_values = first_row[column_name]

#     # Fill in missing values for each client using the corresponding fill value
#     df[column_name] = df.apply(lambda row: fill_values[row['ClientID']] if pd.isnull(row[column_name]) else row[column_name], axis=1)
def fix_column(column_name):
    """
    Fill missing values in a column based on the first row for each client ID.

    Args:
        column_name (str): the name of the column to fix

    Returns:
        None, modifies the data in place
    """
    # For each client, find the first non-missing value in the column_name column
    first_values_by_client = df.groupby('ClientID')[column_name].first().to_dict()

    # Fill missing values in column_name based on first_values_by_client
    df[column_name].fillna(df['ClientID'].map(first_values_by_client), inplace=True)

    print(df.head(10))

for column in COLUMNS_TO_FIX:
    fix_column(column)

df.to_csv(OUTPUT_FILE, index=False)

# # iterate through each client ID
# for client_id in client_ids:
#     # get the rows for the current client ID
#     client_rows = df[df['ClientID'] == client_id]

#     # get the indices of the rows for the current client ID
#     client_row_indices = client_rows.index

#     # iterate through each column in the dataframe
#     for column in COLUMNS_TO_FIX:
#         # get the values for the current column
#         column_values = df[column]

#         # iterate through each row index for the current client ID
#         for row_index in client_row_indices:
#             # if the value for the current row index is empty
#             if pd.isnull(column_values[row_index]):
#                 # set the value for the current row index to the value of the first row for the current client ID
#                 df.loc[row_index, column] = df.loc[client_row_indices[0], column]


# # save the dataframe to a new CSV file
# df.to_csv(OUTPUT_FILE, index=False)


# # iterate through each client ID
# for client_id in client_ids:
#     # get the rows for the current client ID
#     client_rows = df[df['ClientID'] == client_id]

#     # get the indices of the rows for the current client ID
#     client_row_indices = client_rows.index

#     # iterate through each column in the dataframe
#     for column in df.columns:
#         # get the values for the current column
#         column_values = df[column]

#         # iterate through each row index for the current client ID
#         for row_index in client_row_indices:
#             # if the value for the current row index is empty
#             if pd.isnull(column_values[row_index]):
#                 # set the value for the current row index to the value of the first row for the current client ID
#                 df.loc[row_index, column] = df.loc[client_row_indices[0], column]


# # save the dataframe to a new CSV file
# df.to_csv("./datasets/FedCycleData071012 (2).csv", index=False)