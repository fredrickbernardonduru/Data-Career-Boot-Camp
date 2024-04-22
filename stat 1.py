import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for illustration
regions = ['Arab', 'Non-Arab']
sdg10_scores = [80.0, 55.8]  

# Create bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x=regions, y=sdg10_scores)
plt.title('Mean SDG10 Scores by Region')
plt.xlabel('Region')
plt.ylabel('Mean SDG10 Score')
plt.show()
