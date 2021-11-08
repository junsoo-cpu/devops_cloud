import turtle as t


def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360 / n)


def polygon2(n, a):
    for i in range(n):
        t.forward(a)
        t.left(360 / n)


polygon(3)
polygon(5)

t.up()
t.forward(100)
t.down()

polygon2(3, 75)
