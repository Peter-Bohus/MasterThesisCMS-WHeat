import scipy.stats as stats

# Data for genes associated with CMS
cms_pi = [0.06692, 0.00209, 0.02386, 0.00303, 0.02386, 0.31568]

# Data for genes not associated with CMS
non_cms_pi = [0.13946, 0.15149, 0.01538, 0.00212, 0.01245, 0.00193]

# Add a small constant to avoid zero values
epsilon = 1e-6
cms_pi = [pi + epsilon for pi in cms_pi]
non_cms_pi = [pi + epsilon for pi in non_cms_pi]

# Perform Fisher's exact test
odds_ratio, p_value = stats.fisher_exact([[len(cms_pi), len(non_cms_pi)], [sum(cms_pi), sum(non_cms_pi)]])

# Print the results
print(f"Odds Ratio: {odds_ratio}")
print(f"P-value: {p_value}")

# Interpret the results
if p_value < 0.05:
    print("The difference in nucleotide diversity is statistically significant.")
else:
    print("There is no statistically significant difference in nucleotide diversity.")
