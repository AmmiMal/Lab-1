import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, value=0):
    print(f"{value}{' ' * offset}*")
    print(" |")


def draw_function():
    size = 12
    center = size // 2
    offset = (size-1) *3

    step = 1
    length = 1

    # print(size, center, offset)

    colors = [222, 157]
    print(f" ^{END}")
    print(f" |{END}")
    for value in range(size, -1, -1):
        if value==0:
            pass
        else:
            draw_line(offset, value)

        offset-=3



        # length = 1
        # offset = size // 2

    axis_x = ''
    for i in range(1, size):axis_x+='--|'
    print(f"0|{axis_x}->{END}")
    numbers = ''
    for i in range(1, size):numbers+='  '+  str(i)
    print(f" 0{numbers}{END}")


if __name__ == "__main__":
    draw_function()
