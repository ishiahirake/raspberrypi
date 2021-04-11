#!/usr/bin/env python


from time import sleep
from gpiozero import RGBLED


def wait(n: int = 1):
    sleep(n)


def demonstrate(light: RGBLED):
    # RGB 单色控制, RGBLED 支持 PWM, 在开启(默认启用)的情况下, 可以精细的设置各 RGB 的值
    light.red = 0.5
    wait()
    light.red = 1
    wait()

    # 使用 color 设置颜色
    light.color = (0, 1, 0)
    wait()

    light.color = (1, 0, 1)
    wait()
    light.color = (1, 1, 0)
    wait()
    light.color = (0, 1, 1)
    wait()

    light.color = (1, 1, 1)
    wait()
    light.color = (0, 0, 0)
    wait()


def demonstrate_rgb_led(red: int, green: int, blue: int):
    """LED 演示.

    电路图: https://crcit.net/c/5a39694e5e23438ba462c3242ed57c02

    RGB LED, 顾名思义, 就是能同时显示 RGB 三种颜色的 LED 灯.
    RGB LED 有4个管脚, 长度如下所示:

    --      Blue (最短)
    ---     Green
    ----    Cathode (最长)
    ---     RED

    RGB LED 可以精细的控制各个颜色的值(0~1),
    理论上通过组合 RGB 可以显示很多种颜色, 但实际的显示效果可能不会那么理想.
    (如: (1, 1, 1) 理论上应该显示白色, 但实际上看到的是淡绿色)

    Args:
        red (int): RGB LED 红色所接的管脚.
        green (int):RGB LED 绿色所接的管脚.
        blue (int): RGB LED 蓝色所接的管脚.
    """
    light = RGBLED(red=red, green=green, blue=blue)
    while True:
        demonstrate(light)


demonstrate_rgb_led(26, 19, 13)
