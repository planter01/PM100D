# This is a sample Python script to read from PM100D (thorlabs)
# sudo chmod 666 /dev/usbtmc0

import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def PM100D_reading():
    print(power_meter.read)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from ThorlabsPM100 import ThorlabsPM100, USBTMC
    inst = USBTMC(device="/dev/usbtmc0")
    power_meter = ThorlabsPM100(inst=inst)

    for x in range(200):
        PM100D_reading()
        time.sleep(0.1)



git
