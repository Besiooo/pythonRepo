from rich import print
from rich.console import Console

console = Console()


def is_int(element):
    return isinstance(element, int)


class Matrix:

    def __init__(self, mtx, gen="matrix"):
        self.mtx = mtx
        self._cols = 1 if is_int(self.mtx[0]) else len(self.mtx[0])
        self._rows = len(self.mtx)
        console.print(f"I have received a new {gen} with dimensions of [{self._cols}, {self._rows}]", style="bold blue")

    def is_matrix_correct(self):
        cols = len(self.mtx[0])
        for row in self.mtx:
            if len(row) != cols:
                print(f"This matrix is wrong! (not every row has {cols} elements)")
                return False
        return True

    def print_mtx(self):
        for row in self.mtx:
            for col in row:
                print(col, end=" ")
            print()

    def show_mtx(self):
        if self.is_matrix_correct():
            print("M = ")
            self.print_mtx()
        else:
            print("Cannot print wrong matrices!")

    def sum_mtx(self):
        sum_table = []
        for row in self.mtx:
            row_sum = sum(row)
            sum_table.append(row_sum)

        print(f"Sum of this matrix = {sum_table}")


class Vector(Matrix):
    def __init__(self, mtx):
        super().__init__(mtx, "vector")

    def is_matrix_correct(self):
        cols = 1
        for row in self.mtx:
            if not is_int(row):
                print(f"This vector is wrong! (not every row has {cols} element)")
                return False
        return True

    def show_mtx(self):
        if self.is_matrix_correct():
            print("M = ")
            for row in self.mtx:
                print('\t' + str(row))
        else:
            print("Cannot print wrong vortexes!")

    def sum_mtx(self):
        n = [element for element in self.mtx]

        print(f"Sum of this vector = {n}")
