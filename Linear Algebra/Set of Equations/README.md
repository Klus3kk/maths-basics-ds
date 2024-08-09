# 🧮 Set of Equations with Matrices

Systems of linear equations can be represented and solved using matrices. This approach is particularly useful for solving large systems of equations efficiently.

## Representing a System of Equations

A system of linear equations can be written in matrix form as \(\mathbf{A} \cdot \mathbf{x} = \mathbf{b}\), where \(\mathbf{A}\) is the coefficient matrix, \(\mathbf{x}\) is the vector of variables, and \(\mathbf{b}\) is the result vector.

### Example

Consider the system:

\[
\begin{aligned}
2x + 3y &= 5 \\
4x + 6y &= 10
\end{aligned}
\]

This can be written in matrix form as:

\[
\mathbf{A} \cdot \mathbf{x} = \mathbf{b}
\]

\[
\begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix} \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 10 \end{bmatrix}
\]

## Solving a System of Equations

To solve \(\mathbf{A} \cdot \mathbf{x} = \mathbf{b}\), you can use methods such as Gaussian elimination, matrix inversion (if \(\mathbf{A}\) is invertible), or LU decomposition.

### Example: Matrix Inversion

For the system represented by:

\[
\mathbf{A} \cdot \mathbf{x} = \mathbf{b}
\]

If \(\mathbf{A}^{-1}\) exists, the solution is:

\[
\mathbf{x} = \mathbf{A}^{-1} \cdot \mathbf{b}
\]

Given:

\[
\mathbf{A} = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 5 \\ 4 \end{bmatrix}
\]

The inverse of \(\mathbf{A}\) is:

\[
\mathbf{A}^{-1} = \frac{1}{1} \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix}
\]

Thus, the solution is:

\[
\mathbf{x} = \begin{bmatrix} 2 & -3 \\ -1 & 2 \end{bmatrix} \cdot \begin{bmatrix} 5 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}
\]
