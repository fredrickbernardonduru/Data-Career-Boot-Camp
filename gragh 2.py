import pandas as pd

# Sample data for illustration
data = {'Population Level': ['Small', 'Medium', 'Large'],
        'Mean SDG10 Score': [63.6, 89.5, None]}  # Mean SDG10 scores for different population levels
df = pd.DataFrame(data)

# Create scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Population Level', y='Mean SDG10 Score', data=df, s=100)
plt.title('Mean SDG10 Scores vs. Population Level')
plt.xlabel('Population Level')
plt.ylabel('Mean SDG10 Score')
plt.show()
