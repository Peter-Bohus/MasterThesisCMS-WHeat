import pandas as pd
import re

def remove_numbers_from_table(input_file, output_file):
    # Read the input Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file)

    # Regular expression pattern to match numbers in the format "55. "
    pattern = r"\b\d+\.\s\b"

    # Remove numbers from each cell in the DataFrame
    for col in df.columns:
        df[col] = df[col].apply(lambda x: re.sub(pattern, "", str(x)))

    # Save the updated DataFrame to a new Excel file using the 'openpyxl' engine
    df.to_excel(output_file, index=False, engine='openpyxl')

if __name__ == "__main__":
    input_file = input("Enter the input Excel file name: ")
    output_file = input("Enter the output Excel file name: ")

    remove_numbers_from_table(input_file, output_file)
    print(f"\nNumbers removed from '{input_file}' and saved to '{output_file}' successfully.")
