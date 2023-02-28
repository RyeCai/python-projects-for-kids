import turtle

turt = turtle.Pen()
turt.speed(0)
turt.width(2)
# Change the color if you would like!
turt.color("purple")

# Draws a triangle from turt's current location
def triangle(length):
    # Replace pass with your triangle implementation
    pass

# Create a function that draws a square using turt


for side_length in range(10, 500, 10):
    # The loop currently draws circles. Change the code to have it draw triangles or squares 
    turt.circle(side_length)
    turt.left(10)
