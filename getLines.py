from random import choices, random
from math import tan, sqrt, pi, sin, cos


def equation(x):
    return sqrt(1 / (tan(pi / 2 * x) ** 2) + 1)


def get_lines(num_lines, fidelity=1000):
    x_buckets = [(i + 1) / fidelity for i in range(fidelity)]  # x_buckets = [0.1, 0.2, 0.3, ..., 1.0]
    x_buckets = [-v for v in x_buckets[::-1]] + x_buckets  # x_buckets = [-1.0, -0.9, ..., 0.9, 1.0]
    probability = [equation(v) for v in x_buckets]

    slopes = choices(x_buckets, weights=probability, k=num_lines)
    intercepts = [(2 * random() - 1) * equation(x) for x in slopes]
    return list(zip(intercepts, slopes))


def get_lines_ryan(num_lines):
    lines = []

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
        lines.append(((x1, y1), (x2, y2)))
    return lines


def random_rotate_point(x, y, angle):
    return x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle)


def get_average_length(lines):
    total = 0
    for (x1, y1), (x2, y2) in lines:
        total += 1 if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) > sqrt(3) else 0
    return total / len(lines)


if __name__ == '__main__':
    get_lines(1)
