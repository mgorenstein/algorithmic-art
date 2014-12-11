def setup():
    background(255)
    size(900,400)
    
def draw():
    line_height = 0
    line_width = width
    
    # draw lines for bottom triangle
    while line_height != height:
        line(0, line_height, line_width, height)
        line_height += 10
        line_width -= 10
    
    # initial triangle vertices
    x1 = 0; y1 = 0; 
    x2 = width; y2 = height; 
    x3 = width; y3 = 0;

    black = True
    for x in range(20):
        if black:
            fill(0)
            black = False
        else:
            fill(255)
            black = True
    
        triangle(x1, y1, x2, y2, x3, y3)
        x1 += 20; y1 += 20
        x2 -= 20; y2 -= 20
        x3 -= 20; y3 += 20
    
    save('tri1.jpg')
