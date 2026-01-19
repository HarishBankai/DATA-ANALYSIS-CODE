# importing necessary libraries
try:
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.impute import SimpleImputer
    print("All libraries imported successfully.")
except ImportError as e:
    print(f"Error importing libraries: {e}")
    print("Please install missing libraries by running '!pip install <library_name>' in Jupyter cell.")

# Sample Dataset
data = pd.DataFrame({
    'age': [25, 35, 45, None, 50],
    'income': [50000, 60000, 70000, 80000, None],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'purchased': [0, 1, 0, 1, 1]
})

required_columns = ['age', 'income', 'gender', 'purchased']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Missing required columns: {missing_columns}")
else:
    print("All required columns are present.")

X = data.drop('purchased', axis=1)
y = data['purchased']

print("\nInspecting data types:")
print(X.dtypes)
print("\nFirst few rows of data:")
print(X.head())

# Defining columns for preprocessing
numerical_features = ['age', 'income']
categorical_features = ['gender']

# Verifying that columns for numerical and categorical features exist in the data
missing_numerical = [col for col in numerical_features if col not in X.columns]
missing_categorical = [col for col in categorical_features if col not in X.columns]

if missing_numerical or missing_categorical:
    print(f"Missing columns for pipeline: {missing_numerical + missing_categorical}")
else:
    print("All specified columns are present for the pipeline.")