import graphics as gr


def matryoshka(n):
    if n == 1:
        print('matryoshka')
    else:
        print('top of', n)
        matryoshka(n - 1)
        print('bottom of ', n)


def rect(a, b, c, d, w):
    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(w)


# -------------------------------------------------------
def fractal(a, b, c, d, n, k, w):
    if (n == 0):
        return
    rect(a, b, c, d, w)
    a1 = (a[0] * (1 - k) + b[0] * k, a[1] * (1 - k) + b[1] * k)
    b1 = (b[0] * (1 - k) + c[0] * k, b[1] * (1 - k) + c[1] * k)
    c1 = (c[0] * (1 - k) + d[0] * k, c[1] * (1 - k) + d[1] * k)
    d1 = (d[0] * (1 - k) + a[0] * k, d[1] * (1 - k) + a[1] * k)
    fractal(a1, b1, c1, d1, n - 1, k, w)


def draw_fractal():
    win = gr.GraphWin('Fractal', 600, 600)
    k = 0.1
    fractal((100, 100), (500, 100), (500, 500), (100, 500), 50, k, win)
    win.getMouse()
    win.close()


# -------------------------------------------------------
def gcd(a, b):
    """найбільший спільний дільник"""
    if b == 0:
        return a
    a = a % b
    return gcd(b, a)


# -------------------------------------------------------
class Hanoy:
    def __init__(self, n):
        self._n = n
        self._stick_1 = list(range(n, 0, -1))
        self._stick_2 = []
        self._stick_3 = []
        self._counter = 0

    def say(self):
        print(self._stick_1)
        print(self._stick_2)
        print(self._stick_3)
        print('-' * 20, self._counter)
        self._counter+=1

    def work(self, n, f, t, m):
        if n == 1:
            a = f.pop()
            t.append(a)
            self.say()
        else:
            self.work(n - 1, f, m, t)
            self.work(1, f, t, m)
            self.work(n - 1, m, t, f)

    def start(self):
        self.say()
        self.work(self._n, self._stick_1, self._stick_3, self._stick_2)


def hanoy(n):
    h = Hanoy(n)
    h.start()


def generate_number(ss, n, pref=[]):
    if n == 0:
        print(*pref, sep=',')
        return
    for d in range(ss):
        pref.append(d)
        generate_number(ss, n - 1, pref)
        pref.pop()


def main():
    # matryoshka(5)
    # draw_fractal()
    # print(gcd(12,1024))
    # generate_number(5, 3)
    hanoy(5)


if __name__ == '__main__': main()
