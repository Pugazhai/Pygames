import pygame
import sys
from pygame.locals import *
from time import sleep
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x, y = 200, 200
dir_x, dir_y = 1, 1
while True:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 13, 0)
    sleep(0.006)
    x += dir_x
    y += dir_y
    if x >= width or x <= 0:
        dir_x *= -1
    if y >= height or y <= 0:
        dir_y *= -1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
