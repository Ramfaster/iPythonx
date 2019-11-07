def circle(pi, radius):
    print("pi = ", pi)
    print("반지름 = ", radius)
    return pi * radius * 2

def calculate_volume(length, width, height):
    return length * width * height

if __name__ == '__main__':
    print(circle(3.14,3))
    print(calculate_volume(1,2,3))