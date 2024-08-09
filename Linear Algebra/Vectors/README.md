# 🧮 Vectors

Vectors are mathematical objects that have both magnitude and direction. They are fundamental in linear algebra and are used to represent quantities like force, velocity, and more.

## Adding Vectors

Vector addition combines two vectors to form a new vector. The addition is performed by adding corresponding components of the vectors.

### Example

Given vectors \(\mathbf{a} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}\) and \(\mathbf{b} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}\), their sum \(\mathbf{c} = \mathbf{a} + \mathbf{b}\) is:

\[
\mathbf{c} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 4 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \end{bmatrix}
\]

## Scaling Vectors

Scaling a vector involves multiplying it by a scalar (a real number), which changes the vector's magnitude without altering its direction.

### Example

Given vector \(\mathbf{a} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}\) and scalar \(k = 2\), the scaled vector is:

\[
k \cdot \mathbf{a} = 2 \times \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 6 \\ 8 \end{bmatrix}
\]

## Span and Linear Dependence

The span of a set of vectors is the collection of all possible linear combinations of those vectors. Vectors are linearly dependent if one vector in the set can be written as a linear combination of the others.

### Example

For vectors \(\mathbf{a} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}\) and \(\mathbf{b} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}\), \(\mathbf{b}\) is a linear combination of \(\mathbf{a}\) since:

\[
\mathbf{b} = 2 \cdot \mathbf{a}
\]
