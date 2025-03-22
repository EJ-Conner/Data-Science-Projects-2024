import numpy as np
import matplotlib.pyplot as plt

#calculates ols taking in the sqr ft and prices as parameters
def ordinary_least_sqrs(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    slope = (sum((x-x_mean) * (y-y_mean))) / (sum((x - x_mean) ** 2))
    intercept = y_mean - slope * x_mean
    return slope, intercept

#Calculate ordinary least squares using matrix algebra algorithm
def ord_least_sqrs_matrix(x, y):
    X = np.array([np.ones(len(x)), x]).T # transposed matrix of ones with x values to be vertical

    # transpose X
    X_transpose_X = X.T                          # transpose X
    X_T_X_inv = np.linalg.inv(X_transpose_X @ X) # (X^T * X) ^ -1
    X_T_y = X.T @ y                              # X^T * y
    A = X_T_X_inv @ X_T_y                        # A = ((X^T * X)^-1) * X^T * y
    intercept, slope = A
    return slope, intercept


# replaces np.sum
def sum(iterable):
    total = 0
    for i in iterable:
        total += i
    return total

# calc Sum Squared errors
def calc_SSE(x, y, slope, intercept):
    y_predict = slope * x + intercept
    SSE = 0
    sum((y-y_predict) ** 2)
    return SSE

# calc correlation coefficient
def calc_corr_coeff(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    corr_coeff = sum((x-x_mean) * (y-y_mean)) / (sum((x-x_mean) ** 2) * sum((y-y_mean) ** 2)) ** (1/2)
    return corr_coeff

sqr_ft = np.array([250, 500, 1000, 2000, 3000, 4000], dtype=np.float64)
prices = np.array([50000, 100000, 200000, 400000, 600000, 800000], dtype=np.float64)

#noise
randomNumbers = np.random.normal(0.0, 1.0, 6)
noise = randomNumbers * 30000
noisy_prices = prices + noise

# calc regression with and w/o noise
slope_reg, intercept_reg = ordinary_least_sqrs(sqr_ft, prices)
slope_reg_noise, intercept_reg_noise = ordinary_least_sqrs(sqr_ft, noisy_prices)


# calc regression with and w/o noise using MAT algebra algorithm
slope_reg_mat, intercept_reg_mat = ord_least_sqrs_matrix(sqr_ft, prices)
slope_reg_mat_noise, intercept_reg_mat_noise = ord_least_sqrs_matrix(sqr_ft, noisy_prices)


# calc SSE with and w/o noise
sse = calc_SSE(sqr_ft, prices, slope_reg, intercept_reg)
sse_noise = calc_SSE(sqr_ft, noisy_prices, slope_reg_noise, intercept_reg_noise)


# calc SSE with and w/o noise MAT
sse_mat = calc_SSE(sqr_ft, prices, slope_reg_mat, intercept_reg_mat)
sse_mat_noise = calc_SSE(sqr_ft, noisy_prices, slope_reg_mat_noise, intercept_reg_mat_noise)


# calc correlation coefficient w and w/o noise
corr_coeff = calc_corr_coeff(sqr_ft, prices)
corr_coeff_noise = calc_corr_coeff(sqr_ft, noisy_prices)


# predict house prices for given sqr ft
predict_sqr_ft = np.array([200, 1250, 2710, 5100], dtype=np.float64)
pred_prices = slope_reg * predict_sqr_ft + intercept_reg
pred_prices_noise = slope_reg_noise * predict_sqr_ft + intercept_reg_noise


# predict house prices for given sqr ft using MAT
predict_sqr_ft_mat = np.array([200, 1250, 2710, 5100], dtype=np.float64)
pred_prices_mat = slope_reg_mat * predict_sqr_ft_mat + intercept_reg_mat
pred_prices_noise_mat = slope_reg_noise * predict_sqr_ft_mat + intercept_reg_mat_noise


print(f"Regression Line parameters: Slope = {slope_reg}, intercept = {intercept_reg}")
print(f"Regression Line parameters with noise: Slope = {slope_reg_noise}, intercept = {intercept_reg_noise}")
print(f"Predicted house prices for the following sqr ft: 200, 1250, 2710, 5100\nPrices: {pred_prices}\nPrices with noise: {pred_prices_noise}")

print("\nMatrix Algorithm Comparison: \n")

print(f"Regression Line parameters: Slope = {slope_reg_mat}, intercept = {intercept_reg_mat}")
print(f"Regression Line parameters with noise: Slope = {slope_reg_mat_noise}, intercept = {intercept_reg_mat_noise}")
print(f"Predicted house prices for the following sqr ft: 200, 1250, 2710, 5100\nPrices: {pred_prices_mat}\nPrices with noise: {pred_prices_noise_mat}")


# data before noise
plt.scatter(sqr_ft, prices, color='green', label='Before Noise')
plt.plot(sqr_ft, slope_reg * sqr_ft + intercept_reg, color='green', label='Regression Line Before Noise')

# data after noise
plt.scatter(sqr_ft, noisy_prices, color='r', label='After Noise')
plt.plot(sqr_ft, slope_reg_noise * sqr_ft + intercept_reg_noise, color='r', label='Regression Line After Noise')

plt.title('Linear Regression with and w/o Noise')
plt.xlabel('Square Feet')
plt.ylabel('Prices')
plt.legend()
plt.show()
