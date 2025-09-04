def is_valid_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return (
        a + b > c and
        a + c > b and
        b + c > a and
        a > 0 and
        b > 0 and
        c > 0
    )

def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 2 or equilateral(sides)


def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3
