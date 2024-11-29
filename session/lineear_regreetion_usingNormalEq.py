import numpy as np

# Sample data (replace with your actual data)
X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 5, 4])

# Add a column of ones to X to account for the intercept term
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add a column of ones to X

# Compute the parameters using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Print the parameters
theta_0, theta_1 = theta_best
print(f"Optimized parameters: theta_0 = {theta_0}, theta_1 = {theta_1}")

# Make predictions using the optimized parameters
y_pred = X_b.dot(theta_best)

# Plotting the data points and the regression line
import matplotlib.pyplot as plt

plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit using Normal Equation')
plt.legend()
plt.show()