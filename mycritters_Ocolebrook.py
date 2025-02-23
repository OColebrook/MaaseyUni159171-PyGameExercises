import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
brown = (125, 100, 100)
orange = (255, 165, 0)
grey = (165,165,165)
aqua = (0, 128,128)



class Caterpillar:

    color_scheme = [green, red, yellow, purple, brown]
    color_scheme2 = [black, white, orange, grey, aqua]



    def __init__(self):
        x = random.randrange(50, 950)
        y = random.randrange(600, 950)
        self.xcoord = x
        self.ycoord = y
        size = random.randrange(1,4)
        self.color = random.choice(Caterpillar.color_scheme)
        self.size1 = size

    def change_color(self):
        if Caterpillar.color_scheme is Caterpillar.color_scheme1:
            Caterpillar.color_scheme = Caterpillar.color_scheme2

        if Caterpillar.color is Caterpillar.color_scheme2:
            Caterpillar.color_scheme = Caterpillar.color_scheme1



    def draw_critter(self, screen):

        x = self.xcoord
        y = self.ycoord
        color = self.color
        size = self.size1
        pygame.draw.ellipse(screen, color, [x*size, y, 40*size, 45*size])
        pygame.draw.ellipse(screen, color, [(x+40)*size, y, 50*size, 45*size])
        pygame.draw.ellipse(screen, color, [(x+90)*size, y, 50*size, 45*size])
        pygame.draw.ellipse(screen, black, [(x + 6)*size, y + 10, 10*size, 15*size])
        pygame.draw.ellipse(screen, black, [(x + 24)*size, y + 10, 10*size, 15*size])
        pygame.draw.line(screen, black, ((x + 11)*size, y + 1), ((x + 9)*size, y - 10), 3)
        pygame.draw.line(screen, black, ((x + 25)*size, y + 1), ((x + 26)*size, y - 10), 3)
        pygame.draw.line(screen, black, ((x + 65)*size, y + (55*size)), ((x + 61)*size, y + (45*size)), 1)
        pygame.draw.line(screen, black, ((x + 57)*size, y + (55*size)), ((x + 61)*size, y + (45*size)), 1)
        pygame.draw.line(screen, black, ((x + 120)*size, y + (55*size)), ((x + 115)*size, y + (45*size)), 1)
        pygame.draw.line(screen, black, ((x + 110)*size, y + (55*size)), ((x + 115)*size, y + (45*size)), 1)









class Butterfly:

    color_scheme1 = [green, red, yellow, purple, brown]
    color_scheme2 = [black, white, orange, grey, aqua]
    color_scheme = color_scheme1


    def __init__(self):
        x = random.randrange(50, 950)
        y = random.randrange(50, 500)
        self.xcoord = x
        self.ycoord = y
        color = random.choice(Butterfly.color_scheme)
        size = random.randrange(1,4)
        self.color1 = color
        self.size1 = size




    def draw_critter(self, screen):

        x = self.xcoord
        y = self.ycoord
        color = self.color1
        size = self.size1
        pygame.draw.ellipse(screen, color, [x*size, y, 40*size, 50*size])
        pygame.draw.ellipse(screen, color, [(x+38)*size, y, 20*size, 31*size])
        pygame.draw.ellipse(screen, color, [(x-18)*size, y, 20*size, 31*size])
        pygame.draw.ellipse(screen, color, [(x+36)*size, y+(25*size), 20*size, 31*size])
        pygame.draw.ellipse(screen, color, [(x-16)*size, y+(25*size), 20*size, 31*size])
        pygame.draw.ellipse(screen, black, [(x + 6)*size, y + 10, 10*size, 15*size])
        pygame.draw.ellipse(screen, black, [(x + 24)*size, y + 10, 10*size, 15*size])
        pygame.draw.line(screen, black, ((x + 11)*size, y + 1), ((x + 9)*size, y - 10), 3)
        pygame.draw.line(screen, black, ((x + 25)*size, y + 1), ((x + 26)*size, y - 10), 3)

    def change_color(self):
        if Butterfly.color is Butterfly.color_scheme1:
            Butterfly.color_scheme = Butterfly.color_scheme2

        if Butterfly.color is Butterfly.color_scheme2:
            Butterfly.color_scheme = Butterfly.color_scheme1
