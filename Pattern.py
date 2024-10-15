import time

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"


# CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222, ind=0):
    line = " " * length
    if ind == 8:
        print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset*2 + 2 - ind)}{SET_COLOR}{color}m{(length - 2) * " "}{END}",\
              f"{' ' * (offset*2-12)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset*2 + 2 - ind*2)}{SET_COLOR}{color}m{(length - 2) * " "}{END}",\
              f"{' ' * (offset*2-12)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind*2)}{SET_COLOR}{color}m{(length - 2) * " "}{END}",
              f"{' ' * (offset-12)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind*2)}{SET_COLOR}{color}m{(length - 8) * " "}{END}", sep='')
    else:
        print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset*2-6)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset*2-6)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset*2-6)}{SET_COLOR}{color}m{line}{END}",
              f"{' ' * (offset + 2 - ind)}{SET_COLOR}{color}m{line}{END}", sep='')


def draw_romb():
    size = 16
    offset = size // 2

    step = 1
    length = 1

    # print(size, center, offset)

    color = 218

    for i in range(8):
        draw_line(offset + 1, length + 1, color, ind=-1)
        draw_line(offset - 2, 8, color, ind=2)
        draw_line(offset - 4, 12, color, ind=4)
        draw_line(offset - 6, 16, color, ind=8)
        draw_line(offset - 4, 12, color, ind=4)
        draw_line(offset - 2, 8, color, ind=2)
        draw_line(offset + 1, length + 1, color, ind=-1)

        length = 1
        offset = size // 2


if __name__ == "__main__":
    draw_romb()
