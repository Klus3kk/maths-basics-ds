# 📊 Logistic Regression

Logistic regression is a statistical method used for binary classification. Unlike linear regression, which predicts continuous outcomes, logistic regression predicts the probability that a given input belongs to a certain class (e.g., 0 or 1, true or false).

## Logistic Function

The logistic function, also known as the sigmoid function, is used to map predicted values to probabilities. It produces an S-shaped curve, which is confined to the range [0, 1].

### Formula

The logistic function is defined as:

\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

Where \(z\) is the linear combination of input features (e.g., \(z = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_n\)).

### Example

For a model with one feature, the logistic function might look like this:

\[
\text{Probability} = \frac{1}{1 + e^{-(b_0 + b_1x_1)}}
\]

## Logistic Regression with Many Variables

Logistic regression can be extended to multiple variables (features) by including additional terms in the linear combination used in the logistic function.

### Example

For a model with two features \(x_1\) and \(x_2\), the logistic function becomes:

\[
\sigma(z) = \frac{1}{1 + e^{-(b_0 + b_1x_1 + b_2x_2)}}
\]

Where \(b_0\) is the intercept, and \(b_1\), \(b_2\) are the coefficients for each feature.

## Log-Odds (Logit)

The log-odds, or logit, is the logarithm of the odds of the probability of the event occurring versus it not occurring. Logistic regression models the log-odds as a linear combination of the input features.

### Formula

\[
\text{Log-Odds} = \log\left(\frac{P}{1-P}\right) = b_0 + b_1x_1 + \dots + b_nx_n
\]

Where \(P\) is the probability of the event occurring.

### Example

If \(P = 0.8\), the log-odds are:

\[
\log\left(\frac{0.8}{0.2}\right) = \log(4) = 1.386
\]

## R-Squared

In logistic regression, \(R^2\) is not as straightforward as in linear regression. However, pseudo-\(R^2\) values like McFadden's \(R^2\) are used to measure the goodness of fit.

### Formula (McFadden's \(R^2\))

\[
R^2 = 1 - \frac{\ln(L_{\text{full model}})}{\ln(L_{\text{null model}})}
\]

Where \(L_{\text{full model}}\) is the likelihood of the model with predictors and \(L_{\text{null model}}\) is the likelihood of the model without predictors.

## p-Values

In logistic regression, p-values are used to test the null hypothesis that a coefficient is equal to zero (no effect). Low p-values suggest that the predictor is statistically significant.

### Example

If the p-value for \(b_1\) is 0.03, we would reject the null hypothesis and conclude that \(x_1\) has a significant effect on the outcome at the 5% significance level.

## Confusion Matrix

A confusion matrix is a table used to evaluate the performance of a classification model. It shows the true positives, true negatives, false positives, and false negatives.

### Example

For a binary classifier:

|                | Predicted Positive | Predicted Negative |
|----------------|--------------------|--------------------|
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

## ROC Curve

The ROC (Receiver Operating Characteristic) curve is a graphical representation of the diagnostic ability of a binary classifier. It plots the True Positive Rate (sensitivity) against the False Positive Rate (1-specificity) at various threshold settings.

### Example

An ROC curve closer to the top-left corner indicates better performance. The Area Under the Curve (AUC) is often used as a summary measure of the ROC curve's performance.

