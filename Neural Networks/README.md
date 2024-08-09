# 🤖 Neural Networks

Neural networks are a class of machine learning algorithms inspired by the human brain's structure and function. They consist of interconnected layers of nodes (neurons) that process and learn from data.

## When to Use Neural Networks?

Neural networks are particularly useful when dealing with complex patterns in large datasets, especially in tasks like image recognition, natural language processing, and time series forecasting. They are preferred when:

- The problem involves high-dimensional data with intricate relationships.
- The data has a non-linear pattern that simpler models can't capture.
- Large amounts of labeled data are available for training.

## Activation Functions

Activation functions determine whether a neuron should be activated or not, introducing non-linearity into the network. This non-linearity allows neural networks to model complex patterns.

### Common Activation Functions:

- **Sigmoid**: \( \sigma(z) = \frac{1}{1 + e^{-z}} \)
  - Output range: (0, 1)
  - Often used in binary classification tasks.

- **ReLU (Rectified Linear Unit)**: \( \text{ReLU}(z) = \max(0, z) \)
  - Output range: \([0, \infty)\)
  - Popular in hidden layers for its simplicity and efficiency.

- **Tanh (Hyperbolic Tangent)**: \( \text{tanh}(z) = \frac{2}{1 + e^{-2z}} - 1 \)
  - Output range: (-1, 1)
  - Used when the output needs to be centered around zero.

### Example

In a neural network, each neuron applies an activation function to the weighted sum of its inputs:

\[
\text{Output} = \sigma(w_1x_1 + w_2x_2 + \dots + b)
\]

Where \(\sigma\) is the activation function, \(w_i\) are the weights, \(x_i\) are the inputs, and \(b\) is the bias.

## Feed-Forward

Feed-forward is the process by which inputs are passed through the layers of the network to generate an output. Each layer receives inputs from the previous layer, processes them using weights, biases, and activation functions, and sends the result to the next layer.

### Example

For a simple neural network with one hidden layer:

1. **Input Layer**: Receives raw input data.
2. **Hidden Layer**: Applies weights, adds biases, and passes the result through an activation function.
3. **Output Layer**: Produces the final prediction.

Mathematically:

\[
\text{Hidden Layer Output} = \sigma(W \cdot \text{Input} + b)
\]

\[
\text{Final Output} = \sigma(W' \cdot \text{Hidden Layer Output} + b')
\]

## Backpropagation

Backpropagation is the learning algorithm used to train neural networks. It adjusts the weights and biases of the network to minimize the difference between the predicted and actual outputs.

### How Backpropagation Works:

1. **Forward Pass**: Calculate the output using current weights and biases.
2. **Calculate Error**: Determine the difference between the predicted and actual outputs (usually using a loss function like Mean Squared Error).
3. **Backward Pass**: Propagate the error backward through the network, calculating gradients for each weight and bias.
4. **Update Weights**: Adjust the weights and biases to reduce the error using an optimization method like Gradient Descent.

### Example

In a simple network, the weight update rule might be:

\[
w := w - \alpha \cdot \frac{\partial \text{Loss}}{\partial w}
\]

Where \(w\) is the weight, \(\alpha\) is the learning rate, and \(\frac{\partial \text{Loss}}{\partial w}\) is the gradient of the loss function with respect to \(w\).
