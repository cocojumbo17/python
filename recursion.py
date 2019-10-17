import graphics as gr

def matryoshka(n):
    if n==1:
        print('matryoshka')
    else:
        print('top of', n)
        matryoshka(n-1)
        print('bottom of ', n)


def rect(a,b,c,d,w):
    for m,n in (a,b), (b,c), (c,d), (d,a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(w)

def fractal(a,b,c,d,n,k,w):
    if (n==0):
        return
    rect(a,b,c,d,w)
    a1 = (a[0]*(1-k) + b[0]*k, a[1]*(1-k) + b[1]*k)
    b1 = (b[0]*(1-k) + c[0]*k, b[1]*(1-k) + c[1]*k)
    c1 = (c[0]*(1-k) + d[0]*k, c[1]*(1-k) + d[1]*k)
    d1 = (d[0]*(1-k) + a[0]*k, d[1]*(1-k) + a[1]*k)
    fractal(a1,b1,c1,d1,n-1,k,w)

def draw_fractal():
    win = gr.GraphWin('Fractal', 600, 600)
    k = 0.1
    fractal((100,100),(500,100),(500,500),(100,500),50,k,win)
    win.getMouse()
    win.close()

def main():
    draw_fractal()

if __name__ == '__main__':main()
