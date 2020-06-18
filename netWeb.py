from flask import Flask, request
import socket
import pylaunchpad as lp
import time

import pylaunchpad as lp
#import bitmaps as bmp
import time
import sys
from random import choice

host = socket.gethostname()
host = '192.168.1.7'
port = 12345
def sendInfo(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("sending to " + host + ":" + str(port))
    print("msg: " + msg)
    s.connect((host, port))
    s.sendall(str.encode(msg))
    s.close()

def callback(a,b):
    x=a[0]
    m=str(x[0]) + "," + str(x[1]) + "," + str(x[2])
    print(m)
    sendInfo(m)

pad = lp.get_me_a_pad()
pad.in_ports.set_callback(callback)
pad.reset()
#pad.set_led_xy_by_colour(0, 0, pad.colours['green'])
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    try:
        f=request.args
        cmd=f.get('cmd', default = 'missing cmd', type = str)
        x=f.get('x', default = 0, type = int)
        columns=f.get('columns', default = 0, type = int)
        y=f.get('y', default = 0, type = int)
        red=f.get('red', default = 0, type = int)
        char_data=f.get('char_data', default = "", type = str)
        char=f.get('char', default = "", type = str)
        green=f.get('green', default = 0, type = int)
        blue=f.get('blue', default = 0, type = int)
        clear=f.get('clear', default = "false", type = str)
        if cmd=='clear': pad.reset()
        elif cmd=='reset': pad.reset()
        elif cmd=='set_led_xy_by_colour': pad.set_led_xy_by_colour(x, y, pad.colours['white'])
        elif cmd=='set_led_xy': pad.set_led_xy(x, y, red, green, blue)
        elif cmd=='draw_char': pad.draw_char(char_data, x, y, columns, clear)
        elif cmd=='draw_letter': pad.draw_letter(char, x, y, columns, clear)
        elif cmd=='set_all_on': pad.set_all_on(red, green, blue)
        elif cmd=='paint_app': pad.paint_app()
        elif cmd=='set_all_on_slow': pad.paint_app(red, green, blue)
        print(cmd)
        
        return cmd
    except Exception as e:
        s = str(e)
        return ( "<p>Error: %s</p>" % s)
   
#@app.route('/')
#def hello():
#    return "Hello World!"

if __name__ == '__main__':
    #pad = lp.get_me_a_pad()	
    app.run(host='0.0.0.0', port=5000)    
