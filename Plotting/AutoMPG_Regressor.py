import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

auto_mpg_df = pd.read_csv('auto-mpg.csv')


row, col = auto_mpg_df.shape
print('Rows in df:', row)
print('Column in df:', col)

auto_mpg_df = auto_mpg_df.replace('?', np.nan)

auto_mpg_df = auto_mpg_df.dropna()

auto_mpg_df = auto_mpg_df.reset_index(drop=True)

row, col = auto_mpg_df.shape
print('\n\nRows in df:', row)
print('Column in df:', col)


x = np.array(auto_mpg_df["weight"])
y = np.array(auto_mpg_df["mpg"])

slope, intercept, r, p, std_error = stats.linregress(x, y)

model = slope * x + intercept

x_pred = np.arange(1500, 5500, 500)

model_pred = slope * x_pred + intercept

plt.scatter(x, y, color='blue', label='Training Data Points')
plt.scatter(x_pred, model_pred, color='orange', label='test data points')
plt.plot(x, model, color='red', label='OLS' )
plt.title(f"Linear Regression with OLS; slope: {slope:.2f}, y-intercept: {intercept:.2f}, r: {r:.2f}")
plt.grid()
plt.xlabel('weight')
plt.ylabel('mpg')
plt.legend(loc='upper right')
plt.show()