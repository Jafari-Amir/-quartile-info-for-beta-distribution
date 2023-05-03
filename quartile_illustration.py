import matplotlib.pyplot as plt
import numpy as np
#random data
data = np.random.normal(size=100)
# cal the quartiles and mean
q1, q2, q3 = np.percentile(data, [25, 50, 75])
mean = np.mean(data)
# make a box plot

fig, ax = plt.subplots(figsize=(5, 2.8))
ax.boxplot(data, vert=False)
# vertical lines for the quartiles and label them
ax.axvline(q1, color='r', linestyle='--', label='Q1')
ax.axvline(q2, color='g', linestyle='-', label='Q2 (Median)')
ax.axvline(q3, color='b', linestyle='--', label='Q3')
# a horizontal line for the mean
ax.axvline(mean, color='m', linestyle='-', label='Mean')
ax.set_xlabel('Value')
ax.legend()

plt.savefig('simple_.png', dpi=300)
plt.show()
