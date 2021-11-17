# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:57:32 2021

@author: Lakshay
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

speech, fs = sf.read(r'C:\Users\laksh\Desktop\New\Lab9\Q4\should.wav')
# n = np.array(np.linspace(0, len(speech), num = len(speech)))
t = np.array(np.linspace(0, len(speech), num = len(speech))) / fs

print("Sampling rate of signal is {0} Hz".format(fs))

plt.figure(1)
# plt.stem(n[0:1000], speech[0:1000], 'o')
plt.plot(t, speech)
plt.title("Speech")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


def enframe(x,winsize,hoplength,fs,wintype = 'rect'):
    frames = []
    
    winSam = int(fs*winsize)    # No. of samples in window
    hopSam = int(fs*hoplength)  # Frame shift size
    
    numOfFrames = int( (len(x) - winSam) / hopSam) + 1  # No. of possible frame from signal

    window = np.ones(winSam - hopSam)   # Deafault rectangular window
    if wintype == 'hamm':
        window = np.hamming(winSam - hopSam)
    
    step = winSam - hopSam
    for i in range(numOfFrames):
        startIndx = i*step
        endIndx = (i+1)*step
        frames.append( x[startIndx:endIndx]*window )     # Appending frames to the frames
        # plt.figure(i+2)
        # plt.stem(range(len(step)), frames[i], 'o')
        # plt.title(i+1)
        # n = input("Press enter for new plot")
    return frames


winsize = 30/1000    # winsize is 30 ms
hoplength = 15/1000  # hoplength is 15 ms    

frames = enframe(speech,winsize,hoplength,fs, 'hamm')  

## Calculating energy of each frame
n = np.arange( fs*(winsize - hoplength) )  
frameEng = []  
 
for i in range(len(frames)):
    frameEng.append(round(sum(frames[i]**2), 2))

normalisedFrameEng = np.round( frameEng/max(frameEng), 2)

# print(normalisedFrameEng)
plt.figure(2)
plt.plot(range(1,len(frames)+1), frameEng/max(frameEng))    # Plotting Normalised Energy
plt.xlabel("Frames")
plt.ylabel("Normalised Energy")
plt.title("Frames Energy")
plt.show()

## Generating Voice Segments from Audio
threshold = 0.40
voiceSeg = []
voiceCnt  = 0  
prevVoiceSegPos = 0
for pos in range(len(normalisedFrameEng)):
    # print(prevVoiceSegPos, pos)       # For debugging
    nfe = normalisedFrameEng[pos]
    if (nfe > threshold ):
        if prevVoiceSegPos == pos-1:
            # list(voiceSeg[voiceCnt-1].extend(frames[pos])
            voiceSeg[voiceCnt-1].extend(frames[pos])
        else:
            voiceSeg.append(list(frames[pos]))    # Appending the respective frame with greater energy
            voiceCnt += 1
        prevVoiceSegPos = pos
        
## Writing Generated Voice Segments
for i in range(len(voiceSeg)):
    address = str("C:\\Users\\laksh\\Desktop\\New\\Lab9\\Q4\\") + str(i + 1) + str(".wav")
    sf.write(address, voiceSeg[i], samplerate = fs)
        
# sf.write(r'C:\Users\laksh\Desktop\New\Lab9\xyz.wav', xn, samplerate = fs) 
