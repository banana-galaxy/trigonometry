import pygame, math

class trig():
    def __init__(self, width, height, mouse, theme):
        self.winWidth = width
        self.winHeight = height
        self.mouse = mouse
        self.circleR = width//3
        self.circleThick = height//150
        self.theme = theme
        self.angle = 45
        self.xLength = math.cos(math.radians(self.angle))
        self.yLength = math.sin(math.radians(self.angle))
        self.circleX = self.winWidth//3-(self.circleR//2)
        self.circleY = self.winHeight//2-(self.circleR//2)
        self.middleX = self.circleX + self.circleR//2
        self.middleY = self.circleY + self.circleR//2

    def draw_circle(self, screen):

        # drawing circle
        pygame.draw.ellipse(screen, self.theme["lines"], [self.circleX, self.circleY, self.circleR, self.circleR], self.circleThick)
        # drawing line
        endX = self.middleX+(math.cos(math.radians(self.angle))*self.circleR//2)
        endY = self.middleY+(math.sin(math.radians(self.angle))*self.circleR//2)
        pygame.draw.line(screen, self.theme["lines"], [self.middleX, self.middleY], [endX, endY], self.circleThick)
        # pythagoras
        dX = endX - self.middleX
        dY = endY - self.middleY
        distance = math.sqrt(dX**2 + dY**2)
        font = pygame.font.SysFont('Calibri', self.winHeight//25, False, False)
        text = font.render(f"{dX}^2 + {dY}^2 = {int(distance)}^2", True, self.theme["text"])
        screen.blit(text, [self.circleX+self.circleR+self.circleR/10, self.circleY])
        # cosine
        if self.angle < 0:
            angle = -self.angle
        else:
            angle = (180-self.angle)+180
        cos = math.cos(math.radians(self.angle))
        text = font.render("cos({:.2f}) = {:.2f}".format(angle, cos), True, self.theme["text"])
        screen.blit(text, [self.circleX+self.circleR+self.circleR/10, self.circleY+self.winHeight//20])
        # sine
        sin = math.sin(math.radians(self.angle))
        text = font.render("sin({:.2f}) = {:.2f}".format(angle, sin), True, self.theme["text"])
        screen.blit(text, [self.circleX+self.circleR+self.circleR/10, self.circleY+self.winHeight//20*2])
        # atan2
        text = font.render("atan2({:.2f}, {:.2f}) = {:.2f}".format(dY, dX, angle), True, self.theme["text"])
        screen.blit(text, [self.circleX+self.circleR+self.circleR/10, self.circleY+self.winHeight//20*3])

    def changeTheme(self, newTheme):
        self.theme = newTheme

    def update(self, mouse):
        self.mouse = mouse
        dX = mouse[0] - self.middleX
        dY = mouse[1] - self.middleY
        rad = math.atan2(dY, dX)
        distance = math.sqrt(dX**2 + dY**2)
        if distance <= self.circleR//2:
            self.angle = math.degrees(rad)
            self.xLength = math.cos(math.radians(self.angle))
            self.yLength = math.sin(math.radians(self.angle))

    def draw(self, screen):
        self.draw_circle(screen)