# CSV Fuzzy Matcher :mag_right:

CSV Fuzzy Matcher is a Python script that automates the matching of data between two CSV files using fuzzy string matching techniques. It aims to find matching rows in the second CSV file based on specified columns while allowing flexibility for inconsistencies in naming conventions.

🚀 **Features**
- Matches data between Google Sheets CSV and Excel CSV files.
- Uses fuzzywuzzy library to compare similar but inconsistently named data.
- Provides flexibility in matching rows based on selected columns.
- Easy to set up and run with minimal dependencies.

🔧 **Setup and Usage (Under Development)**
1. Clone the repository to your local machine.
2. Make sure you have Python and required libraries (pandas, fuzzywuzzy) installed.
3. Place your master.csv and second.csv files in the project directory.
4. Update the script's `columns_to_compare` list to include the columns you want to match.
5. Run the script and get the results in the `updates.csv` file.

🔍 **How It Works**
1. Loads data from `master.csv` and `second.csv` files.
2. Performs fuzzy string matching on the 'Style Name' column for rows with matching 'Style No' and 'Channel'.
3. Creates a new CSV file, `updates.csv`, containing unmatched rows from `master.csv` and their fuzzy match results.

📝 **Note**
- The script currently provides fuzzy matching results with a token set ratio of 80 or higher. You can adjust this threshold in the `fuzzy_match` function for more or less strict matching.

🛠️ **Under Development**
- The setup and usage instructions are still being finalized and may be subject to changes.
- We are actively working on adding more features and refining the matching process.

Feel free to explore, modify, and use this script to streamline your CSV data matching process. If you encounter any issues or have ideas for improvements, don't hesitate to open an issue or contribute to the project!

📚 **Resources**
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [FuzzyWuzzy Documentation](https://github.com/seatgeek/fuzzywuzzy)

Happy matching! :raised_hands:
