# Build mini linear regression using NumPy only.

# Formula:

# y=XW+b

# Implement gradient descent manually.

# This single project will:

# Teach matrix multiplication
# Teach broadcasting
# Teach gradients
# Teach optimization

# What is Linear Regression? only points
# Linear regression is a statistical method used to model the relationship between a dependent variable (y) and one or more independent variables (X). The goal of linear regression is to find the best-fitting line (or hyperplane in higher dimensions) that describes the relationship between the variables. The equation of a linear regression model is given by:
# y = XW + b
# where:
# y is the dependent variable (target variable) 
# X is the independent variable(s) (feature(s))
# W is the weight(s) (coefficient(s)) that represent the strength of the relationship between the independent variable(s) and the dependent variable
# b is the bias (intercept) that represents the value of y when all independent variables are zero 

# Gradient Descent
# Gradient descent is an optimization algorithm used to minimize the cost function of a machine learning model. In the context of linear regression, the cost function is typically the mean squared error (MSE) between the predicted values and the actual values. The goal of gradient descent is to find the optimal values of W and b that minimize the cost function. The update rules for W and b in gradient descent are given by:
# W = W - learning_rate * dW
# b = b - learning_rate * db    
# where:
# learning_rate is a hyperparameter that controls the step size of the updates
# dW is the gradient of the cost function with respect to W
# db is the gradient of the cost function with respect to b 

# Implementing Linear Regression using NumPy
import numpy as np
# Generate synthetic data
X = np.random.rand(100, 1) # 100 samples, 1 feature
true_W = 2.5
true_b = 1.0
y = true_W * X + true_b + np.random.randn(100, 1) * 0.5 # Add some noise
# Initialize parameters
W = np.random.rand(1, 1) # Random initial weight
b = np.random.rand(1) # Random initial bias

# Hyperparameters
learning_rate = 0.01
num_iterations = 1000

# Gradient Descent
for i in range(num_iterations):
    # Forward pass
    y_pred = X @ W + b # Predicted values
    # Compute cost (mean squared error)
    cost = np.mean((y_pred - y) ** 2)
    # Compute gradients
    dW = (2 / X.shape[0]) * X.T @ (y_pred - y) # Gradient with respect to W
    db = (2 / X.shape[0]) * np.sum(y_pred - y) # Gradient with respect to b
    # Update parameters
    W -= learning_rate * dW
    b -= learning_rate * db
    # Print cost every 100 iterations
    if i % 100 == 0:
        print(f"Iteration {i}, Cost: {cost}")   

# Final parameters
print(f"Estimated W: {W[0][0]}, Estimated b: {b[0]}")
print(f"True W: {true_W}, True b: {true_b}")
print(f"Final Cost: {cost}")
print(f"Predicted values: {y_pred[:5].flatten()}, Actual values: {y[:5].flatten()}")
