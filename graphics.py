from simulation import objList, simulate
import pygame
import sys
pygame.init()

size = width, height = 500, 500
black = 0, 0, 0
space = pygame.display.set_mode(size)
pygame.display.set_caption("Space")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

ball = pygame.image.load("ball.png")
body_list = objList()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    space.fill(black)
    for body in body_list:
        space.blit(ball, (body.p[0],body.p[1]))
    pygame.display.update()
    body_list = simulate()
