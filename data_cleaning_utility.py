"""
Data Cleaning Utility
---------------------
A comprehensive project demonstrating data cleaning techniques including:
- Detecting and handling missing values (drop/fill/impute)
- Fixing incorrect data types and parsing dates
- Removing duplicates
- Standardizing column names
- Generating cleaning logs and reports

Author: Syntecxhub Data Science Intern
Project: Week 1 - Data Cleaning Utility
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# GENERATE DIRTY SAMPLE DATA
# ============================================================================

def generate_dirty_data():
    """Generates sample dataset with common data quality issues"""
    print("="*70)
    print("GENERATING DIRTY SAMPLE DATA")
    print("="*70)
    
    np.random.seed(42)
    
    # Create intentionally messy data
    data = {
        'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                       16, 17, 18, 19, 20, 5, 6, 21, 22, 23, 24, 25],  # Contains duplicates (5, 6)
        'First Name': ['John', 'Jane', 'Bob', np.nan, 'Alice', 'Charlie', 'David',
                      'Emma', 'Frank', np.nan, 'Grace', 'Henry', 'Ivy', 'Jack',
                      'Kate', 'Leo', 'Mia', 'Noah', 'Olivia', 'Paul', 'Bob', 
                      'Charlie', 'Quinn', 'Rose', 'Sam', np.nan, 'Uma'],  # Missing values
        ' Last_Name ': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
                       'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez',
                       'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor',
                       'Moore', 'Jackson', 'Johnson', 'Jones', 'Lee', 'Walker',
                       'Hall', 'Allen', 'Young'],  # Inconsistent spacing
        'age': ['25', '30', 'thirty-five', '28', '45', '32', '29', '35', 
               '40', '26', '33', '38', '27', '31', '36', '24', '34', '39',
               '41', '23', '45', '32', '37', '42', '44', '22', '43'],  # Mixed types
        'Email Address': ['john@email.com', 'jane@email.com', 'bob@email.com',
                         'williams@email.com', 'alice@EMAIL.COM', 'charlie@email.com',
                         'david@email.com', np.nan, 'frank@email.com', 'rodriguez@email.com',
                         'grace@email.com', 'henry@email.com', np.nan, 'jack@email.com',
                         'kate@email.com', 'leo@email.com', 'mia@email.com', 'noah@email.com',
                         'olivia@email.com', 'paul@email.com', 'bob@email.com', 
                         'charlie@email.com', 'quinn@email.com', 'rose@email.com',
                         'sam@email.com', 'allen@email.com', 'uma@email.com'],  # Missing values, inconsistent case
        'Phone_Number': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123',
                        '567-890-1234', '678-901-2345', np.nan, '890-123-4567',
                        '901-234-5678', '012-345-6789', '123-456-7891', np.nan,
                        '345-678-9013', '456-789-0124', '567-890-1235', '678-901-2346',
                        '789-012-3457', '890-123-4568', '901-234-5679', '012-345-6780',
                        '567-890-1234', '678-901-2345', '234-567-8902', '345-678-9014',
                        '456-789-0125', '567-890-1236', '678-901-2347'],  # Missing values
        'Registration Date': ['2023-01-15', '2023/02/20', 'March 10, 2023', '2023-04-05',
                             '05/15/2023', '2023-06-01', '2023-07-12', '2023-08-23',
                             '2023-09-14', '10-25-2023', '2023-11-05', 'December 1, 2023',
                             '2024-01-10', '2024/02/14', '03/20/2024', '2024-04-08',
                             '2024-05-16', '06/22/2024', '2024-07-30', '2024-08-11',
                             '05/15/2023', '2023-06-01', '2024-09-05', '2024-10-12',
                             '11/18/2024', '2024-12-03', np.nan],  # Inconsistent date formats, missing value
        'Purchase_Amount': [150.50, 200.75, np.nan, 89.99, 450.00, 125.25,
                          np.nan, 350.50, 275.00, 190.75, 425.50, 310.25,
                          np.nan, 175.00, 265.50, 395.75, 155.25, 285.00,
                          330.50, 215.75, 450.00, 125.25, 405.50, 295.75,
                          185.00, 375.25, 225.50],  # Missing values
        'CITY': ['Lagos', 'Ibadan', 'Abuja', 'Lagos', 'Port Harcourt', 'Kano',
                'Lagos', 'Ibadan', 'Abuja', 'Lagos', 'Ibadan', 'Lagos',
                'Kano', 'Abuja', 'Lagos', 'Port Harcourt', 'Ibadan', 'Lagos',
                'Abuja', 'Kano', 'Port Harcourt', 'Kano', 'Lagos', 'Ibadan',
                'Abuja', 'Lagos', 'Port Harcourt'],
        'Member Status': ['Active', 'active', 'ACTIVE', 'Inactive', 'Active', 'inactive',
                         'Active', 'INACTIVE', 'Active', 'active', 'Inactive', 'ACTIVE',
                         'active', 'Inactive', 'Active', 'inactive', 'ACTIVE', 'Active',
                         'inactive', 'Active', 'Active', 'inactive', 'ACTIVE', 'active',
                         'Inactive', 'Active', 'inactive']  # Inconsistent capitalization
    }
    
    df = pd.DataFrame(data)
    
    # Save dirty data
    df.to_csv('dirty_data.csv', index=False)
    print("\n✓ Created 'dirty_data.csv' with the following issues:")
    print("  - Missing values in multiple columns")
    print("  - Inconsistent data types (age column has strings)")
    print("  - Inconsistent date formats")
    print("  - Duplicate rows (Customer IDs 5 and 6)")
    print("  - Inconsistent column names (spaces, mixed case)")
    print("  - Inconsistent text capitalization")
    print("  - Extra whitespace in column names")
    
    return df


# ============================================================================
# DATA CLEANING UTILITY
# ============================================================================

class DataCleaningUtility:
    """Comprehensive data cleaning utility class"""
    
    def __init__(self, df):
        """Initialize with a DataFrame"""
        self.df = df.copy()
        self.original_df = df.copy()
        self.cleaning_log = []
        self.log_entry("="*70)
        self.log_entry("DATA CLEANING LOG")
        self.log_entry(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log_entry("="*70)
        self.log_entry(f"\nOriginal Dataset Shape: {df.shape}")
        self.log_entry(f"Original Columns: {list(df.columns)}\n")
    
    def log_entry(self, message):
        """Add entry to cleaning log"""
        self.cleaning_log.append(message)
        print(message)
    
    # ========================================================================
    # 1. DETECT AND HANDLE MISSING VALUES
    # ========================================================================
    
    def detect_missing_values(self):
        """Detect and report missing values"""
        self.log_entry("\n" + "="*70)
        self.log_entry("1. DETECTING MISSING VALUES")
        self.log_entry("="*70)
        
        missing_count = self.df.isnull().sum()
        missing_percent = (self.df.isnull().sum() / len(self.df) * 100).round(2)
        
        missing_df = pd.DataFrame({
            'Column': missing_count.index,
            'Missing_Count': missing_count.values,
            'Missing_Percent': missing_percent.values
        })
        
        missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
        
        if len(missing_df) > 0:
            self.log_entry(f"\nFound missing values in {len(missing_df)} columns:")
            self.log_entry(missing_df.to_string(index=False))
        else:
            self.log_entry("\n✓ No missing values found")
        
        return missing_df
    
    def handle_missing_values(self, strategy='smart'):
        """
        Handle missing values using different strategies
        
        Strategies:
        - 'drop': Drop rows with missing values
        - 'fill_mean': Fill numerical columns with mean
        - 'fill_median': Fill numerical columns with median
        - 'fill_mode': Fill categorical columns with mode
        - 'smart': Intelligent handling based on data type and missing percentage
        """
        self.log_entry("\n--- HANDLING MISSING VALUES ---")
        self.log_entry(f"Strategy: {strategy}")
        
        rows_before = len(self.df)
        
        if strategy == 'drop':
            self.df = self.df.dropna()
            self.log_entry(f"Dropped all rows with missing values")
            self.log_entry(f"Rows removed: {rows_before - len(self.df)}")
        
        elif strategy == 'smart':
            # For numerical columns: fill with median if < 30% missing, else drop
            # For categorical columns: fill with mode if < 50% missing, else drop
            
            for col in self.df.columns:
                missing_pct = (self.df[col].isnull().sum() / len(self.df)) * 100
                
                if missing_pct > 0:
                    if self.df[col].dtype in ['float64', 'int64']:
                        if missing_pct < 30:
                            median_val = self.df[col].median()
                            self.df[col].fillna(median_val, inplace=True)
                            self.log_entry(f"  ✓ Filled '{col}' with median: {median_val:.2f}")
                        else:
                            self.df = self.df.dropna(subset=[col])
                            self.log_entry(f"  ✓ Dropped rows with missing '{col}' (>{30}% missing)")
                    else:
                        if missing_pct < 50:
                            mode_val = self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else "Unknown"
                            self.df[col].fillna(mode_val, inplace=True)
                            self.log_entry(f"  ✓ Filled '{col}' with mode: {mode_val}")
                        else:
                            self.df = self.df.dropna(subset=[col])
                            self.log_entry(f"  ✓ Dropped rows with missing '{col}' (>{50}% missing)")
        
        else:
            self.log_entry(f"Unknown strategy: {strategy}")
        
        self.log_entry(f"\nRows after handling missing values: {len(self.df)}")
    
    # ========================================================================
    # 2. FIX INCORRECT DATA TYPES
    # ========================================================================
    
    def fix_data_types(self):
        """Fix incorrect data types and parse dates"""
        self.log_entry("\n" + "="*70)
        self.log_entry("2. FIXING INCORRECT DATA TYPES")
        self.log_entry("="*70)
        
        self.log_entry("\nOriginal Data Types:")
        for col in self.df.columns:
            self.log_entry(f"  {col}: {self.df[col].dtype}")
        
        # Fix age column (convert to numeric)
        if 'age' in self.df.columns:
            self.log_entry("\n--- Fixing 'age' column ---")
            # Convert non-numeric values
            self.df['age'] = pd.to_numeric(self.df['age'], errors='coerce')
            # Fill NaN with median
            median_age = self.df['age'].median()
            self.df['age'].fillna(median_age, inplace=True)
            self.df['age'] = self.df['age'].astype(int)
            self.log_entry(f"✓ Converted 'age' to integer (filled invalid values with median: {int(median_age)})")
        
        # Parse dates
        date_columns = [col for col in self.df.columns if 'date' in col.lower()]
        
        if date_columns:
            self.log_entry("\n--- Parsing Date Columns ---")
            for col in date_columns:
                try:
                    self.df[col] = pd.to_datetime(self.df[col], errors='coerce', infer_datetime_format=True)
                    # Fill missing dates with mode or a default date
                    if self.df[col].isnull().sum() > 0:
                        mode_date = self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else pd.Timestamp('2024-01-01')
                        self.df[col].fillna(mode_date, inplace=True)
                    self.log_entry(f"✓ Parsed '{col}' as datetime")
                except Exception as e:
                    self.log_entry(f"✗ Could not parse '{col}': {str(e)}")
        
        self.log_entry("\nUpdated Data Types:")
        for col in self.df.columns:
            self.log_entry(f"  {col}: {self.df[col].dtype}")
    
    # ========================================================================
    # 3. REMOVE DUPLICATES
    # ========================================================================
    
    def remove_duplicates(self, subset=None, keep='first'):
        """
        Remove duplicate rows
        
        Parameters:
        - subset: Column(s) to check for duplicates (default: all columns)
        - keep: 'first', 'last', or False (remove all duplicates)
        """
        self.log_entry("\n" + "="*70)
        self.log_entry("3. REMOVING DUPLICATES")
        self.log_entry("="*70)
        
        rows_before = len(self.df)
        
        if subset:
            duplicates = self.df.duplicated(subset=subset, keep=False)
            self.log_entry(f"\nChecking duplicates based on: {subset}")
        else:
            duplicates = self.df.duplicated(keep=False)
            self.log_entry("\nChecking duplicates based on all columns")
        
        duplicate_count = duplicates.sum()
        
        if duplicate_count > 0:
            self.log_entry(f"Found {duplicate_count} duplicate rows:")
            self.log_entry(self.df[duplicates].to_string())
            
            self.df = self.df.drop_duplicates(subset=subset, keep=keep)
            rows_removed = rows_before - len(self.df)
            self.log_entry(f"\n✓ Removed {rows_removed} duplicate rows (keeping '{keep}')")
        else:
            self.log_entry("\n✓ No duplicate rows found")
        
        self.log_entry(f"Rows after removing duplicates: {len(self.df)}")
    
    # ========================================================================
    # 4. STANDARDIZE COLUMN NAMES
    # ========================================================================
    
    def standardize_column_names(self):
        """Standardize column names (lowercase, underscores, no spaces)"""
        self.log_entry("\n" + "="*70)
        self.log_entry("4. STANDARDIZING COLUMN NAMES")
        self.log_entry("="*70)
        
        self.log_entry("\nOriginal Column Names:")
        self.log_entry(f"  {list(self.df.columns)}")
        
        # Create mapping of old to new names
        name_mapping = {}
        for col in self.df.columns:
            # Remove leading/trailing spaces, convert to lowercase, replace spaces with underscores
            new_name = col.strip().lower().replace(' ', '_').replace('-', '_')
            # Remove special characters
            new_name = ''.join(c for c in new_name if c.isalnum() or c == '_')
            name_mapping[col] = new_name
        
        self.df.rename(columns=name_mapping, inplace=True)
        
        self.log_entry("\nStandardized Column Names:")
        self.log_entry(f"  {list(self.df.columns)}")
        
        if name_mapping:
            self.log_entry("\nChanges made:")
            for old, new in name_mapping.items():
                if old != new:
                    self.log_entry(f"  '{old}' → '{new}'")
    
    # ========================================================================
    # 5. STANDARDIZE TEXT DATA
    # ========================================================================
    
    def standardize_text_data(self):
        """Standardize text data (consistent capitalization, trim whitespace)"""
        self.log_entry("\n" + "="*70)
        self.log_entry("5. STANDARDIZING TEXT DATA")
        self.log_entry("="*70)
        
        text_columns = self.df.select_dtypes(include=['object']).columns
        
        for col in text_columns:
            # Skip email columns (preserve case)
            if 'email' in col.lower():
                self.df[col] = self.df[col].str.strip().str.lower()
                self.log_entry(f"✓ Standardized '{col}' (lowercase, trimmed)")
            else:
                # Title case for names, trim whitespace
                self.df[col] = self.df[col].str.strip().str.title()
                self.log_entry(f"✓ Standardized '{col}' (title case, trimmed)")
    
    # ========================================================================
    # GENERATE CLEANING REPORT
    # ========================================================================
    
    def generate_report(self):
        """Generate comprehensive cleaning report"""
        self.log_entry("\n" + "="*70)
        self.log_entry("CLEANING SUMMARY")
        self.log_entry("="*70)
        
        self.log_entry(f"\nOriginal Dataset:")
        self.log_entry(f"  Rows: {len(self.original_df)}")
        self.log_entry(f"  Columns: {len(self.original_df.columns)}")
        self.log_entry(f"  Missing Values: {self.original_df.isnull().sum().sum()}")
        
        self.log_entry(f"\nCleaned Dataset:")
        self.log_entry(f"  Rows: {len(self.df)}")
        self.log_entry(f"  Columns: {len(self.df.columns)}")
        self.log_entry(f"  Missing Values: {self.df.isnull().sum().sum()}")
        
        rows_removed = len(self.original_df) - len(self.df)
        self.log_entry(f"\nRows Removed: {rows_removed} ({(rows_removed/len(self.original_df)*100):.2f}%)")
        
        self.log_entry(f"\nCleaned at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log_entry("="*70)
    
    def get_cleaned_data(self):
        """Return the cleaned DataFrame"""
        return self.df
    
    def save_cleaning_log(self, filename='cleaning_log.txt'):
        """Save cleaning log to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.cleaning_log))
        print(f"\n✓ Cleaning log saved to '{filename}'")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to demonstrate data cleaning"""
    print("\n" + "="*70)
    print(" "*15 + "DATA CLEANING UTILITY")
    print(" "*10 + "Syntecxhub Data Science Internship")
    print(" "*20 + "Week 1 - Project 3")
    print("="*70 + "\n")
    
    # Generate dirty data
    dirty_df = generate_dirty_data()
    
    print("\n" + "="*70)
    print("DIRTY DATA PREVIEW")
    print("="*70)
    print(dirty_df.head(10))
    print(f"\nShape: {dirty_df.shape}")
    print(f"Missing values: {dirty_df.isnull().sum().sum()}")
    
    # Initialize cleaning utility
    cleaner = DataCleaningUtility(dirty_df)
    
    # Perform cleaning steps
    cleaner.detect_missing_values()
    cleaner.handle_missing_values(strategy='smart')
    cleaner.fix_data_types()
    cleaner.remove_duplicates(subset=['Customer ID'])
    cleaner.standardize_column_names()
    cleaner.standardize_text_data()
    
    # Generate report
    cleaner.generate_report()
    
    # Get cleaned data
    cleaned_df = cleaner.get_cleaned_data()
    
    print("\n" + "="*70)
    print("CLEANED DATA PREVIEW")
    print("="*70)
    print(cleaned_df.head(10))
    print(f"\nShape: {cleaned_df.shape}")
    print(f"Missing values: {cleaned_df.isnull().sum().sum()}")
    
    # Save cleaned data
    cleaned_df.to_csv('cleaned_data.csv', index=False)
    print("\n✓ Cleaned data saved to 'cleaned_data.csv'")
    
    # Save cleaning log
    cleaner.save_cleaning_log()
    
    print("\n" + "="*70)
    print(" "*15 + "PROJECT COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nGenerated Files:")
    print("  Input:")
    print("    - dirty_data.csv (original messy data)")
    print("  Output:")
    print("    - cleaned_data.csv (cleaned dataset)")
    print("    - cleaning_log.txt (detailed cleaning report)")
    print("\nNext steps:")
    print("  1. Review the cleaning log to understand all changes")
    print("  2. Compare dirty_data.csv with cleaned_data.csv")
    print("  3. Upload this code to your GitHub repository")
    print("  4. Submit through the official Submission Form")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
