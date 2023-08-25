import scipy.stats as stats

# Observed counts for genes associated with CMS (CCMFC, RPS3, ORF279)
cms_genes_present = 80 + 80 + 69  # CCMFC + RPS3 + ORF279
cms_genes_absent = 13 + 13 + 24   # CCMFC + RPS3 + ORF279

# Observed counts for genes not associated with CMS (ATP1, COX1, CCMFN)
non_cms_genes_present = 91 + 85 + 80  # ATP1 + COX1 + CCMFN
non_cms_genes_absent = 2 + 8 + 13  # ATP1 + COX1 + CCMFN

# Create a 2x2 contingency table
observed_table = [[cms_genes_present, non_cms_genes_present],
                  [cms_genes_absent, non_cms_genes_absent]]

# Perform Fisher's exact test
odds_ratio, p = stats.fisher_exact(observed_table)

# Print the results
print(f"Odds Ratio: {odds_ratio}")
print(f"P-value: {p}")
