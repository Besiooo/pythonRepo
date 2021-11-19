from matrix import Matrix, Vector, is_int
import random


class Program:
    matrix = []

    def __init__(self):
        self.randomize_matrix()
        if is_int(self.matrix[0]):
            matrix_object = Vector(self.matrix)
        else:
            matrix_object = Matrix(self.matrix)

        if matrix_object.is_matrix_correct():
            matrix_object.show_mtx()
            matrix_object.sum_mtx()

    def randomize_matrix(self):
        max_range = 30
        max_value = 9
        min_value = 0
        cols = random.randint(1, max_range)
        rows = random.randint(1, max_range)

        for _ in range(rows):
            row = [random.randint(min_value, max_value) for x in range(cols)]
            self.matrix.append(row)


Program()

