from flask import Flask, request
import pylaunchpad as lp
import bitmaps as bmp
import time
import sys
from random import choice

pad = lp.get_me_a_pad()
pad.reset()
    
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    try:
        f=request.args
        cmd=f.get('cmd', default = 'missing cmd', type = str)
        x=f.get('x', default = 0, type = int)
        y=f.get('y', default = 0, type = int)
        if cmd=='clear':
            pad.reset()
        elif cmd=='set_led_xy_by_colour':
            pad.set_led_xy_by_colour(x, y, pad.colours['white'])
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