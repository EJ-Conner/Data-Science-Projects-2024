import csv
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

grades_df = pd.read_csv('grades.csv', names=['Hours Studied', 'Grades'])

x = np.array(grades_df['Hours Studied'])
y = np.array(grades_df['Grades'])

slope, intercept, r, p, std_err = stats.linregress(x, y)
model = intercept + slope*x


y_pred = slope* 10.5 + intercept

x_pred = x.reshape(-1, 1)

print(grades_df)
print("Slope: ", slope)
print("Y-intercept: ", intercept)
print("r: ", r)
print("p value: ", p)
print("Standard error: ", std_err)


plt.scatter(x, y, color='b', label = 'data points')
plt.scatter(10.5, y_pred, color='orange', label=f'x = 10.5, y(pred) = {y_pred:.2f}')
plt.plot(x, model, color='g', label=f'y = {slope:.1f}x + {intercept:.1f}')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend()
plt.show()


