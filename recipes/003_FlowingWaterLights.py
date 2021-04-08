#!/usr/bin/env python

from time import sleep
from signal import pause

from gpiozero import LED


def flowing_water_lights(pins, on_time=0.1):
    """流水灯.

    电路图: https://crcit.net/c/cbb36203c2214ef6a8f80dcec26f15fb

    Args:
        pins (list<int>): 接有流水灯的管脚. 按这里指定的顺序播放.
        on_time (float, optional): 每个灯亮的时间, 单位秒. 默认 0.1.
    """
    lights = [LED(pin) for pin in pins]
    while True:
        for light in lights:
            light.on()
            sleep(on_time)
            light.off()


flowing_water_lights([21, 20, 16, 17, 13, 19, 26])
