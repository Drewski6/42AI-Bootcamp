"""
Vector class
"""
class Vector:
    """
    Vector class for common vector operations.\n
    values:\n
    takes a list of list of floats where at least one dimention of the vector must be 1.\n
    or, an int indicating the size of the resulting vector starting with 0\n
    or, a tuple of 2 ints with beginning and end values\n
    """
    def __init__(self, values):
        if isinstance(values, int):
            assert (values > 0), "Integers passed for vector initialization must be positive."
            self.__init_n_1(values)
            print(self.values)
            self.__init_shape()
        elif isinstance(values, tuple):
            assert (len(values) == 2), "Tuples passed can only contain 2 elements"
            assert (isinstance(values[0], int) and isinstance(values[1], int)), "\
                Tuple values must be ints."
            assert (values[1] - values[0] > 0), "\
                range of values must be greater than 0"
            self.__init_n_1(values[1], values[0])
            print(self.values)
            self.__init_shape()
        elif isinstance(values, list):
            for l_item in values:
                for f_item in l_item:
                    assert (isinstance(f_item, float)), "values should be a list of list of floats"
                assert (isinstance(l_item, list)), "values should be a list of list of floats"
            assert (len(values) == 1 or len(values[0]) == 1), "\
                At least one dimention of the vector must be 1."
            self.values = values
            self.__init_shape()
        else:
            raise ValueError("Argument 'values' must be a positive int,\
                a tuple either (1, n) or (n, 1), \
                or a list of lists of floats.")

    def __vector_op_check(self, vector):
        assert (isinstance(vector, Vector)), "\
            Can only perform operations on vectors the same shape."
        assert (self.shape == vector.shape), "\
            Can only perform operations on vectors the same shape."

    def __scalar_op_check(self, scalar):
        assert isinstance(scalar, float) or isinstance(scalar, int), "\
            scalar value must be float or int"
        if isinstance(scalar, int):
            f_scalar = float(scalar)
        else:
            f_scalar = scalar
        return f_scalar

    def __init_shape(self):
        if len(self.values[0]) > 1:
            self.shape = (1, len(self.values[0]))
        else:
            self.shape = (len(self.values), 1)

    def __init_n_1(self, size, start=0):
        self.values = []
        for pos, item in enumerate(range(start, size)):
            self.values.append([])
            self.values[pos].append(float(item))

    def dot(self, vector):
        """
        Perform dot product on two vectors of the same shape.
        """
        self.__vector_op_check(vector)
        result = []
        if len(vector.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(vector.values[0]):
                result[0].append(value * self.values[0][pos])
        else:
            for pos, value in enumerate(vector.values):
                result.append([])
                result[pos].append(value[0] * self.values[pos][0])
        return result

    def T(self):
        """
        Transpose:\n
        Change vectors of shape (1, n) to (n, 1) and vice versa.
        """
        result = []
        if len(self.values[0]) > 1:
            for pos, value in enumerate(self.values[0]):
                result.append([])
                result[pos].append(value)
            self.values = result
            self.__init_shape()
        else:
            result.append([])
            for pos, value in enumerate(self.values):
                result[0].append(value[0])
            self.values = result
            self.__init_shape()
        self.values = result

    def __add__(self, vector):
        self.__vector_op_check(vector)
        result = []
        if len(vector.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(vector.values[0]):
                result[0].append(value + self.values[0][pos])
        else:
            for pos, value in enumerate(vector.values):
                result.append([])
                result[pos].append(value[0] + self.values[pos][0])
        return result

    def __radd__(self, vector):
        self.__vector_op_check(vector)
        result = []
        if len(vector.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(vector.values[0]):
                result[0].append(value + self.values[0][pos])
        else:
            for pos, value in enumerate(vector.values):
                result.append([])
                result[pos].append(value[0] + self.values[pos][0])
        return result

    def __sub__(self, vector):
        self.__vector_op_check(vector)
        result = []
        if len(vector.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(vector.values[0]):
                result[0].append(self.values[0][pos] - value)
        else:
            for pos, value in enumerate(vector.values):
                result.append([])
                result[pos].append(self.values[pos][0] - value[0])
        return result

    def __rsub__(self, vector):
        self.__vector_op_check(vector)
        result = []
        if len(vector.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(vector.values[0]):
                result[0].append(self.values[0][pos] - value)
        else:
            for pos, value in enumerate(vector.values):
                result.append([])
                result[pos].append(self.values[pos][0] - value[0])
        return result

    def __truediv__(self, scalar):
        scalar = self.__scalar_op_check(scalar)
        result = []
        if len(self.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(self.values[0]):
                result[0].append(value / scalar)
        else:
            for pos, value in enumerate(self.values):
                result.append([])
                result[pos].append(value[0] / scalar)
        return result

    def __rtruediv__(self, scalar):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, scalar):
        scalar = self.__scalar_op_check(scalar)
        result = []
        if len(self.values[0]) > 1:
            result.append([])
            for pos, value in enumerate(self.values[0]):
                result[0].append(value * scalar)
        else:
            for pos, value in enumerate(self.values):
                result.append([])
                result[pos].append(value[0] * scalar)
        return result

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f'Vector({self.values})'
