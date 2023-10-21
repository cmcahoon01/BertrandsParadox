from random import choices, random
from math import tan, sqrt, pi, sin, cos
from functools import reduce
from sys import argv


def compute_all_solutions(num_lines=1_000_000):
    if num_lines > 100_000:
        print("Computing", num_lines, "lines. This might take a while...")
    solutions = [("Connor's first Solution", get_lines_connor_first),
                 ("Connor's second Solution", get_lines_connor_second),
                 ("Ryan's first Solution", get_lines_ryan_first),
                 ("Ryan's second Solution", get_lines_ryan_second), ]
    for name, solution in solutions:
        lines = solution(num_lines)
        print(f"{name}: {get_ratio(lines) * 100:.3f}% less than sqrt(3)")


# Picks a random point anywhere, then a random slope that would connect the point with the circle
def get_lines_connor_first(num_lines, fidelity=1000):
    x_buckets = [(i + 1) / fidelity for i in range(fidelity)]  # x_buckets = [0.1, 0.2, 0.3, ..., 1.0]
    x_buckets = [-v for v in x_buckets[::-1]] + x_buckets  # x_buckets = [-1.0, -0.9, ..., 0.9, 1.0]
    probability = [special_equation(v) for v in x_buckets]

    slopes = choices(x_buckets, weights=probability, k=num_lines)
    intercepts = [(2 * random() - 1) * special_equation(x) for x in slopes]
    intercepts = [-slope * intercept for slope, intercept in zip(slopes, intercepts)]  # convert from x intercept to y intercept
    return list(zip(slopes, intercepts))


def special_equation(x):
    return sqrt(1 / (tan(pi / 2 * x) ** 2) + 1)


# picks a random angle, then a random intercept that keep the line in the circle
def get_lines_connor_second(num_lines):
    lines = []
    for _ in range(num_lines):
        angle = random() * 2 * pi
        slope = tan(angle)
        intercept = random() * 2 - 1  # random y intercept as if the angle was 0
        x, y = random_rotate_point(0, intercept, angle)  # rotate the point to the correct angle
        intercept = y - slope * x  # fix the y intercept
        lines.append((slope, intercept))
    return lines


# picks an x in the circle, then a random y for that x. Repeats to get a second point, and connects them to form a line
def get_lines_ryan_first(num_lines):
    points = []

    for _ in range(num_lines):
        x1 = random() * 2 - 1
        y1 = sqrt(1 - x1 ** 2)
        if random() < 0.5:
            y1 *= -1

        x2 = random() * 2 - 1
        y2 = sqrt(1 - x2 ** 2)
        if random() < 0.5:
            y2 *= -1
        if random() < 0.5:
            x1, y1 = y1, x1
        if random() < 0.5:
            x2, y2 = y2, x2

        # x1, y1 = random_rotate_point(0, 1, random() * 2 * pi)
        # x2, y2 = random_rotate_point(0, 1, random() * 2 * pi)
        points.append(((x1, y1), (x2, y2)))
    return convert_to_intercept_slope(points)


# picks a random point in the circle, then a random angle
def get_lines_ryan_second(num_lines):
    lines = []
    for _ in range(num_lines):
        x, y = 1, 1
        while x ** 2 + y ** 2 >= 1:
            x, y = random() * 2 - 1, random() * 2 - 1
        angle = random() * 2 * pi
        slope = tan(angle)
        intercept = y - slope * x
        lines.append((slope, intercept))
    return lines


def random_rotate_point(x, y, angle):
    return x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle)


def get_lengths(lines):
    lengths = []
    for slope, intercept in lines:  # using quadratic formula
        a = slope ** 2 + 1
        b = 2 * slope * intercept
        c = intercept ** 2 - 1
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        y1 = slope * x1 + intercept
        y2 = slope * x2 + intercept
        distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        lengths.append(distance)
    return lengths


def get_ratio(lines):
    return reduce(lambda total, length: total + 1 if length > sqrt(3) else total, get_lengths(lines), 0) / len(lines)


def convert_to_intercept_slope(points):
    new_lines = []
    for (x1, y1), (x2, y2) in points:
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        new_lines.append((slope, intercept))
    return new_lines


if __name__ == '__main__':
    if len(argv) > 1:
        compute_all_solutions(int(argv[1]))
    else:
        compute_all_solutions()
