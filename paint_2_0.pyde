def setup():
    background(100, 100, 100)
    size(800, 800)
    noStroke()
    rect(width * 0.1, height * 0.05, width * 0.8, height * 0.75)



index = 0
radiuse = 3
clr = (
color(193, 179, 53),
color(144, 95, 83),
color(41, 5, 255),
color(162, 17, 11),
color(27, 213, 222),
color(245, 35, 235),
color(155, 250, 109),
color(87, 8, 116),
color(21, 255, 89),
color(22, 100, 45),
color(102, 124, 126),
color(67, 155, 132),
color(224, 132, 38),
color(245, 143, 235),
color(255, 0, 0),
color(95, 92, 93),
color(172, 185, 182),
color(115, 183, 165),
color(140, 0, 196),
color(233, 255, 0),
color(255)
)




def draw():
    global radiuse, clr, index
    noStroke() 
    fill(clr[index]) 
    rect(5, 60, 70, 40)

    if mouseButton == LEFT:
        
        if 5 < mouseX < 40 and 250 < mouseY < 285:
            fill(255)
            rect(15, 260, 15, 15)
            fill(100, 100, 100)
            ellipse(57.5, 267.5, 15, 15)
    
            
        if 40 < mouseX < 75 and 250 < mouseY < 285:
            fill(255)
            ellipse(57.5, 267.5, 15, 15)
            fill(100, 100, 100)
            rect(15, 260, 15, 15)
       
            
        if width * 0.89 > mouseX > width * 0.11 and height * 0.79 > mouseY > height * 0.06:
            ellipse(mouseX, mouseY, radiuse, radiuse)
    
        

        if width * 0.1 < mouseX < width * 0.1 + 30 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 0
        if width * 0.1 + 30 < mouseX < width * 0.1 + 60 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 1
        if width * 0.1 + 60 < mouseX < width * 0.1 + 90 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 2
        if width * 0.1 + 90 < mouseX < width * 0.1 + 120 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 3 
        if width * 0.1 + 120 < mouseX < width * 0.1 + 150 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 4
        if width * 0.1 + 150 < mouseX < width * 0.1 + 180 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 5
        if width * 0.1 + 180 < mouseX < width * 0.1 + 210 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 6
        if width * 0.1 + 210 < mouseX < width * 0.1 + 240 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 7
        if width * 0.1 + 240 < mouseX < width * 0.1 + 270 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 8
        if width * 0.1 + 270 < mouseX < width * 0.1 + 300 and height * 0.8 < mouseY < height * 0.8 + 30:
            index = 9
        if width * 0.1 < mouseX < width * 0.1 + 30 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 10
        if width * 0.1 + 30 < mouseX < width * 0.1 + 60 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 11
        if width * 0.1 + 60 < mouseX < width * 0.1 + 90 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 12
        if width * 0.1 + 90 < mouseX < width * 0.1 + 120 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 13
        if width * 0.1 + 120 < mouseX < width * 0.1 + 150 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 14
        if width * 0.1 + 150 < mouseX < width * 0.1 + 180 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 15
        if width * 0.1 + 180 < mouseX < width * 0.1 + 210 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 16
        if width * 0.1 + 210 < mouseX < width * 0.1 + 240 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 17
        if width * 0.1 + 240 < mouseX < width * 0.1 + 270 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 18
        if width * 0.1 + 270 < mouseX < width * 0.1 + 300 and height * 0.8 + 30 < mouseY < height * 0.8 + 60:
            index = 19
    
    
    
    
    if mouseButton == RIGHT:
        fill(255)
        noStroke()
        rect(width * 0.1, height * 0.05, width * 0.8, height * 0.75)
    
    
    for i in range(20):
        fill(clr[i])
        if i < 10:
            rect(width * 0.1 + 30 * i, height * 0.8, 30, 30)
        else:
            rect(width * 0.1 - 300 + 30 * i, height * 0.8 + 30, 30, 30)
    
    
    stroke(0)        
    strokeWeight(2)
    line(5, 120, 70, 120)
    strokeWeight(6)
    line(6, 138, 70, 138)
    strokeWeight(12)
    line(9, 160, 67, 160)
    strokeWeight(20)
    line(13, 190, 65, 190)
    
    
    if mouseButton == LEFT:
        if 5 < mouseX < 75 and 110 < mouseY < 130:
            radiuse = 3
            noFill()
            strokeWeight(2)
            stroke(0, 255, 0)
            rect(1, 115, 75, 10)
            stroke(100, 100, 100)
            rect(1, 175, 75, 30)
            rect(1, 148, 75, 25)
            rect(1, 130, 75, 15)
            
        if 5 < mouseX < 75 and 130 < mouseY < 145:
            radiuse = 9
            noFill()
            strokeWeight(2)
            stroke(0, 255, 0)
            rect(1, 130, 75, 15)
            stroke(100, 100, 100)
            rect(1, 175, 75, 30)
            rect(1, 148, 75, 25)
            rect(1, 115, 75, 10)
            
        if 5 < mouseX < 75 and 148 < mouseY < 173:
            radiuse = 15
            noFill()
            strokeWeight(2)
            stroke(0, 255, 0)
            rect(1, 148, 75, 25)
            stroke(100, 100, 100)
            rect(1, 175, 75, 30)
            rect(1, 130, 75, 15)
            rect(1, 115, 75, 10)
            
        if 5 < mouseX < 75 and 173 < mouseY < 210:
            radiuse = 25
            noFill()
            strokeWeight(2)
            stroke(0, 255, 0)
            rect(1, 175, 75, 30)
            stroke(100, 100, 100)
            rect(1, 148, 75, 25)
            rect(1, 130, 75, 15)
            rect(1, 115, 75, 10)
        if width * 0.1 + 300 < mouseX < width * 0.1 + 360 and height * 0.8 < mouseY < height * 0.8 + 60:
            index = 20
    noFill()
    strokeWeight(2)
    stroke(0)
    fill(255)
    rect(width * 0.1 + 300, height * 0.8, 60, 60)
    line(width * 0.1 + 315, height * 0.8 + 53, width * 0.1 + 355, height * 0.8 + 53)
    line(width * 0.1 + 315, height * 0.8 + 53, width * 0.1 + 305, height * 0.8 + 45)
    line(width * 0.1 + 330, height * 0.8 + 8, width * 0.1 + 305, height * 0.8 + 45)
    line(width * 0.1 + 330, height * 0.8 + 8, width * 0.1 + 355, height * 0.8 + 25)
    line(width * 0.1 + 335, height * 0.8 + 53, width * 0.1 + 355, height * 0.8 + 25)
    line(width * 0.1 + 317, height * 0.8 + 30, width * 0.1 + 341, height * 0.8 + 45)
    
       
    strokeWeight(2)
    stroke(0)
    noFill()
    rect(15, 260, 15, 15)
    ellipse(57.5, 267.5, 15, 15)
    noFill()
    strokeWeight(5)
    stroke(255)
    rect(5, 250, 35, 35)  
    rect(40, 250, 35, 35)
    
def mouseWheel(event):
    global radiuse
    a = event.getCount()
    radiuse += a
    
        
