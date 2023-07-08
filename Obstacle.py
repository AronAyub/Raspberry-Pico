from machine import Pin,UART
from time import sleep

Ob_in=1
P_in=Pin(Ob_in, Pin.IN, Pin.PULL_UP)

while True:
    if P_in.value():
        print("Obstacle Found")
    else:
        print("No Obstacle")
    sleep(1)
    print(P_in.value())