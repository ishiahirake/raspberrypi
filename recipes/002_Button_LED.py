#!/usr/bin/env python

from gpiozero import LED, Button
from signal import pause

"""
使用按钮控制 LED 灯.

电路图: https://crcit.net/c/bbc7f5e55baa49118deec4110d3e4275
"""

light = LED(17)
button = Button(18)

button.when_activated = light.toggle

pause()
