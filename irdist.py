#This uses modified code credited to Jeremy Blythe at:
#https://github.com/jerbly/Pi/blob/master/distance-screen.py
import mcp3008

#Reads from the mcp3008 chip, and outputs the calculated distance from the
#SHARP IR Sensor
def get_distance(mcp3008_ch):
    num_samples = 10
    r = []
    for i in range (0,num_samples):
        r.append(mcp3008.readadc(mcp3008_ch))
    a = sum(r)/float(num_samples)
    v = (a/1023.0)*3.3
    d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
    return int(round(d))

#This method involves using mcp3008 with the SPI drivers.
#No GPIO are used, and all sensors are connected to
#mcp3008 channels 0-7
