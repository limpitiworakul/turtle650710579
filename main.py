"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'purple','red', 'green', 'blue', 'yellow','red', 'green', 'blue', 'pink','red', 'green', 'blue','black','red', 'green', 'blue','red', 'green', 'blue', 'purple','red', 'green', 'blue', 'yellow','red', 'green', 'blue', 'pink','red', 'green', 'blue','black','red', 'green', 'blue']:
    t.color(c)
    t.forward(200)
    t.left(175)