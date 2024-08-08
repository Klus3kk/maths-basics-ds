# 📈 Statistical Inference

Statistical inference involves drawing conclusions about a population based on a sample of data. It uses probability theory to estimate population parameters and test hypotheses.

## Central Limit Theorem (CLT)

The Central Limit Theorem (CLT) states that the distribution of the sample mean approaches a normal distribution as the sample size becomes large, regardless of the original distribution of the population.

### Key Points

- **Applicability**: The CLT applies to sample means when the sample size is sufficiently large (typically \(n > 30\)).
- **Distribution**: For large sample sizes, the sample mean distribution is approximately normal, even if the population distribution is not.

### Example

If you take multiple samples of size 50 from a population with a non-normal distribution, the distribution of the sample means will approximate a normal distribution.

## Confidence Intervals

A confidence interval provides a range of values within which a population parameter is likely to fall, with a certain level of confidence. Common confidence levels are 90%, 95%, and 99%.

### Key Points

- **Point Estimate**: The sample statistic (e.g., sample mean) used to estimate the population parameter.
- **Margin of Error**: The amount added and subtracted from the point estimate to create the interval. It is calculated based on the standard error and the critical value from the standard normal distribution (or t-distribution).

### Example

For a sample mean of 50 and a standard error of 2 with a 95% confidence level, the confidence interval can be calculated using the critical value (approximately 1.96 for 95% confidence) as follows:

\[
\text{Confidence Interval} = \text{Mean} \pm (\text{Critical Value} \times \text{Standard Error})
\]

\[
\text{Confidence Interval} = 50 \pm (1.96 \times 2) = [46.08, 53.92]
\]

This means we are 95% confident that the true population mean lies within this interval.

## Conclusion

Statistical inference allows researchers to make informed conclusions about populations from sample data. The Central Limit Theorem ensures that sample means will be normally distributed for large samples, while confidence intervals provide a range within which the true population parameters are likely to fall.
