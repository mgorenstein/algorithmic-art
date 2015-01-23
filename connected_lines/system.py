from line import Line
# Python's random function serves me better here
import random

class System:
    def __init__(self, initial, connective):
        self.lines = []
        self.initial = initial
        self.connective = connective
        
        for x in range(self.initial):
            new_line = Line.two_random_points()
            v1, v2 = new_line.points()
            self.lines.append(new_line)
            
        for x in range(self.connective):
            # decimal from 0 to 1
            choice = random.random()
            if choice < 0.3:
                new_line = self.line_with_one_connection()
            else:
                new_line = self.line_with_two_connections()
            
            self.lines.append(new_line)
        
    def line_with_one_connection(self):
        random_line = random.choice(self.lines)
        random_point = random.choice(random_line.points())
        return Line.one_random_point(random_point)
    
    def line_with_two_connections(self):
        random_line_one = random.choice(self.lines)
        random_line_two = random.choice(self.lines)
        random_point_one = random.choice(random_line_one.points())
        random_point_two = random.choice(random_line_two.points())
        return Line(random_point_one, random_point_two)
