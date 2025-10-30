# Data Cleaning Utility

A comprehensive Python utility for detecting and fixing common data quality issues including missing values, incorrect data types, duplicates, and inconsistent formatting.

## 📋 Project Overview

This project is part of the **Syntecxhub Data Science Internship Program - Week 1, Project 3**. It provides a robust, reusable data cleaning utility that can handle real-world messy datasets and generate detailed cleaning reports.

## 🎯 Learning Objectives

- Detect and handle missing values using multiple strategies
- Fix incorrect data types and parse dates in various formats
- Remove duplicate records efficiently
- Standardize column names and text data
- Generate comprehensive cleaning logs and reports
- Understand data quality best practices

## ✨ Features

### 1. Missing Value Detection & Handling
- **Detect**: Identify missing values across all columns
- **Report**: Show count and percentage of missing data
- **Handle**: Multiple strategies available:
  - Drop rows with missing values
  - Fill numerical columns with mean/median
  - Fill categorical columns with mode
  - Smart strategy (adaptive based on data type and missing percentage)

### 2. Data Type Correction
- **Automatic Type Inference**: Convert columns to appropriate data types
- **Date Parsing**: Handle multiple date formats automatically
  - `2023-01-15`, `2023/02/20`, `March 10, 2023`, `05/15/2023`, etc.
- **Numerical Conversion**: Fix columns with mixed numeric/text data
- **Error Handling**: Gracefully handle conversion failures

### 3. Duplicate Removal
- **Detection**: Identify duplicate rows
- **Flexible Removal**: Choose which duplicates to keep (first/last/none)
- **Subset Checking**: Check duplicates based on specific columns
- **Detailed Reporting**: Show duplicate records before removal

### 4. Column Name Standardization
- **Lowercase Conversion**: All column names to lowercase
- **Space Removal**: Replace spaces with underscores
- **Special Character Handling**: Remove or replace special characters
- **Consistency**: Ensure uniform naming convention

### 5. Text Data Standardization
- **Capitalization**: Consistent title case or lowercase
- **Whitespace Trimming**: Remove leading/trailing spaces
- **Email Normalization**: Lowercase email addresses
- **Category Consistency**: Standardize categorical values

### 6. Comprehensive Logging
- **Detailed Logs**: Every cleaning step documented
- **Before/After Comparison**: Track all changes made
- **Statistics**: Row counts, missing values, data types
- **Exportable**: Save logs as text files for reference

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pandas library
- NumPy library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Zoro321-3/Syntecxhub_Data_Cleaning_Utility.git
cd Syntecxhub_Data_Cleaning_Utility
```

2. Install required dependencies:
```bash
pip install pandas numpy openpyxl
```

### Usage

#### Basic Usage

Run the main script to see a complete demonstration:
```bash
python data_cleaning_utility.py
```

#### Using the Cleaning Utility in Your Own Projects

```python
from data_cleaning_utility import DataCleaningUtility
import pandas as pd

# Load your dirty data
df = pd.read_csv('your_messy_data.csv')

# Initialize the cleaner
cleaner = DataCleaningUtility(df)

# Perform cleaning steps
cleaner.detect_missing_values()
cleaner.handle_missing_values(strategy='smart')
cleaner.fix_data_types()
cleaner.remove_duplicates()
cleaner.standardize_column_names()
cleaner.standardize_text_data()

# Generate report
cleaner.generate_report()

# Get cleaned data
cleaned_df = cleaner.get_cleaned_data()

# Save results
cleaned_df.to_csv('cleaned_data.csv', index=False)
cleaner.save_cleaning_log('cleaning_log.txt')
```

## 📊 Sample Output

### Input: Dirty Data
The script generates sample data with common issues:
- Missing values in multiple columns
- Inconsistent data types (e.g., age stored as text)
- Multiple date formats
- Duplicate records
- Inconsistent column names with spaces
- Mixed text capitalization

### Output: Cleaned Data
- All missing values handled appropriately
- Correct data types for all columns
- Standardized date formats
- Duplicates removed
- Clean, consistent column names
- Standardized text formatting

### Cleaning Log Example
```
======================================================================
DATA CLEANING LOG
Started at: 2024-10-30 15:30:45
======================================================================

Original Dataset Shape: (27, 10)

======================================================================
1. DETECTING MISSING VALUES
======================================================================

Found missing values in 5 columns:
Column              Missing_Count  Missing_Percent
First Name                     3            11.11
Email Address                  2             7.41
Registration Date              1             3.70
Purchase_Amount                3            11.11

--- HANDLING MISSING VALUES ---
Strategy: smart
  ✓ Filled 'First Name' with mode: John
  ✓ Filled 'Purchase_Amount' with median: 265.50
  ...
```

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Pandas** - Data manipulation and cleaning
- **NumPy** - Numerical operations
- **datetime** - Date parsing and manipulation

## 📁 Project Structure

```
Syntecxhub_Data_Cleaning_Utility/
│
├── data_cleaning_utility.py    # Main Python script
├── README.md                    # Project documentation
│
├── Input Files/
│   └── dirty_data.csv          # Generated sample messy data
│
└── Output Files/
    ├── cleaned_data.csv        # Cleaned dataset
    └── cleaning_log.txt        # Detailed cleaning report
```

## 🎓 Key Concepts Covered

- **Data Quality Assessment**: Identifying data quality issues
- **Missing Value Imputation**: Different strategies for handling missing data
- **Type Conversion**: Converting data to appropriate types
- **Date Parsing**: Handling various date formats
- **Duplicate Detection**: Finding and removing duplicate records
- **Data Standardization**: Consistent formatting across dataset
- **Logging Best Practices**: Documenting data transformations
- **Defensive Programming**: Handling errors gracefully

## 💡 Cleaning Strategies

### Smart Missing Value Strategy
The utility uses intelligent handling based on:
- **Numerical Columns**: 
  - If < 30% missing → Fill with median
  - If ≥ 30% missing → Drop rows
- **Categorical Columns**:
  - If < 50% missing → Fill with mode
  - If ≥ 50% missing → Drop rows

### Date Parsing
Automatically handles formats:
- ISO format: `2023-01-15`
- Slash format: `2023/02/20`
- Written format: `March 10, 2023`
- Mixed format: `10-25-2023`

### Duplicate Handling
- By default, keeps first occurrence
- Can be customized to keep last or remove all
- Can check duplicates based on specific columns

## 📈 Common Data Quality Issues Addressed

1. **Missing Data**
   - Incomplete records
   - NULL values
   - Empty strings

2. **Type Issues**
   - Numbers stored as text
   - Inconsistent date formats
   - Mixed data types in columns

3. **Duplicates**
   - Exact duplicate rows
   - Duplicates based on key columns
   - Multiple entries for same entity

4. **Formatting Issues**
   - Inconsistent capitalization
   - Extra whitespace
   - Special characters in column names
   - Inconsistent category values

5. **Structural Issues**
   - Non-standard column names
   - Inconsistent data layout

## 🔍 Use Cases

This utility is perfect for:
- **Data Preprocessing**: Clean data before analysis
- **ETL Pipelines**: Data transformation workflows
- **Data Migration**: Standardize data from multiple sources
- **Quality Assurance**: Ensure data meets quality standards
- **Reporting**: Generate data quality reports
- **Machine Learning**: Prepare data for ML models

## 🤝 Contributing

This is an internship project, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 👨‍💻 Author

**Syntecxhub Data Science Intern**
- GitHub: [@Zoro321-3](https://github.com/Zoro321-3)
- LinkedIn: [www.linkedin.com/in/olamitide-adesiyan-b2256925b]

## 📝 License

This project is created for educational purposes as part of the Syntecxhub Internship Program.

## 🙏 Acknowledgments

- **Syntecxhub** - For providing this learning opportunity
- **Pandas Community** - For excellent data manipulation tools
- **Data Science Community** - For best practices and inspiration

## 📞 Contact

For questions or feedback regarding this project:
- Email: info@syntecxhub.com
- Phone: +91 63937 80295
- Website: [www.syntecxhub.com](https://www.syntecxhub.com)

## 🔗 Related Projects

- [NumPy Data Explorer](https://github.com/Zoro321-3/NumPy-Data-Explorer) - Week 1, Project 1
- [Pandas CSV Reader](https://github.com/Zoro321-3/Syntecxhub_Pandas_CSV_Reader) - Week 1, Project 2

---

⭐ If you find this project helpful, please consider giving it a star!

**Project Status**: Completed ✅ | **Week**: 1 | **Project**: 3 | **Program**: Syntecxhub Data Science Internship
