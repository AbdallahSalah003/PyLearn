class Ball:
    def __init__(self,canvas,x,y,d,xVel,yVel,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,d,d,fill=color)
        self.xVel = xVel
        self.yVel = yVel
    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVel = - self.xVel
        if (coordinates[3] >= (self.canvas.winfo_width()) or coordinates[1] < 0):
            self.yVel = - self.yVel
        self.canvas.move(self.image,self.xVel,self.yVel)