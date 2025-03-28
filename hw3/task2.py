import numpy as np

from matrix_numpy import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    matrix_lhs = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix_rhs = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    m_add = matrix_lhs + matrix_rhs
    m_add.write_to_file("artifacts/task2/matrix+.txt")

    m_mul = matrix_lhs * matrix_rhs
    m_mul.write_to_file("artifacts/task2/matrix*.txt")

    m_matmul = matrix_lhs @ matrix_rhs
    m_matmul.write_to_file("artifacts/task2/matrix@.txt")
