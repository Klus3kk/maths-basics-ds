# 📉 Basic Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It aims to find the best-fitting line through the data points that minimizes the error in predictions.

## Residuals and Error Squares

Residuals are the differences between the observed values and the values predicted by the linear model. The sum of the squared residuals (error squares) is minimized in linear regression to find the best-fit line.

### Example

Given observed values \(y_i\) and predicted values \(\hat{y}_i\):

\[
\text{Residual} = y_i - \hat{y}_i
\]

The sum of squared errors (SSE) is:

\[
\text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

## Finding the Best-Fit Line

The best-fit line is found by minimizing the sum of squared errors (SSE). This can be done using calculus to derive the line equation in the form \(y = mx + b\), where \(m\) is the slope and \(b\) is the intercept.

### Example

The slope \(m\) and intercept \(b\) are calculated as:

\[
m = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}
\]

\[
b = \frac{(\sum y) - m(\sum x)}{n}
\]

## Gradient Descent Method

Gradient Descent is an optimization algorithm used to minimize the error function by iteratively adjusting the parameters of the model (slope and intercept) to find the best-fit line.

### Steps of Gradient Descent

1. **Initialize Parameters**: Start with an initial guess for the slope and intercept.
2. **Calculate Gradient**: Compute the partial derivatives of the error function with respect to the slope and intercept.
3. **Update Parameters**: Adjust the slope and intercept in the direction opposite to the gradient to reduce the error.
4. **Repeat**: Continue until the error converges to a minimum.

### Example

For a simple linear regression model, the updates for the slope \(m\) and intercept \(b\) are:

\[
m := m - \alpha \frac{\partial}{\partial m} \text{SSE}
\]

\[
b := b - \alpha \frac{\partial}{\partial b} \text{SSE}
\]

Where \(\alpha\) is the learning rate.

## Correlation Coefficient

The correlation coefficient (denoted as \(r\)) measures the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, where:

- \(r = 1\): Perfect positive correlation.
- \(r = -1\): Perfect negative correlation.
- \(r = 0\): No correlation.

### Example

Given variables \(X\) and \(Y\), the correlation coefficient is calculated as:

\[
r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}
\]

## Coefficient of Determination

The coefficient of determination (denoted as \(R^2\)) represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s). It ranges from 0 to 1, where:

- \(R^2 = 1\): The model explains all the variability in the response data.
- \(R^2 = 0\): The model explains none of the variability in the response data.

### Example

The \(R^2\) value is calculated as:

\[
R^2 = 1 - \frac{\text{SSE}}{\text{SST}}
\]

Where:

- SSE: Sum of squared errors (residual sum of squares).
- SST: Total sum of squares (variance in the observed data).
