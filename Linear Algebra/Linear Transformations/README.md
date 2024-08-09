# 🧮 Linear Transformations

Linear transformations are functions that map vectors to vectors in a way that preserves vector addition and scalar multiplication. They can be represented by matrices.

## Basis Vectors (Matrices)

Basis vectors are a set of vectors that span a vector space. In matrix form, they define the coordinate system in which any vector in the space can be represented.

### Example

In \(\mathbb{R}^2\), the standard basis vectors are:

\[
\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
\]

## Matrix-Vector Multiplication

Matrix-vector multiplication applies a linear transformation to a vector, resulting in a new vector.

### Example

Given matrix \(\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) and vector \(\mathbf{x} = \begin{bmatrix} 5 \\ 6 \end{bmatrix}\), the product is:

\[
\mathbf{A} \cdot \mathbf{x} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \cdot \begin{bmatrix} 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 17 \\ 39 \end{bmatrix}
\]

## Matrix Multiplication

Matrix multiplication involves multiplying two matrices together to produce a new matrix. It’s a fundamental operation in linear transformations.

### Example

Given matrices \(\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) and \(\mathbf{B} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}\), their product \(\mathbf{C} = \mathbf{A} \cdot \mathbf{B}\) is:

\[
\mathbf{C} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \cdot \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
\]

## Determinants

The determinant is a scalar value that can be computed from the elements of a square matrix. It provides important information about the matrix, such as whether it is invertible.

### Example

The determinant of matrix \(\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) is:

\[
\text{det}(\mathbf{A}) = 1 \times 4 - 2 \times 3 = 4 - 6 = -2
\]
