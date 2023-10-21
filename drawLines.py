from computeLines import get_lines_connor_first, get_lines_connor_second, get_lines_ryan_first, get_lines_ryan_second, get_ratio
import pygame
from math import tan, pi
from random import randrange
from sys import argv


def draw_lines(num_lines=100):
    lines = get_lines_connor_first(num_lines)
    print(f"Percent of lines > sqrt(3): {get_ratio(lines) * 100}%")
    colors = [(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for _ in lines]

    pygame.init()
    height, width = 800, 800
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Lines')
    clock = pygame.time.Clock()

    center = (height // 2, width // 2)
    scaling = height // 4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), center, scaling, 2)

        for (slope, intercept), color in zip(lines, colors):
            x1 = 0
            y1 = width // 2 * -slope + intercept * scaling + height // 2
            x2 = width
            y2 = width // 2 * slope + intercept * scaling + height // 2
            pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    if len(argv) > 1:
        draw_lines(int(argv[1]))
    else:
        draw_lines()
