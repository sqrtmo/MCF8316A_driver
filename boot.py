from machine import UART
import os

uart = UART(0, 230400)
os.dupterm(uart)