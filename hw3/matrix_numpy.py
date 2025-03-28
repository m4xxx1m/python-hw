import numpy as np


class FileWriteMixin:
    def write_to_file(self, filename: str):
        with open(filename, "w") as f:
            print(self, file=f)


class DisplayMixin:
    def __str__(self):
        str_matrix = [[str(elem) for elem in row] for row in self._data]
        rows = ["\t".join(row) for row in str_matrix]
        return "\n".join(rows)

    def __repr__(self):
        str_matrix = [[str(elem) for elem in row] for row in self._data]
        rows = [", ".join(row) for row in str_matrix]
        return "Matrix([\n[" + "],\n[".join(rows) + "]\n])"


class DataPropertyMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, type(self)):
            self._data = value._data
        elif isinstance(value, np.ndarray):
            self._data = value
        elif isinstance(value, list):
            self._data = np.array(value)


class Matrix(
    np.lib.mixins.NDArrayOperatorsMixin, DisplayMixin, FileWriteMixin, DataPropertyMixin
):
    def __init__(self, matrix):
        self._data = np.array(matrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x._data if isinstance(x, Matrix) else x for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        return type(self)(result.tolist()) if isinstance(result, np.ndarray) else result
