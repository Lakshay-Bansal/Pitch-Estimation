# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:06:04 2021

@author: lakshay
"""
import numpy as np
import matplotlib.pyplot as plt

def voiceSeg(frames):
    
    ## Calculating energy of each frame
    frameEng = []  
    for i in range(len(frames)):
        frameEng.append(round(sum(frames[i]**2), 2))
    
    normalisedFrameEng = np.round( frameEng/max(frameEng), 2)
    
    # print(normalisedFrameEng)
    plt.figure()
    plt.plot(range(1,len(frames)+1), normalisedFrameEng)    # Plotting Normalised Energy
    plt.xlabel("Frame Number")
    plt.ylabel("Normalised energy of each frame")
    plt.title("Frames Energy")
    plt.show()
    
    ## Asking user to enter the threshold value that he think best from the above plot
    ## "Normalised energy of each frame"
    threshold = float(input("---Provide a threshold value for frame classification as voiced or not \n Should be in a range of (0, 1): "))
    threshold = round(threshold, 2)
    
    # Generating Voice Segments from Audio
    frames_label = []
    voiceSeg = []
    
    for loc in range(len(normalisedFrameEng)):
        if normalisedFrameEng[loc] >= threshold :
            frames_label.append([frames[loc], 1])
        else:
            frames_label.append([frames[loc], 0])    # 0 to signify noise part                     
            
    return frames_label
