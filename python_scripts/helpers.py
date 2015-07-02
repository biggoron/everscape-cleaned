import math
import binascii
#Cycling throught color cycle
#returns a #RRGGBB string in hexadecimal notation
#blue -> green -> red
def Color_cycle(i, freq):
    p = math.pi*2.0/3.0
    red = math.sin(freq*i) * 127 + 128
    green = math.sin(freq*i + p) * 127 + 128
    blue = math.sin(freq*i + 2.0 * p) * 127 + 128
    red_str = hex(int(red))[2:]
    if len(red_str)  == 1:
        red_str = '0'+red_str
    green_str = hex(int(green))[2:]
    if len(green_str)  == 1:
        green_str = '0'+green_str
    blue_str = hex(int(blue))[2:]
    if len(blue_str)  == 1:
        blue_str = '0'+blue_str
    return '#' + red_str + green_str + blue_str
    
def Distance(X1, Y1, Z1, X2, Y2, Z2):
    return math.sqrt((X1-X2)*(X1-X2)+(Y1-Y2)*(Y1-Y2)+(Z1-Z2)*(Z1-Z2))
def Distance(X1, Y1, X2, Y2):
    return math.sqrt((X1-X2)*(X1-X2)+(Y1-Y2)*(Y1-Y2))
