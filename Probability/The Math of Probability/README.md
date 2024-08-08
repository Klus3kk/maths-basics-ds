# 🔢 The Math of Probability

This section covers the mathematical foundations of probability, including joint, alternative, conditional probabilities, and important distributions.

## Joint Probability (AND)

Joint probability, denoted \( P(A \text{ AND } B) \), is the probability that two events \( A \) and \( B \) both occur.

### Example

If you roll two dice, the probability that both show a "1" is:

\[
P(A \text{ AND } B) = P(A) \times P(B) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}
\]

## Alternative Probability (OR)

Alternative probability, denoted \( P(A \text{ OR } B) \), is the probability that at least one of the events \( A \) or \( B \) occurs.

### Example

If you roll a die, the probability of getting a "2" or a "5" is:

\[
P(A \text{ OR } B) = P(A) + P(B) - P(A \text{ AND } B)
\]
\[
P(2 \text{ OR } 5) = \frac{1}{6} + \frac{1}{6} - 0 = \frac{2}{6} = \frac{1}{3}
\]

## Conditional Probability (IF)

Conditional probability, denoted \( P(A \mid B) \), is the probability that event \( A \) occurs given that event \( B \) has already occurred.

### Example

If there is a 30% chance of rain, but you know it’s cloudy (which makes rain more likely), the conditional probability of rain given that it’s cloudy might be 50%.

## Bayes' Theorem

Bayes' Theorem describes the probability of an event, based on prior knowledge of conditions that might be related to the event. It's written as:

\[
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
\]

### Example

If a medical test is 99% accurate and 1 in 1000 people have a disease, Bayes' Theorem can be used to calculate the probability that a person actually has the disease given a positive test result.

## Binomial Distribution

The binomial distribution represents the number of successes in a fixed number of independent Bernoulli trials (yes/no experiments), each with the same probability of success.

### Example

The probability of getting exactly 3 heads in 5 flips of a fair coin is calculated using the binomial distribution formula.

\[
P(X = 3) = \binom{5}{3} \cdot (0.5)^3 \cdot (0.5)^{2} = 10 \cdot 0.125 \cdot 0.25 = 0.3125
\]

## Beta Distribution

The Beta distribution is a continuous probability distribution that is often used to model the distribution of probabilities. It is defined on the interval [0, 1] and parametrized by two positive shape parameters, typically denoted as \( \alpha \) and \( \beta \).

### Example

If you have observed 3 successes and 2 failures, the Beta distribution \( \text{Beta}(4, 3) \) can model the uncertainty in the probability of success.
