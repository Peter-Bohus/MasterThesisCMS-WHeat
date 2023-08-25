import scipy.stats as stats

# Observed counts based on your data
observed = [
    [91, 2],   # ATP1
    [85, 8],   # COX1
    [80, 13],  # CCMFN
    [80, 13],  # CCMFC
    [78, 15],  # RPS3
    [69, 24]   # ORF279
]

# Perform the chi-squared test
chi2, p, dof, expected = stats.chi2_contingency(observed)

# Print the results
print(f"Chi-squared: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
