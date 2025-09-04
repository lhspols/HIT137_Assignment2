import turtle

def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)
        turtle.right(120)
        draw_edge(length, depth - 1)
        turtle.left(60)
        draw_edge(length, depth - 1)

def draw_pattern(sides, length, depth):
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(360 / sides)

def main():
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.pendown()

    draw_pattern(sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()
