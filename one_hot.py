# Program for demonstration of one hot encoding
# Import libraries
import numpy as np
import pandas as pd

# Creating Data
data = {'Employee id': [45, 78, 56, 12, 7, 68, 23, 45, 89, 75, 47, 62],
        'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
        'Remarks': ['Nice', 'Good', 'Great', 'Great', 'Nice', 'Great', 'Good', 'Nice', 'Great', 'Nice', 'Good', 'Nice'],
        }

# Create DataFrame
data2 = pd.DataFrame(data)
print(data2.head())

# Unique Elements in Categorical Column
print('\nUnique elements:')
print(data2['Gender'].unique())
print(data2['Remarks'].unique())

# Count of Elements in the Column
print('\nCount of Elements:')
print(data2['Gender'].value_counts())
print(data2['Remarks'].value_counts())

"""One-hot Encoding"""
# Using Pandas
one_hot_encoded_data = pd.get_dummies(data2, columns = ['Remarks', 'Gender'])
print(f"\nOne-Hot encoded data: \n{one_hot_encoded_data}")

# Using Sci-Kit Learn 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Building a dummy employee dataset for example
data = {'Employee id': [10, 20, 15, 25, 30],
        'Gender': ['M', 'F', 'F', 'M', 'F'],
        'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice'],
        }

# Converting into a Pandas dataframe
df = pd.DataFrame(data)

# Print the dataframe:
print(f"Employee data : \n{df}")

# Extract categorical columns from the dataframe
# Here we extract the columns with object datatype as they are the categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

# Initialize OneHotEncoder
encoder = OneHotEncoder(sparse_output=False) # dense array

# Apply one-hot encoding to the categorical columns
one_hot_encoded = encoder.fit_transform(df[categorical_columns])

# Create a DataFrame with the one-hot encoded columns
# We use get_feature_names_out() to get the column names for the encoded data
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

# Concatenate the one-hot encoded dataframe with the original dataframe
df_encoded = pd.concat([df, one_hot_df], axis=1)

# Drop the original categorical columns
df_encoded = df_encoded.drop(categorical_columns, axis=1)

# Display the resulting dataframe
print(f"Encoded Employee data : \n{df_encoded}")