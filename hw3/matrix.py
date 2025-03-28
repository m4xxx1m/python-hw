from functools import reduce


class HashMixin:
    def __hash__(self):
        """Sum each value in row, multiply all row sums and get
        remainder of the product of deleting by 140146659"""
        hash = (
            int(
                reduce(
                    lambda a, b: a * b,
                    map(lambda row: reduce(lambda a, b: a + b, row), self._matrix),
                )
            )
            % 140146659
        )
        if hash == -1:
            return -2
        return hash

    def __eq__(self, other):
        return isinstance(other, Matrix) and self._matrix == other._matrix


class DisplayMixin:
    def __str__(self):
        str_matrix = [[str(elem) for elem in row] for row in self._matrix]
        rows = ["\t".join(row) for row in str_matrix]
        return "\n".join(rows)

    def __repr__(self):
        str_matrix = [[str(elem) for elem in row] for row in self._matrix]
        rows = [", ".join(row) for row in str_matrix]
        return "Matrix([\n[" + "],\n[".join(rows) + "]\n])"


class Matrix(HashMixin, DisplayMixin):
    def __init__(self, data):
        if not isinstance(data, list) or any(not isinstance(row, list) for row in data):
            raise ValueError("Matrix must be a list of lists")
        if len(data) == 0 or len(data[0]) == 0:
            raise ValueError("Matrix must not be empty")
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must be the same size")
        self._matrix = data
        self._rows = len(data)
        self._cols = len(data[0])
        self._cache = {}

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Both operands must be Matrix")
        if self._cols != other._cols or self._rows != other._rows:
            raise ValueError("Addition requires matrices of the same shape")
        new_data = [
            [self._matrix[i][j] + other._matrix[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return Matrix(new_data)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Both operands must be a Matrix")
        if self._cols != other._cols or self._rows != other._rows:
            raise ValueError(
                "Element-wise multiplication requires matrices of the same shape"
            )
        new_data = [
            [self._matrix[i][j] * other._matrix[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return Matrix(new_data)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Both operands must be a Matrix")
        if self._cols != other._rows:
            raise ValueError("Matrices shapes are not valid for multiplication")

        key = hash(other)
        if key in self._cache:
            return self._cache[key]

        result = Matrix(
            [
                [
                    sum(
                        self._matrix[i][k] * other._matrix[k][j]
                        for k in range(self._cols)
                    )
                    for j in range(other._cols)
                ]
                for i in range(self._rows)
            ]
        )

        self._cache[key] = result
        return result

    def clear_cache(self):
        self._cache = {}
