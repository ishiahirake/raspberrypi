#!/usr/bin/env python

from gpiozero import PWMLED
from signal import pause


def breathing_light(pin: int, fade_in_time: float = 1, fade_out_time: float = 1):
    """LED 呼吸灯.

    电路图: 同 001 https://crcit.net/c/6f31f46af16541528a91698b4ea109a1

    使用 PWMLED 即可简单的实现该功能.
    PWMLED 与 普通的 LED 对比, 可以更精细的控制 value 值.
    LED 的 value 值类型为 bool, 即只能是 True 或者 False.
    而 PWMLED 的 value 值类型为 float, 可以是 0 到 1 之间的任何值.

    Args:
        pin (int): 接有 LED 灯的管脚.
        fade_in_time (int, optional): 淡入时间, 单位秒. 默认 1.
        fade_out_time (int, optional): 淡出时间, 单位秒. 默认 1.
    """
    light = PWMLED(pin)
    light.pulse(fade_in_time=fade_in_time, fade_out_time=fade_out_time)


breathing_light(17)
pause()
