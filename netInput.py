import socket
import sys
import pylaunchpad as lp
import time

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
#input("Press Eter to continue...")
#pad.in_ports.cancel_callback()
while True:
    time.sleep(100000)


if __name__ == "__main__":
    #launchpad = lp.get_me_a_pad()
    pad.reset()