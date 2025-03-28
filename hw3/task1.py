import numpy as np

from matrix import Matrix

if __name__ == "__main__":
    np.random.seed(0)
    matrix_lhs = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix_rhs = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    with open("artifacts/task1/matrix+.txt", "w") as f:
        print(matrix_lhs + matrix_rhs, file=f)

    with open("artifacts/task1/matrix*.txt", "w") as f:
        print(matrix_lhs * matrix_rhs, file=f)

    with open("artifacts/task1/matrix@.txt", "w") as f:
        print(matrix_lhs @ matrix_rhs, file=f)
