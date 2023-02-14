#Jonah Valentine
#jonahfordvalentine@gmail.com
#Week 4 PA
#North Seattle College CSC110
#done

#function 1: main

import turtle

def main():
    jamie = turtle.Turtle()

    #all polygons
    num_sides = int(input("please input positive integer that is 3 or greater: "))
    num_sides2 = int(input("please input positive integer that is 3 or greater: "))
    num_sides3 = int(input("please input positive integer that is 3 or greater: "))

    #all circle sets; how many circles
    num_circles = int(input("please input a positive integer: "))
    num_circles2 = int(input("please input a positive integer: "))

    #size/scale of poly and circles
    size = int(input("please input number between 50 and 200: "))

    #first poly plus color
    jamie.color("lightpink")
    jamie.pencolor("red")
    jamie.begin_fill()
    
    draw_polygon(jamie, num_sides, size)
    jamie.penup()
    jamie.backward(200)
    jamie.left(200)
    
    jamie.end_fill()
    
    #sec poly plus fill
    jamie.color("PaleTurquoise")
    jamie.pencolor("cyan")
    jamie.begin_fill()
    
    draw_polygon(jamie, num_sides2, size)
    jamie.penup()
    jamie.backward(300)
    jamie.right(100)

    jamie.end_fill()

    #third poly plus fill
    jamie.color("lightgreen")
    jamie.pencolor("green")
    jamie.begin_fill()
    draw_polygon(jamie, num_sides3, size)
    jamie.penup()
    jamie.forward(100)
    jamie.left(50)

    jamie.end_fill()


#circles below
    jamie.pencolor("gold")
    jamie.home()
    draw_concentric_circles(jamie, num_circles, size)

   
    jamie.goto(-100,-150)
    jamie.pencolor("red")
    draw_concentric_circles(jamie, num_circles2, size)
    

#function 2: polygon
def draw_polygon(our_turtle, num_sides, side_length):
    our_turtle.pendown()
    angle = (num_sides - 2) * (180 / num_sides)
    for i in range(num_sides):
        our_turtle.forward(side_length)
        our_turtle.right(180 - angle)

    
#function 3: CIRCLES that are ACTUALLY CONCENTRIC
def draw_concentric_circles(our_turtle, num_circles, starting_radius):
    our_turtle.penup()
    for i in range(num_circles):
        our_turtle.pendown()
        our_turtle.circle(starting_radius)
        our_turtle.dot()
        our_turtle.penup()
        our_turtle.dot()
        
        our_turtle.seth(270)
        starting_radius = starting_radius + 20
        our_turtle.forward(20)
        our_turtle.seth(0)


        
        

main()
