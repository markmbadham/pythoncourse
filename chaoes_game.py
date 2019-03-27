# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:52:43 2014

@author: mark
"""

import random
import numpy as np
import time
import matplotlib.pyplot as pl #!
import numpy as np

def Sierpinski_Chaos(gp=None,n=None):
    """ This Chaos game shows how randomness can lead to structure:
    1. 3 points have to be drawn in the plane
    2. Mark a triangle with these points with pl.plot
    3. draw a random point outside this triangle- this is the first 'Game-Point(gp)'
    Repeat til n:
    4. Choose a randomly a base-point out of the three corner points 
    5. Build the vector between the 'Game-Point' and the randomly chosen base-point
    and mark a point (scatter) half way to the base-point
    Created 08-29-2014 by Pierre Noire """ 
    
    #1.,2.
    pl.plot([0,4,2,0],[0,0,4,0])
    pl.xlim(0,4)
    pl.ylim(0,4)
    base_points=[[0,0],[4,0],[2,4]]
    if gp==None:
        gp=np.array([5,5])#starting game_point
    if n==None:
        n=500 #number of iterations
    for n in range(500):
        gp_log=gp.copy()
        pl.scatter(gp[0],gp[1],lw='0',s=20)#3.
        pl.xlim(0,4)#!
        pl.ylim(0,4)#!
        pl.draw()#!
        pl.show()
        #display.clear_output(wait=True)#!
        #display.display(pl.gcf())#!
        time.sleep(0.0000005)#!
        #4
        fort_wheel=random.choice(base_points)
        rand_base=np.array(fort_wheel)
        #5
        gp=gp-1.0/2*(gp-rand_base)
        gp_log=np.concatenate((gp_log,gp))
        #(gp-rand_base) is 
        #"direction-vector" starting from the gp and just walking half way leads to new gp    
    return gp_log
Sierpinski_Chaos()