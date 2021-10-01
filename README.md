# Fractal-Draw
This project the turtle module in Python to draw a fractal using the Lindenmayer System (L-System). You can learn more about the system here: https://en.wikipedia.org/wiki/L-system. This was a personal project to practice building more robust code and parsing arguments through the command line.

----------------------------------------------------------------------------------------
How it works.

Fractals are shapes with infinite complexity. They may not take up an infinite space but when zooming in infinitely on certain regions of a fractal, you will always see new patterns arise. Fractals can have a dimension between 1 and 2 as they necassarily do not take up infinite space but do still exist in the x-y plane.

The L-System is useful way to classify how a fractal is created it. We start with an initial state (the axiom) and we apply a production rule to this state a specified number of times (the iteration number). Fractals arise by applying a rule to an axiom an infinite amount of time.

The axiom and production rules are defined by a set of commands that tell the turtle how to draw the fractal. This project has programmed the following list of commands available for defining the axiom and production rules:

   'F' = Move forward 1 unit
   'G' = Move forward 1 unit
   '+' = Turn left
   '-' = Turn right
   '.' = Move forward 1 unit without drawing
   '[' = Save current position and angle
   ']' = Return to saved position and angle
 
The code takes in 5 arguments:

   -a --axiom       = The axiom for the fractal.
   -p --prod        = The production rule(s) for the fractal.
   -i --iteration   = The number of iterations (number of times the production rule is applied to the axiom).
   -t --angle       = The angle by which the turtle turns left or right, in degrees.
   -s --scalefactor = How much the lengths of the sides on the fractal decrease with each iteration.

Some fractals take more iterations to see their true shape. Some fractals also need different scalefactors in order to fit the shape on the screen.

----------------------------------------------------------------------------------------
Example 1: Von Koch Snowflake

The Von Koch Snowflake is defined by the following arguments:

   axiom = 'F--F--F'
   prod  = 'F:F+F--F+F'
   angle = 60

The axiom says that we start by moving forward 1 unit, turning left 120 degrees (turning left 60 degrees twice), move forward 1 unit, turn left 120 degrees, move forward unit. This creates an equalateral triangle. The production rule then says for everytime we move forward 1 unit, instead move forward 1 unit, turn right 60 degree, move forward 1 unit, turn left 120 degrees, move forward 1 unit, turn right 60 degrees, move forward 1 unit. This creates a line with a spike in the middle. Effectively we're saying that everytime we move forward, draw a spike in the middle of the line. By applying this rule 4 or more times, the snowflake shape starts to become apparent.

----------------------------------------------------------------------------------------
Example 2: Fractal Tree
   
   axiom = '++F'
   prod  = 'F:G[+F]-F', 'G:GG'
   angle = 45
   
This fractal has two types lines: a 'leaf' (F) and a 'branch' (G). The axiom is simply turn right 90 degrees and draw a leaf. The first production rule is then for each leaf, replace with a branch and draw two leafs at the end of it. The second production rule is to double the length of branches after each iteration. The tree shape can be seen after 5 iterations. Defining two different 'draw forward' commands allow for the distinction between branches and leafs. You can even set the color of the branches to brown and the leaves to green to get a more realistic tree look.

----------------------------------------------------------------------------------------
Other examples for fractals

Dragon Curve:

   axiom = 'F'
   prod  = 'F:F+G', 'G:F-G'
   angle = 90
   
Sierpinski triangle:

   axiom = 'F-G-G'
   prod  = 'F:F-G+F+G-F', 'G:GG'
   angle = 120

Sierpiński Arrowhead Curve

   axiom = 'F'
   prod  = 'F:G-F-G', 'G:F+G+F'
   angle = 60

----------------------------------------------------------------------------------------
Difficulties encountered when completing the project.

The first problem encountered was how to pass the production rule, as it relies on two inputs: the command being changed and what it is being changed into. I decided to take the input in the form of "old:new" (ex. "F:F+F--F+F"). This way the production rule is a single string. We can then separate this string into a tuple of two strings; one being the old command and one being the new command. Having the production rule in this format then makes it very simple to update the axiom.

The second problem was how to take in two or more production rules. This turned out to be a simple fix however as passing multiple arguments puts the arguments in a list. Passing them through the command line was simple as adding a "nargs='+'" to the argument parser allows multiple arguments to be passed through. The strategy used to separate the old and new command can then just be applied to each production rule in the list.

The final problem (and the hardest to solve) was how to update the axiom with two or more production rules. I had originally gone with using the replace function on the string:

   axiom.replace(prod[0], prod[1])
   
This worked when applying one rule, however when applying a second rule it would affect the 'new' commands created by applying the first rule, which would lead to the whole command list for drawing the fractal incorrect. This was solved by creating a separate function for updating the axiom with the production rule. We start by splitting the axiom string into a list of each individual command. The list is then scanned to see if any of the production rules can be applied. If they can then they are changed. This way, you don't get updated commands updated twice within one iteration. Once all commands have been scanned, the axiom is put back together with all the necassary commands updated.

-----------------------------------------------------------------------------------------
Thank you for looking at this personal project of mine. Any comments on how this could be improved will be gratefull, and I hope you enjoy making some pretty fractals :)
