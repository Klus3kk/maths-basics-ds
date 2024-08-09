# 🧮 Different Types of Matrices

Matrices are rectangular arrays of numbers, symbols, or expressions arranged in rows and columns. They are used to represent linear transformations and systems of linear equations.

## Square Matrix

A square matrix has the same number of rows and columns. It is the basis for many matrix operations, including finding the determinant and inverse.

### Example

\[
\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\]

## Identity Matrix

An identity matrix is a square matrix with ones on the diagonal and zeros elsewhere. It acts as the multiplicative identity in matrix multiplication.

### Example

\[
\mathbf{I} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\]

## Inverse Matrix

The inverse of a matrix \(\mathbf{A}\) is a matrix \(\mathbf{A}^{-1}\) such that:

\[
\mathbf{A} \cdot \mathbf{A}^{-1} = \mathbf{I}
\]

### Example

The inverse of \(\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) is:

\[
\mathbf{A}^{-1} = \frac{1}{-2} \begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}
\]

## Diagonal Matrix

A diagonal matrix is a square matrix where all the elements outside the main diagonal are zero.

### Example

\[
\mathbf{D} = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}
\]

## Triangular Matrix

A triangular matrix is a square matrix where all the elements above or below the main diagonal are zero. It can be either upper triangular or lower triangular.

### Example

Upper Triangular:

\[
\mathbf{U} = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix}
\]

Lower Triangular:

\[
\mathbf{L} = \begin{bmatrix} 4 & 0 \\ 2 & 5 \end{bmatrix}
\]

## Sparse Matrix

A sparse matrix is a matrix in which most of the elements are zero. They are used in computational applications to save memory.

### Example

\[
\mathbf{S} = \begin{bmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 7 & 0 & 0 \end{bmatrix}
\]
