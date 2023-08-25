import pandas as pd

# Read the input CSV file
input_file = "Genes.csv"
df = pd.read_csv(input_file)

# Create a list to store the output data as dictionaries
output_data = []

# Get the species names for each gene
species_names = {
    "Atp1": df["Atp1"].dropna().tolist(),
    "ccmFC": df["ccmFC"].dropna().tolist(),
    "ccmFN": df["ccmFN"].dropna().tolist(),
    "cox1": df["cox1"].dropna().tolist(),
    "rps3": df["rps3"].dropna().tolist(),
}

# Get the set of all species from all genes
all_species = set(species for species_list in species_names.values() for species in species_list)

# Fill in the output data list with species names and presence/absence
for species_name in all_species:
    row_data = {"Species": species_name}

    # Check each gene and add P (Presence) or A (Absent) based on species availability
    for gene_name in ["Atp1", "ccmFC", "ccmFN", "cox1", "rps3"]:
        if species_name in species_names[gene_name]:
            row_data[gene_name] = "P"
        else:
            row_data[gene_name] = "A"

    # Append the row data to the output data list
    output_data.append(row_data)

# Convert the list of dictionaries into a DataFrame
output_df = pd.DataFrame(output_data)

# Save the output DataFrame to a new CSV file
output_file = "GenesOutput.csv"
output_df.to_csv(output_file, index=False)

print("GenesOutput.csv created successfully!")
