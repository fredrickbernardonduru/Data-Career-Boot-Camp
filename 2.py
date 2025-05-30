#import pandas as pd
import matplotlib.pyplot as plt
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
cumulative_returns_etf = pd.Series(index=dates)  # Initialize empty Series with dates as index
cumulative_returns_index = pd.Series(index=dates)  # Initialize empty Series with dates as index
cumulative_returns_index = pd.Series(index=dates)  # Initialize empty Series with dates as index

cumulative_returns_index = pd.Series(index=dates)  # Initialize empty Series with dates as index

cumulative_returns_etf[dates[0]] = 0.0  # Initial value
cumulative_returns_index[dates[0]] = 0.0  # Initial value

for i in range(1, len(dates)):
    cumulative_returns_etf[dates[i]] = cumulative_returns_etf[dates[i-1]] * (1 + 0.05)  # calculation for ETFs
    cumulative_returns_index[dates[i]] = cumulative_returns_index[dates[i-1]] * (1 + 0.03)  #calculation for indices

plt.figure(figsize=(12, 6))

# Plot cumulative returns for ETFs
plt.plot(cumulative_returns_etf.index, cumulative_returns_etf, label='ETFs', marker='o')

# Plot cumulative returns for indices
plt.plot(cumulative_returns_index.index, cumulative_returns_index, label='Indices', linestyle='--', marker='x')

plt.title('Cumulative Returns of 3x Leveraged ETFs vs Underlying Indices')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

