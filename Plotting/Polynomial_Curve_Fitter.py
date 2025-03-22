import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, -1, 0, 1, 2], dtype=np.float64)
y = np.array([3, 5, 1, 4, 10], dtype=np.float64)

# A * X = B
# X = A^-1 * B
# in our case B = y

# degree will be n - 1
degree = len(x) - 1

# create degree n matrix 
A = np.zeros((len(x), degree + 1))
for i in range(degree + 1):
    A[:, i] = x ** (degree - i)

print(A)

A_T = A.T #transpose
#A_T_A_inv = np.linalg.inv(np.matmul(A_T, A))
A_T_A_inv = np.linalg.inv(A_T @ A)
A_T_y = A.T @ y
coefficients = A_T_A_inv @ A_T_y
a, b, c, d, e = coefficients

print(f"Polynomial Coefficients: a = {a:.3f}, b = {b:.3f}, c = {c:.3f}, d = {d:.3f}, e = {e:.3f}")


polynomial_x = np.arange(-3, 2.7, 0.6)
polynomial_y = 0
for i, j in enumerate(coefficients):
    polynomial_y += j * (polynomial_x ** (degree - i))

plt.scatter(x, y, color='green', label='Given Points')
plt.plot(polynomial_x, polynomial_y, color='red', label='Fitted Polynomial')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Polynomial Curve Fitting')
plt.legend()
plt.show()