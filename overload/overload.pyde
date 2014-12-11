def setup():
    size(900,400)
    background(255)
    rectMode(CENTER)

def draw():
    ''' left rectangle '''
    noStroke()
    x = width / 4
    y = height / 2
    rect_width = width/2
    rect_height = height
    black = True
    for rectangle in range(20):
        if black:
            fill(0)
            black = False
        else:
            fill(255)
            black = True
        rect(x, y, rect_width, rect_height)
        rect_width -= 23
        rect_height -= 23
    
    ''' right lines '''
    stroke(0)
    strokeWeight(3)
    
    # horizontal lines
    for l in range(20):
        y = 10 * (l + 1)
        line(width/2, y, width, y)
        
    # vertical lines
    for l in range(30):
        x = width/2 + 15 * (l + 1)
        line(x, 0, x, height/2)
    
    # diagonal lines
    strokeWeight(2)
    x1 = width/2; y1 = height/2; x2 = width; y2 = height
    while y1 != height:
        line(x1, y1, x2, y2)
        y1 += 10
        x2 -= 20
    
    # final triangle
    fill(0)
    triangle(width/2, height/2, width, height/2, width, height)
    
    save('overload.jpg')

