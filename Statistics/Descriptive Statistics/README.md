# 📊 Descriptive Statistics

Descriptive statistics involve methods for summarizing and describing the important features of a dataset. It provides a way to present data in a meaningful and concise manner.

## Measures of Central Tendency

**1. Mean**  
The mean is the average value of a dataset, calculated as the sum of all data points divided by the number of data points.

### Example

For the dataset \[2, 4, 6, 8, 10\], the mean is:

\[
\text{Mean} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6
\]

**2. Median**  
The median is the middle value when the data points are ordered from smallest to largest. If there is an even number of data points, the median is the average of the two middle values.

### Example

For the dataset \[1, 3, 3, 6, 7, 8, 9\], the median is 6.  
For the dataset \[1, 2, 3, 4\], the median is \(\frac{2 + 3}{2} = 2.5\).

**3. Mode**  
The mode is the value that appears most frequently in a dataset. A dataset may have one mode, more than one mode, or no mode at all.

### Example

For the dataset \[4, 4, 5, 6, 6, 6, 7\], the mode is 6.

## Measures of Dispersion

**1. Range**  
The range is the difference between the highest and lowest values in a dataset.

### Example

For the dataset \[3, 7, 8, 5\], the range is:

\[
\text{Range} = 8 - 3 = 5
\]

**2. Variance**  
Variance measures how much the data points in a dataset vary from the mean. It’s calculated as the average of the squared differences between each data point and the mean.

### Example

For the dataset \[4, 8, 6, 5, 3\] with a mean of 5.2, the variance is:

\[
\text{Variance} = \frac{(4-5.2)^2 + (8-5.2)^2 + (6-5.2)^2 + (5-5.2)^2 + (3-5.2)^2}{5} = 3.7
\]

**3. Standard Deviation**  
The standard deviation is the square root of the variance and provides a measure of the dispersion of data points around the mean in the same units as the data.

### Example

For the variance calculated above (\(3.7\)), the standard deviation is:

\[
\text{Standard Deviation} = \sqrt{3.7} \approx 1.92
\]

## Measures of Relative Standing

**1. Percentiles**  
Percentiles divide the dataset into 100 equal parts. The nth percentile is the value below which n% of the data falls.

### Example

The 25th percentile (or first quartile) of the dataset \[1, 3, 5, 7, 9\] is 3.

**2. Quartiles**  
Quartiles divide the dataset into four equal parts. The first quartile (Q1) is the 25th percentile, the second quartile (Q2) is the median, and the third quartile (Q3) is the 75th percentile.

### Example

For the dataset \[1, 2, 3, 4, 5, 6, 7, 8, 9\]:

- Q1 (25th percentile) = 3
- Q2 (50th percentile or median) = 5
- Q3 (75th percentile) = 7

**3. Interquartile Range (IQR)**  
The IQR measures the spread of the middle 50% of the data and is calculated as the difference between the third quartile (Q3) and the first quartile (Q1).

### Example

For the dataset \[1, 3, 5, 7, 9\]:

\[
\text{IQR} = Q3 - Q1 = 7 - 3 = 4
\]

## Additional Statistical Concepts

**1. Variance and Standard Deviation**  
Variance and standard deviation are crucial for understanding the spread of data. Variance is the mean of the squared deviations from the mean, while the standard deviation is its square root.

### Example

Given a dataset \[2, 4, 4, 4, 5, 7, 9\], the variance and standard deviation can be calculated as discussed previously.

**2. Mode**  
The mode is the value that appears most frequently in the dataset.

### Example

For the dataset \[1, 2, 2, 3, 4, 5\], the mode is 2.

**3. Normal Distribution**  
The normal distribution, also known as the Gaussian distribution, is a continuous probability distribution characterized by its bell-shaped curve. It’s defined by its mean (\(\mu\)) and standard deviation (\(\sigma\)).

### Example

In a normal distribution with a mean of 0 and a standard deviation of 1 (the standard normal distribution), about 68% of the data falls within one standard deviation from the mean.

**4. Probability Density Function (PDF)**  
The PDF describes the likelihood of a random variable taking on a particular value. For a normal distribution, the PDF is given by:

\[
f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{ -\frac{(x - \mu)^2}{2 \sigma^2} }
\]

### Example

For a normal distribution with \(\mu = 0\) and \(\sigma = 1\), the PDF evaluates the probability density at any value of \(x\).

**5. Cumulative Distribution Function (CDF)**  
The CDF describes the probability that a random variable is less than or equal to a certain value. It’s the integral of the PDF from negative infinity to that value.

### Example

For a normal distribution, the CDF gives the probability that a value is below a certain threshold.

**6. Standardization (Z-Score)**  
Standardization converts a normal distribution to the standard normal distribution. The Z-score represents the number of standard deviations a data point is from the mean.

\[
Z = \frac{X - \mu}{\sigma}
\]

### Example

If \(X = 70\), \(\mu = 65\), and \(\sigma = 5\), the Z-score is:

\[
Z = \frac{70 - 65}{5} = 1
\]
