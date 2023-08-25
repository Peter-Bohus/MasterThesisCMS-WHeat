import os
import sys
import pandas as pd
from extract_species import extract_species_names

def process_files_in_folder(folder_path):
    print(f"Processing files in folder: {folder_path}")
    result_table = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".fasta"):
            file_path = os.path.join(folder_path, file_name)
            species_names = extract_species_names(file_path)

            if species_names:
                result_table.append({"File": file_name, "Species": ", ".join(species_names)})
    
    return result_table

def save_to_excel(output_file, result_table):
    print(f"Saving data to: {output_file}")
    df = pd.DataFrame(result_table)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_fasta_files.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Get the absolute path of the folder and remove any leading/trailing spaces and backslashes
    folder_path = os.path.abspath(folder_path).strip().rstrip("\\/")

    output_file = input("Enter the output Excel file name: ")

    result_table = process_files_in_folder(folder_path)

    if result_table:
        save_to_excel(output_file, result_table)
        print(f"\nData saved to '{output_file}' successfully.")
    else:
        print("No valid species names found in any .fasta files.")
