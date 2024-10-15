import os
import time

frames = ['   *   *   ', '  *** ***  ', ' ********* ', '  ******* ', '   *****  ', '    ***   ', '     *    ']


def draw_lines(frame_number=7):
    for i in range(frame_number):
        if i ==frame_number:
            print(frames[i], end='\r')
        else: print(frames[i])


def animation():
    for frame_number in [3,5,7]:
        draw_lines(frame_number)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        animation()
