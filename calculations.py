import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Sample data for demonstration
data = {
    'Country': ['Country1', 'Country2', 'Country3', 'Country4'],
    'SDG10 Score': [85, 90, 75, 80],
    'HD Level': ['High', 'Medium', 'Low', 'High'],
    'Population Level': ['Large', 'Small', 'Medium', 'Medium']
}
df = pd.DataFrame(data)

# Calculate mean SDG10 score
mean_score = df['SDG10 Score'].mean()

# Calculate frequency and percentage of HD Level
hd_level_counts = df['HD Level'].value_counts()
hd_level_freq = hd_level_counts / len(df) * 100

# Calculate frequency and percentage of Population Level
pop_level_counts = df['Population Level'].value_counts()
pop_level_freq = pop_level_counts / len(df) * 100

# Calculate standard deviation of SDG10 scores
sd_score = df['SDG10 Score'].std()

# Calculate t-test statistic and p-value
group1 = df[df['HD Level'] == 'High']['SDG10 Score']
group2 = df[df['HD Level'] == 'Medium']['SDG10 Score']
t_stat, p_value = ttest_ind(group1, group2)

# Print results
print(f"Mean SDG10 Score: {mean_score}")
print(f"Frequency of HD Level:\n{hd_level_counts}\nPercentage:\n{hd_level_freq}")
print(f"Frequency of Population Level:\n{pop_level_counts}\nPercentage:\n{pop_level_freq}")
print(f"Standard Deviation of SDG10 Score: {sd_score}")
print(f"T-test Statistic: {t_stat}, p-value: {p_value}")
