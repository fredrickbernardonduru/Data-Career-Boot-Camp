import numpy as np

# Sample data for illustration
np.random.seed(0)
sdg10_scores = np.random.normal(60, 20, 100)  
# Create histogram
plt.figure(figsize=(8, 5))
sns.histplot(sdg10_scores, bins=10, kde=True)
plt.title('Distribution of SDG10 Scores')
plt.xlabel('SDG10 Score')
plt.ylabel('Frequency')
plt.show()
