import re

def extract_species_names(file_name):
    species_names = set()

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            header_lines = [line.strip() for line in lines if line.startswith(">")]

            for header in header_lines:
                match = re.search(r">[^_]+_(.+?)(?:_\w+)?;", header)
                if match:
                    species_name = match.group(1)
                    species_names.add(species_name)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing the file.\n{e}")
        return []

    return species_names

if __name__ == "__main__":
    file_name = input("Enter the file name (including path if necessary): ")
    species_names = extract_species_names(file_name)

    if species_names:
        print("\nTable of Wheat Species:")
        print("-----------------------")
        for i, species in enumerate(species_names, 1):
            print(f"{i}. {species}")
    else:
        print("No valid species names found in the file.")
