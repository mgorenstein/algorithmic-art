'''
This algorithm generates a stochastic system of connected lines.
The System class draws a specified number of initial lines and then
draws a specified number of random lines that form a vertex with
one or two of the previously drawn lines. 
'''
from system import System
from datetime import datetime

def setup():
    global initial, connective
    initial = 30
    connective = 60
    size(450, 400)

def draw():
    background(255)
    global initial, connective
    sys = System(initial, connective)
    time = datetime.now().time()
    saveFrame("frames/%s.png" % (time))
    exit()
