import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta
# random data
x = np.linspace(0, 1, 1000)
y1 = beta.pdf(x, 2, 8)
y2 = beta.pdf(x, 5, 5)
y3 = beta.pdf(x, 8, 2)
# calculate the quartiles for each dataset
q1_1, q2_1, q3_1 = np.percentile(y1, [25, 50, 75])
q1_2, q2_2, q3_2 = np.percentile(y2, [25, 50, 75])
q1_3, q2_3, q3_3 = np.percentile(y3, [25, 50, 75])

# make the first plot
fig, ax = plt.subplots()
ax.plot(x, y1, label='Beta(2,8)')

# vertical lines for the quartiles and label them
ax.axhline(q1_1, color='r', linestyle='--', label='Q1')
ax.axhline(q2_1, color='g', linestyle='-', label='Q2 (Median)')
ax.axhline(q3_1, color='b', linestyle='--', label='Q3')

# set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Density')
ax.set_title('Beta(2,8)')
ax.legend()

# Create the second plot
fig, ax = plt.subplots()
ax.plot(x, y2, label='Beta(5,5)')

#  vertical lines for the quartiles and label them
ax.axhline(q1_2, color='r', linestyle='--', label='Q1')
ax.axhline(q2_2, color='g', linestyle='-', label='Q2 (Median)')
ax.axhline(q3_2, color='b', linestyle='--', label='Q3')

# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Density')
ax.set_title('Beta(5,5)')
ax.legend()

# third plot
fig, ax = plt.subplots()
ax.plot(x, y3, label='Beta(8,2)')

# vertical lines for the quartiles and label them
ax.axhline(q1_3, color='r', linestyle='--', label='Q1')
ax.axhline(q2_3, color='g', linestyle='-', label='Q2 (Median)')
ax.axhline(q3_3, color='b', linestyle='--', label='Q3')

# set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Density')
ax.set_title('Beta(8,2)')
ax.legend()
plt.show()