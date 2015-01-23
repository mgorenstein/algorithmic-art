# return a random point within the display parameters
def random_point():
    return random(width + 1), random(height + 1)

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.draw()
    
    @classmethod
    def one_random_point(cls, point1):
        point2 = random_point()
        return cls(point1, point2)

    @classmethod
    def two_random_points(cls):
        point1 = random_point()
        point2 = random_point()
        return cls(point1, point2)
        
    def draw(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        line(x1, y1, x2, y2)
        
    def points(self):
        return self.point1, self.point2
        
