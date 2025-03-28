from matrix import Matrix

if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    C = Matrix([[2, 5], [0, 3]])
    B = Matrix([[1, 3], [3, 7]])
    D = Matrix([[1, 3], [3, 7]])

    with open("artifacts/task3/A.txt", "w") as f:
        print(A, file=f)
    with open("artifacts/task3/B.txt", "w") as f:
        print(B, file=f)
    with open("artifacts/task3/C.txt", "w") as f:
        print(C, file=f)
    with open("artifacts/task3/D.txt", "w") as f:
        print(D, file=f)

    assert hash(A) == hash(C)
    assert A != C
    assert B == D
    AB = A @ B
    CD = C @ D
    assert AB != CD

    with open("artifacts/task3/AB.txt", "w") as f:
        print(AB, file=f)
    with open("artifacts/task3/CD.txt", "w") as f:
        print(CD, file=f)

    with open("artifacts/task3/hash.txt", "w") as f:
        print(f"hash of matrices A and C: {hash(A)}", file=f)
        print(f"hash of matrices B and D: {hash(B)}", file=f)
        print(f"hash of matrix A @ B: {hash(AB)}", file=f)
        print(f"hash of matrix C @ D: {hash(CD)}", file=f)
