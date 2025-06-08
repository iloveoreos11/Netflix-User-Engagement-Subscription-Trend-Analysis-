# 📚 Netflix Dataset Validation and Export 

import pandas as pd

# Load the cleaned Excel file
file_path = 'netflix_user_engagement_20233.xlsx'  

# Read Excel (xlsx uses openpyxl automatically)
df = pd.read_excel(file_path)

# Preview first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# Check dataset shape
print(f"\n📊 Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Check for missing values
print("\n🔍 Missing values per column:")
print(df.isnull().sum())

# Check data types
print("\n🔍 Data types of each column:")
print(df.dtypes)

# Unique values check for key columns (FIXED 'Churned' not 'Churn')
key_columns = ['SubscriptionTier', 'ContentGenreFavorite', 'churnflag', 'Churned']
for col in key_columns:
    print(f"\n📝 Unique values in {col}:")
    print(df[col].unique())

# Validate no negative watch hours or session counts
if (df['HoursWatched'] < 0).any() or (df['SessionsCount'] < 0).any():
    print("\n⚠️ Warning: Negative values found in HoursWatched or SessionsCount!")
else:
    print("\n✅ No negative values found in HoursWatched or SessionsCount.")


# Export the validated data to CSV
output_path = 'cleaned_netflix_data.csv'
df.to_csv(output_path, index=False)
print(f"\n✅ Cleaned and validated dataset exported successfully to {output_path}.")
