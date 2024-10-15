SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
green = 29

with open('sequence.txt', 'r') as f:
    file = f.readlines()
    file = [float(i.rstrip()) for i in file]


def draw_condition():
    couter_from_0_to_5, couter_from_minus5_to_0 = 0, 0
    file_capacity = len(file)
    for i in file:
        if 0 <= i <= 5:
            couter_from_0_to_5 += 1
        if -5 <= i <= 0:
            couter_from_minus5_to_0 += 1
    all_from_minus5_to5 = couter_from_minus5_to_0 + couter_from_0_to_5
    persent_minus5_0 = round(100 * couter_from_minus5_to_0 / all_from_minus5_to5)
    print("Numbers from -5 to 0, %")
    print(f"{SET_COLOR}{green}m{" " * persent_minus5_0}{END} {persent_minus5_0}%")
    print("Numbers from 0 to 5, %")
    print(f"{SET_COLOR}{green}m{" " * (100 - (persent_minus5_0))}{END} {100 - persent_minus5_0}%")


if __name__ == '__main__':
    draw_condition()
