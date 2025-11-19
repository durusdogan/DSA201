class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.upperX = x1
        self.upperY = y1
        self.lowerX = x2
        self.lowerY = y2
        self.height = self.upperY - self.lowerY
        self.width = self.lowerX - self.upperX
    
    def __str__(self):
        res = "*" * self.width + "\n" # first line
        
        for i in range(self.height-2): # lines in the middle
            line_mid = "*" + " " * (self.width - 2) + "*\n"
            res += line_mid
        
        res += "*" * self.width + "\n" # last line
        return res

    def calcArea(self):
        return self.height * self.width

    def calcPerimeter(self):
        return 2 * (self.height + self.width)