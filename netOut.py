from flask import Flask, request
import pylaunchpad as lp
import bitmaps as bmp
import time
from random import choice

launchpad = lp.get_me_a_pad()
launchpad.reset()
    
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
 f=request.form
 cmd=f['cmd']
 if cmd=='clear':
  pad.reset()
 elif cmd=='set_led_xy_by_colour':
  x=int(f['x'])
  y=int(f['y'])
  pad.set_led_xy_by_colour(x, y, pad.colours['white'])
 return cmd


if __name__ == '__main__':
    #pad = lp.get_me_a_pad()	
    app.run()    