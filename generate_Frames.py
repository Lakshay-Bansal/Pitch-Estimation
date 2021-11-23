# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:57:32 2021
@author: lakshay
"""
import numpy as np

def enframe(x,winsize,hoplength,fs,wintype = 'rect'):
    frames = []
    
    winSam = int(fs*winsize)    # No. of samples in window
    hopSam = int(fs*hoplength)  # Frame shift size
    step = winSam - hopSam       # Frame size
    
    # numOfFrames = int( (len(x) - winSam) // hopSam) + 1
    numOfFrames = min ( int( (len(x) - winSam) // hopSam) + 1 , len(x)//winSam) # No. of possible frame from signal
    # print(numOfFrames)
    
    window = np.ones(winSam)   # Deafault rectangular window
    if wintype == 'hamm':
        window = np.hamming(winSam)
    
    # print(step)
    frames.append( x[0:winSam]*window ) # For first frame only
    
    for i in range(1, numOfFrames):
        startIndx = i*winSam - step
        endIndx = startIndx + winSam
        frames.append( x[startIndx:endIndx]*window )     # Appending frames to the frames
        # plt.figure(i+2)
        # plt.stem(range(len(step)), frames[i], 'o')
        # plt.title(i+1)
        # n = input("Press enter for new plot")
    return frames, numOfFrames



    


