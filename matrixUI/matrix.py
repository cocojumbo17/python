import getpass
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

    def multiply(self, koef):
        """
        multiply matrix to number
        :param koef: float number
        :return: new matrix
        """
        temp = Matrix(self.dimension())
        for i in range(self.dimension()):
            for j in range(self.dimension()):
                temp.el(i, j, self.el(i, j) * koef)
        return temp


    def dimension(self):
        return self._dimension

    def matrix(self):
        return self._m

    def el(self, x, y, val=None):
        if x >= self.dimension() or y >= self.dimension():
            raise TypeError(f'indexes should be < {self.dimension()}')
        if val is not None:
            self.matrix()[x][y] = val
        return self.matrix()[x][y]

    def row(self, r, val=None):
        if r >= self.dimension():
            raise TypeError(f'row should be < {self.dimension()}')
        if val is not None:
            self.matrix()[r] = val
        return self.matrix()[r]

    def transpose(self):
        """
        make transpose matrix
        :return: new transpose matrix
        """
        temp = Matrix(self.dimension())
        for i in range(self.dimension()):
            for j in range(self.dimension()):
                temp.el(i, j, self.el(j, i))
        return temp

    def minor(self, r, c):
        """
        find minor of mathix
        :param r: row
        :param c: column
        :return: return new matrix without row and column
        """
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
        """
        find determinant of matrix
        :return: float number
        """
        if self.dimension() == 2:
            return self.el(0,0)*self.el(1,1) - self.el(0,1)*self.el(1,0)
        else:
            temp,sign = self.makeFirstColumnZero()
            minor = temp.minor(0,0)
            return sign * temp.el(0,0) * minor.determinant()

    def inverse(self):
        """
        find inverse matrix
        :return: return new inverse matrix
        """
        det = self.determinant()
        if det == 0:
            raise TypeError('determinant is zero. impossible to find inverse matrix')
        comp = self.complement()
        trans_comp = comp.transpose()
        im = trans_comp.multiply(1/det)
        return im

    def complement(self):
        """
        find algebraic complement to current matrix
        :return: new algebraic complement matrix
        """
        acm = Matrix(self.dimension())
        for i in range(self.dimension()):
            for j in range(self.dimension()):
                minor = self.minor(i, j)
                minor_det = minor.determinant()
                sign = -1
                if (i+j)%2 == 0:
                    sign = 1
                acm.el(i,j,sign*minor_det)
        return acm


    def makeFirstColumnZero(self):
        """
        try to make first column of matrix make zero
        :return: new matrix with zero first column
        """
        temp = copy(self)
        found = False
        if temp.el(0,0) == 0:
            for y in range(1,temp.dimension()):
                if temp.el(y, 0) != 0:
                    found=True
                    buf = temp.row(0);
                    temp.row(0, temp.row(y))
                    temp.row(y, buf)
                    break
            if not found:
                return [temp, 1]
        for row in range(1, temp.dimension()):
            k = -(temp.el(row, 0) / temp.el(0, 0))
            for col in range(temp.dimension()):
                new_val = temp.el(row, col) + k*temp.el(0, col)
                temp.el(row, col, new_val)
        return [temp, -1 if found else 1]


    def __str__(self):
        res_str = ''
        for i in range(self.dimension()):
            res_str += f'|'
            for j in range(self.dimension()):
                res_str += f'{self.matrix()[i][j]:10.5} '
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

def initMatrixFromText(string):
    first_line = True;
    cur_line=0
    for s in string:
        l = s.split()
        if len(l) > 1:
            if first_line:
                first_line = False
                m = Matrix(len(l))
            cur_row = 0
            for item in l:
                value = float(item)
                m.el(cur_line, cur_row, value)
                cur_row += 1
            cur_line += 1
    return m

def initMatrixFromFile(filename):
    f = open(filename, 'r')
    string = f.readlines()
    f.close()
    return initMatrixFromText(string)

def test():
    print('start')
    pas = getpass.getpass('your password:')
    print(pas)

def main():
#    m1 = initMatrix()
    m1 = initMatrixFromFile('4.matrix')
    print('matrix is:')
    print(m1)
    print(f'determinant is {m1.determinant()}')
    invers = m1.inverse()
    print('inverse matrix is:')
    print(invers)

if __name__ == '__main__': main()
