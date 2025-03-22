import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([1, 2, 4, 4, 6])

# linear best fit: A = ((X^T * X) ^ -1) * X^T * y

# matrix A with ones on left side and x values on right
X = np.array([np.ones(len(x)), x]).T

# transpose X
X_transpose_X = X.T

# (X^T * X) ^ -1
X_T_X_inv = np.linalg.inv(X_transpose_X @ X)

# X^T * y
X_T_y = X.T @ y

# A = ((X^T * X) ^ -1) * X^T * y
A = X_T_X_inv @ X_T_y

y_intercept, slope = A

y_fit = slope * x + y_intercept


x_predict = 2.5
y_fit_predict = slope * x_predict + y_intercept
y_2_predict = 0.5 + x_predict
y_3_predict = 1.2 * x_predict

# plot points and linear regression line 
plt.scatter(x, y, color='k', label='data points')
plt.scatter(x_predict, y_fit_predict, color='orange', label=f'x = 2.5, y-predicted = {y_fit_predict:.2f}')
plt.plot(x, y_fit, color='g', label = f'y = {slope:.2f}x + {y_intercept:.2f}')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend()
plt.show()





