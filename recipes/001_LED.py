#!/usr/bin/env python

from gpiozero import LED

"""
使用 GPIO 控制 LED 灯闪烁.

电路图: https://crcit.net/c/6f31f46af16541528a91698b4ea109a1
"""

light = LED(17)

# 默认的, blink 方法开启一个后台线程执行闪烁并让该函数的调用直接返回.
# 但是函数的返回会导致脚本结束从而导致闪烁也停止.
# 因此需要将 background 设置为 False. (或者使用 pause)
#
# 可以通过
#
# - `on_time`: 来指定灯亮的时间(秒), 默认 1
# - `off_time`: 来指定灯灭的时间(秒), 默认 1
# - `n`: 来指定闪烁的次数
light.blink(background=False)
# pause()

# version 2:
#
# from time import sleep
#
# while True:
#     light.on()
#     sleep(1)
#     light.off()
#     sleep(1)
