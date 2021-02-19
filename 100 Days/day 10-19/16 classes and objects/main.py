#import turtle
# the object is timmy
#the variable or class is Turtle()
#the first turtle is pulling it from the module
#timmy = turtle.Turtle()

#to simplify
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.fd(100)
#
# my_screen = Screen()
# #adjust object attributes
# print(my_screen.canvheight)
# #call object methods
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon name", ["pikachu","squirtle", "charmander"])
table.add_column("type", ["electric", "water", "fire"])

#adjust attribute
table.align ="l"

print(table)