import time

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(length_green=10, length=22, color=222, green=29):
    line = " " * 36
    print(f"{SET_COLOR}{green}m{" " * length_green}{END}", f"{SET_COLOR}{color}m{" " * length}{END}", sep="")


def draw_flag():
    step = 1
    length = 24
    length_green = 13
    green = 29
    draw_line(length_green, length, 220, green)
    draw_line(length_green, length, 220, green)
    draw_line(length_green, length, 220, green)
    draw_line(length_green, length, 220, green)
    draw_line(length_green, length, 220, green)
    draw_line(length_green, length, 9, green)
    draw_line(length_green, length, 9, green)
    draw_line(length_green, length, 9, green)
    draw_line(length_green, length, 9, green)
    draw_line(length_green, length, 9, green)


if __name__ == "__main__":
    draw_flag()
