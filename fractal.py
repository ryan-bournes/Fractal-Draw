#!/usr/bin/env python

# Imports needed modules
import argparse
import sys
import numpy as np

# This code uses tthe turtle module to draw fractals.
import turtle


# Function that updates the axiom with the production rule(s).
def update_axiom( axiom, prod ):
    """Applies the production rule(s) to the axiom and returns the updated axiom."""

    # Separate the axiom string into a list of each individual command.
    temp = []
    for i in axiom:
        temp.append(i)

    # Read through the list, if the command matches a production rule, update it.
    for i in range(np.size(temp)):
        for j in range(np.size(prod)/2):
            if temp[i] == prod[j][0]:
                temp[i] = prod[j][1]

    # Combine the updated list into a single string of commands.
    new_axiom = ''
    for i in temp:
        new_axiom += i
    
    return new_axiom


# Draws the fractal.
def fractal( t, axiom, prod, iteration, angle, scalefactor ):
    """Reads the axiom and draws the fractal based on the L-system."""

    # Update the axiom with the production rule n times. 
    for n in range(iteration):
        axiom = update_axiom( axiom, prod )
    
    # Initiate position and angle lists, needed for the '[' and ']' commands.
    x = []
    y = []
    a = []

    # Read through each command in axiom and draw based on what the command is.
    for i in axiom:
        if i == 'F':
            # Move forward 1 unit
            t.forward(300.0/scalefactor**iteration)
        elif i == 'G':
            # Move forward 1 unit. Two different commands for moving forward is needed for drawing some fractals.
            t.forward(300.0/scalefactor**iteration)
        elif i == '+':
            # Turn left by angle.
            t.left(angle)
        elif i == '-':
            # Turn right by angle.
            t.right(angle)
        elif i == '.':
            # Move forward 1 unit without drawing.
            t.penup()
            t.forward(300.0/scalefactor**iteration)
            t.pendown()
        elif i == '[':
            # Save the current position and angle of the turtle.
            x.append(t.pos()[0])
            y.append(t.pos()[1])
            a.append(t.heading())
        elif i == ']':
            # Return to the saved position and angle.
            t.penup()
            t.setpos(x[-1], y[-1])
            t.setheading(a[-1])
            t.pendown()
            # Remove that saved position and angle from the lists.
            x.pop(-1)
            y.pop(-1)
            a.pop(-1)
        else:
            # If the command does not match any of the programmed commands, print error message and terminate the program.
            print(i + ' is an invalid command. Please see the README for list of commands.')
            sys.exit()


# Function that allows command line to take arguements.
def parse_args():
    """Parses arguements in the command line."""

    # Create the argument parser.
    parser = argparse.ArgumentParser(description='Create a fractal using the Lindenmeyer System. Explanation of this can be found here: https://en.wikipedia.org/wiki/L-system')

    # Define the term needed to set each variable, give a brief description of what the variable is, a default value for it and what type it takes in.
    parser.add_argument( "-a", "--axiom", help="Axiom for the fractal. Taken as a string. Example: 'F++F', start by moving forward 1 unit, turning left twice and moving forward 1 unit.", type=str)
    parser.add_argument( "-p", "--prod", help="Production rule after each iteration. Taken as a string. Example: 'F:F+F' will replace every F with F+F .", nargs='+', type=str)
    parser.add_argument( "-i", "--iteration", help="Iteration number to be drawn. Taken as a positive integer. Example: 3 applies the production rule 3 times.", default=3, type=int)
    parser.add_argument( "-t", "--angle", help="Angle which turtle turns in degrees. Taken as a float. Example: 60.0 will cause + and - to turn left and right 60 degrees respectively.", default=60.0, type=float)
    parser.add_argument( "-s", "--scalefactor", help="Scale at which the lengths of lines decrease with each iteration. Lower scalefactors leads to slower decrease. Taken as a float. Cannot be zero. Example: 3 decreases the length of lines to 1/3 after each iteration.", default=3.0, type=float)

    return parser.parse_args()


def main():
    """Main function of the project."""

    # Loads in the arguements from the command line
    args = parse_args()

    # Initiates the turtle, hides the turtle crosshair and sets it max speed.
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Places the production rule(s) into an array.
    prod = []
    for i in args.prod:
        # Separates each production rule into the command being updated and what the update is.
        prod.append(( i[:i.index(':')], i[i.index(':')+1:] ))

    
    # Draws the fractal based on the axiom, production rule(s), iteration number, angle and length adjustment scalefactor.
    fractal(t, args.axiom, prod, args.iteration, args.angle, args.scalefactor)

    # Keeps the drawing on screen once turtle has finished drawing the fractal.
    turtle.mainloop()


# Runs the code.
if __name__ == '__main__':
    main()
