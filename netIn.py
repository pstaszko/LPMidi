import socket
import sys
import pylaunchpad as lp
import time

host = socket.gethostname()
host = '127.0.0.1'
port = 12345
def sendInfo(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("trying " + host)
    #print("trying " + str(port))
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
input("Press Enter to continue...")
#for loop in range(20000000):
#    time.sleep(1)
pad.in_ports.cancel_callback()


if __name__ == "__main__":
    #launchpad = lp.get_me_a_pad()
    pad.reset()