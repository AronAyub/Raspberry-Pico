from machine import Pin
import time

class Blink:
    def __init__(self, pin_no):
        self.pin_no=pin_no
        self.Led=Pin(self.pin_no,Pin.OUT)

    def blink_twice(self):
        for i in range(5):
            print(i)
            self.Led.value(1)
            time.sleep(0.5)
            self.Led.value(0)
            time.sleep(0.5)

    ,2qd2q2dc   

# blink1 = Blink(25)
# blink1.blink_twice()

#Write a class (think through )

# Method 1
 #set uart 0 to use
 #plus string to send 

#Method 2
    #You should be able to set/select another uart, which uart, b_rate, pins to use in uart,  the & which send string

#method 3, 
    # blink led 2 times

#method 4,
    #blink led 3 times 

#before you send blink led 2 times 
#after u send blink 3 times/
