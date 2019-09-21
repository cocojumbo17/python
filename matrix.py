from copy import copy


class Matrix:
    def __init__(self, dim=2):
        self._dimension = dim
        self._m = [[1 for x in range(dim)] for y in range(dim)]

    def __copy__(self):
        temp = Matrix(self.dimension())
        for i in range(self.dimension()):
            for j in range(self.dimension()):
                temp.el(i, j, self.el(i, j))
        return temp

    def dimension(self):
        return self._dimension

    def matrix(self):
        return self._m

    def el(self, x, y, val=None):
        if x >= self.dimension() or y >= self.dimension():
            raise TypeError(f'indexes should be < {self.dimension()}')
        if val is not None: self.matrix()[x][y] = val
        return self.matrix()[x][y]

    def transpose(self):
        temp = Matrix(self.dimension())
        for i in range(self.dimension()):
            for j in range(self.dimension()):
                temp.el(i, j, self.el(j, i))
        return temp

    def minor(self, r, c):
        temp = Matrix(self._dimension - 1)
        d_row=0
        for row in range(self.dimension()):
            d_col=0
            if row == r:
                d_row -= 1
                continue
            for col in range(self.dimension()):
                if col == c:
                    d_col -= 1
                    continue
                temp.el(row+d_row, col+d_col, self.matrix()[row][col])
        return temp

    def determinant(self):
        if self.dimension() == 2:
            return self.el(0,0)*self.el(1,1) - self.el(0,1)*self.el(1,0)
        else:
            temp = self.makeFirstColumnZero()
            minor = temp.minor(0,0)
            return temp.el(0,0) * minor.determinant()

    def makeFirstColumnZero(self):
        temp = copy(self)
        if temp.el(0,0) == 0: raise TypeError('first element is zero')
        for row in range(1, temp.dimension()):
            k = -(temp.el(row, 0) / temp.el(0, 0))
            for col in range(temp.dimension()):
                new_val = temp.el(row, col) + k*temp.el(0, col)
                temp.el(row, col, new_val)
        return temp


    def __str__(self):
        res_str = ''
        for i in range(self.dimension()):
            res_str += f'|'
            for j in range(self.dimension()):
                res_str += f'{self.matrix()[i][j]:4} '
            res_str += f'|\n'
        return res_str


def initMatrix():
    dimension = int(input('dimension of matrix is '))
    m = Matrix(dim=dimension)
    for i in range(dimension):
        for j in range(dimension):
            value = float(input(f'M[{i},{j}]= '))
            m.el(i, j, value)
    return m

def initMatrixFromFile(filepath):
    m = Matrix(2)
    return m


def main():
    m1 = initMatrix()
    print('matrix is:')
    print(m1)
    print(f'determinant is {m1.determinant()}')
    # m2 = m1.transpose()
    # print('transpose matrix is:')
    # print(m2)
    #
    # m3=m2.minor(0,0)
    # print('minor00 of transpose matrix is:')
    # print(m3)


if __name__ == '__main__': main()
