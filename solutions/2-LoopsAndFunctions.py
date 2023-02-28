import turtle

turt = turtle.Pen()
turt.speed(0)
turt.width(2)
def triangle(length):
    for i in range(3):
        turt.forward(length)
        turt.left(120)

def square(length):
    for i in range(4):
        turt.forward(length)
        turt.left(90)
        
for j in range(10, 500, 10):
    #turt.begin_fill()
    turt.circle(j)
    #triangle(j)
    #turt.end_fill()
    turt.left(10)
