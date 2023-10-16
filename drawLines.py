from getLines import get_lines, get_lines_ryan, get_average_length
import pygame
from math import tan, pi
from random import randrange


# lines = get_lines_ryan(num_lines=1000000)
# print(get_average_length(lines))

lines = get_lines(num_lines=100)


pygame.init()
height, width = 800, 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Lines')
clock = pygame.time.Clock()

center = (height // 2, width // 2)
scaling = height // 4

print(center, scaling)

colors = [(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for _ in range(len(lines))]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), center, scaling, 2)

    for (intercept, slope), color in zip(lines, colors):
        x1 = 0
        y1 = (width//2 / scaling + intercept) * -slope * scaling + height//2
        x2 = width
        y2 = (width//2 / scaling - intercept) * slope * scaling + height//2
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)

    pygame.display.update()
    clock.tick(60)
