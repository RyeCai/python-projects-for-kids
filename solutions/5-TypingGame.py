import turtle
import random
import time
import math

finishLine = 400
screen = turtle.Screen()
turt = turtle.Pen()
end = turtle.Pen()
turt.resizemode("auto")
screen.setup(width = finishLine*2, height = 480, startx = None, starty = None)
operations = ["+", "-", "*"]


def playGame(x,y):
    turt.reset()
    end.reset()
    end.ht()
    turt.shape("turtle")
    turt.color("green")
    turt.width(10)
    turt.penup()
    turt.speed(0)
    turt.goto(-finishLine, -120)
    turt.pendown()
    turt.speed("fast")
    startTime = time.time()
    finished = False
    while not finished and turt.xcor() < finishLine:
        operand1 = random.randint(1,10)
        operand2 = random.randint(1,10)
        operation = operations[random.randint(0,len(operations)-1)]
        solution = 0
        if operation == "+":
            solution = operand1 + operand2
        elif operation == "-":
            solution = operand1 - operand2
        elif operation == "*":
            solution = operand1 * operand2
        answer = screen.numinput("Solve the Math Problem:", str(operand1) + operation + str(operand2))
        if answer != None and answer == solution:
            turt.forward(100)
        elif answer == None:
            finished = True
        else:
            turt.backward(50)

    if turt.xcor() >= finishLine:
        end.write("You Win! Your time: " + str(math.trunc(time.time()- startTime)) + " seconds. Click to try again!", False, align="center", font=('Arial', 24, 'bold'))
        
screen.onclick(playGame)
playGame(0,0)
    


