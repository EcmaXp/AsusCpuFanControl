import sys, os
sys.path.append(os.path.join(__file__, ".."))

from asusfan import get_cpu_fan
from ipgapi import load_ipg
import ctypes
from time import sleep
import atexit
import array


def main():
    SCALE = 80
    MIN, MAX = 35, 95
    ON_TEMP = 0
    DIFF = MAX - MIN

    BSIZE = 100
    INTERVAL = 0.25

    if not ctypes.windll.shell32.IsUserAnAdmin():
        raise EnvironmentError("This program are require running as admin")

    ipg = load_ipg()
    fan = get_cpu_fan()

    @atexit.register
    def fan_shutdown(fan=fan):
        fan.restore()

    def get_temp():
        ipg.ReadSample()
        temp = ipg.GetTemperature(0)
        print("T", temp)
        return temp

    def cycle(value=None):
        if value is not None:
            print("R", value)
            fan.setCycle(value)
            return

        return fan.getCycle()

    i = 0
    rtfs = array.array("i", [0] * BSIZE)

    # reconfig
    SCALE = max(min(SCALE, 100), 0)
    
    with fan:
        pass
        
    while True:
        while True:
            rtfs[0] = temp = get_temp()
            if temp > ON_TEMP:
                break
                
            sleep(INTERVAL)
        
        with fan:
            while max(rtfs) >= MIN:
                for i in range(BSIZE):
                    temp = get_temp()
                    rtfs[i] = int((max(min(MAX, temp), MIN) - MIN) / DIFF * SCALE)
                    cycle(max(rtfs))
                    sleep(INTERVAL)
                    
                    

    return

if __name__ == "__main__":
    main()
