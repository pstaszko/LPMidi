import pylaunchpad as lp

if __name__ == "__main__":
    pad = lp.get_me_a_pad()
    pad.set_all_on_slow
    
    pad.reset()
