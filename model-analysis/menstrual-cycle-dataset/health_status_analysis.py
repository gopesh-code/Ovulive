import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./datasets/FedCycleData071012 (2).csv")


# calculate the total number of women in the data set
n_women = df['ClientID'].nunique()

# create a new column to indicate whether a woman is reproductively healthy or not
# (for the purposes of this example, let's assume that women with cycle lengths between 26 and 34 days are considered reproductively healthy)
df['Healthy'] = (df['LengthofCycle'] >= 26) & (df['LengthofCycle'] <= 34)

# calculate the number of women who are reproductively healthy
n_healthy = df[df['Healthy'] == True]['ClientID'].nunique()

# calculate the proportion of women who are reproductively healthy
proportion = n_healthy / n_women

# print the results
print("Number of women:", n_women)
print("Number of reproductively healthy women:", n_healthy)
print("Proportion of reproductively healthy women: {:.2f}".format(proportion))

# visualize the results
plt.bar(["Healthy", "Not Healthy"], [n_healthy, n_women - n_healthy])
plt.xlabel("Health Status")
plt.ylabel("Number of Women")
plt.show()