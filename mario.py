"""
Start of an arduino project 8*8 running mario project
"""
import pylaunchpad as lp
import time

def arduino_map(x, in_min, in_max, out_min, out_max):
    """
    Python equivalent of the Arduino map function
    :param x:
    :param in_min:
    :param in_max:
    :param out_min:
    :param out_max:
    :return:
    """
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


# Bitmaps from https://github.com/druckgott/neomatrix/blob/master/arduino_neo_matrix_image.ino
# Data is in 4bit RGB format, so limited colours

mario = [[0x000, 0x000, 0x000, 0x50F, 0x50F, 0x50F, 0xEEF, 0x000],
         [0x50F, 0x50F, 0x50F, 0x50F, 0x50F, 0x000, 0x000, 0x000],
         [0x000, 0x000, 0x35A, 0xACF, 0x35A, 0x000, 0xACF, 0x000],
         [0xACF, 0x35A, 0x35A, 0xACF, 0xACF, 0x35A, 0x000, 0x000],
         [0x000, 0x000, 0x000, 0x35A, 0xACF, 0xACF, 0xACF, 0x000],
         [0x000, 0x0AF, 0xFA2, 0xFA2, 0x2FF, 0x50F, 0x50F, 0x000],
         [0xEEF, 0x000, 0xFA2, 0xFA2, 0xFA2, 0xFA2, 0x532, 0x978],
         [0x000, 0x527, 0x000, 0x000, 0x000, 0x35A, 0x000, 0x000]]

mario_2 = [[0x000, 0x000, 0x000, 0x50F, 0x50F, 0x50F, 0xEEF, 0x000],
           [0x50F, 0x50F, 0x50F, 0x50F, 0x50F, 0x000, 0x000, 0x000],
           [0x000, 0x000, 0x35A, 0xACF, 0x35A, 0x000, 0xACF, 0x000],
           [0xACF, 0x35A, 0x35A, 0xACF, 0xACF, 0x35A, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0x35A, 0xACF, 0xACF, 0xACF, 0x000],
           [0x000, 0x532, 0xFA2, 0x2FF, 0x50F, 0x50F, 0x000, 0x000],
           [0x000, 0x000, 0x50F, 0xEEF, 0xFA2, 0xFA2, 0x532, 0x000],
           [0x000, 0x000, 0x527, 0x35A, 0x35A, 0x000, 0x000, 0x000]]

mario_3 = [[0x000, 0x000, 0x000, 0x50F, 0x50F, 0xEEF, 0x50F, 0x000],
           [0x50F, 0x50F, 0x50F, 0x50F, 0x50F, 0x000, 0x000, 0x000],
           [0x000, 0x000, 0xACF, 0x35A, 0x000, 0xACF, 0x000, 0x000],
           [0x35A, 0xACF, 0x35A, 0x35A, 0xACF, 0xACF, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0xACF, 0xACF, 0xACF, 0xACF, 0x000],
           [0x000, 0x0AF, 0xFA2, 0xFA2, 0x2FF, 0x50F, 0x50F, 0x000],
           [0xEEF, 0x000, 0xFA2, 0xFA2, 0xFA2, 0xFA2, 0x532, 0x978],
           [0x000, 0x000, 0x35A, 0x000, 0x000, 0x527, 0x000, 0x000]]

mario_4 = [[0x000, 0x000, 0x000, 0x50F, 0x50F, 0xEEF, 0x50F, 0x000],
           [0x50F, 0x50F, 0x50F, 0x50F, 0x50F, 0x000, 0x000, 0x000],
           [0x000, 0x000, 0xACF, 0x35A, 0x000, 0xACF, 0x000, 0x000],
           [0x35A, 0xACF, 0x35A, 0x35A, 0xACF, 0xACF, 0x000, 0x000],
           [0x000, 0x50F, 0x50F, 0xACF, 0xACF, 0xACF, 0xACF, 0x000],
           [0xEEF, 0x0AF, 0xFA2, 0xFA2, 0x2FF, 0x50F, 0x000, 0xEEF],
           [0x000, 0x527, 0xFA2, 0xFA2, 0xFA2, 0xFA2, 0x532, 0x000],
           [0x000, 0x35A, 0x000, 0x000, 0x000, 0x000, 0x000, 0x000]]

hertz_1 = [[0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x0BF, 0x0BF, 0x000],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x00F, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x00F, 0x00F, 0x00F, 0x00F, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x00F, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000],
           [0x000, 0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x000]]

hertz_2 = [[0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x0BF, 0x0BF, 0x000],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x00F, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x00F, 0x00F, 0x00F, 0x00F, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x00F, 0x0BF, 0x0BF, 0x0BF],
           [0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000],
           [0x000, 0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x000]]

hertz_3 = [[0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x0BF, 0x0BF, 0x000],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x5A0, 0x0BF, 0x0BF],
           [0x0BF, 0x5A0, 0x5A0, 0x5A0, 0x5A0, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x5A0, 0x0BF, 0x0BF],
           [0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000],
           [0x000, 0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x000]]

hertz_4 = [[0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x0BF, 0x0BF, 0x000],
           [0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF],
           [0x0BF, 0x0BF, 0xBBE, 0x0BF, 0x0BF, 0x0BF, 0xEA0, 0x0BF],
           [0xEA0, 0xEA0, 0xEA0, 0xEA0, 0x0BF, 0x0BF, 0xBBE, 0x0BF],
           [0x0BF, 0xBBE, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0xEA0, 0x0BF],
           [0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000],
           [0x000, 0x000, 0x0BF, 0x0BF, 0x0BF, 0x0BF, 0x000, 0x000],
           [0x000, 0x000, 0x000, 0x0BF, 0x0BF, 0x000, 0x000, 0x000]]

smiley = [[0x000, 0x000, 0x000, 0x000, 0x000, 0x000, 0x000, 0x000],
          [0x000, 0x000, 0x07F, 0x00F, 0x00F, 0x07F, 0x000, 0x000],
          [0x000, 0x0EF, 0x0FF, 0x07F, 0x07F, 0x0EF, 0x0FF, 0x000],
          [0x000, 0x0F3, 0x000, 0x0DF, 0x0DF, 0x000, 0x0F3, 0x000],
          [0x000, 0xFB0, 0x0F3, 0x0FA, 0x0FA, 0x0F3, 0xFB0, 0x000],
          [0x000, 0xF15, 0xFE0, 0x000, 0x000, 0xFE0, 0xF15, 0x000],
          [0x000, 0x000, 0xF15, 0xFB0, 0xFB0, 0xF15, 0x000, 0x000],
          [0x000, 0x000, 0x000, 0x000, 0x000, 0x000, 0x000, 0x000]]

frames = [mario, mario_2, mario_3, mario_4]


def main():
    pad = lp.get_me_a_pad()
    # frames = [hertz_1, hertz_2, hertz_3, hertz_4]
    # frames = [smiley]
    for _ in range(20):
        for frame in frames:
            for y, row in enumerate(frame, 1):
                for x, col in enumerate(row):
                    color = int(col)

                    b = (color & 0xF00) >> 8
                    g = (color & 0x0F0) >> 4
                    r = color & 0x00F
                    # Scale up the colour range to the Launchpad 6 bits format
                    b = arduino_map(b, 0, 15, 0, 63)
                    g = arduino_map(g, 0, 15, 0, 63)
                    r = arduino_map(r, 0, 15, 0, 63)

                    pad.set_led_xy(x, y, r, g, b)
            time.sleep(.02)

if __name__ == "__main__":
    main()
