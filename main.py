# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 17:57:32 2021

@author: lakshay
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd


## Plot of spectrum of readed sound file
print("----Provide the address of file which you want to read----")
address = str(input("Address: ")).split('/')
address = ('\\').join(address)

speech, fs = sf.read(address)

t = np.array(np.linspace(0, len(speech), num = len(speech))) / fs

print("\n Sampling rate of signal is {0} Hz\n".format(fs))

plt.figure(1)
# plt.stem(n[0:1000], speech[0:1000], 'o')
plt.plot(t, speech)
plt.title("Spectrum of Sound File")
plt.xlabel("Time (in seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


## Add folder path in environment variable to import the user defined python file
## Check if the current working directory is present 
##In the available added path for python in system using below code
# import sys
# for p in sys.path:
#     print(p)

## Generating frames from speech
from generate_Frames import enframe

winsize = 18.5/1000    # winsize is 18.5 ms
hoplength = 10/1000  # hoplength is 10 ms   

print("----Would you like to enter your own window size and hop length----")
print("If not than the default values will be used, those are:")
print("Window Size = {0} ms and Hop Length = {1} ms".format(winsize*1000, hoplength*1000))
win_choice = str(input("Press Y or y, to provide your own values: "))
if win_choice == 'y' or win_choice == 'Y':
    winsize = float(input("Window Size: ")) / 1000     # For converting it in ms
    hoplength = float(input("Hop Length: ")) / 1000   
    
## Frames are generated in accordance of winsize and hoplength
print("\n----Default window for sampling is Rectangular----")
wintype = str(input("If ypu like to use Hamming window, Enter H or h : "))
if wintype == 'H' or wintype == 'h':
    frames, numOfFrames = enframe(speech,winsize,hoplength,fs, 'hamm')  
else:
    frames, numOfFrames = enframe(speech,winsize,hoplength,fs, 'rect')


## Finding voiced frame from the obtained frames
from voicedFrame import voiceSeg

frames_label = voiceSeg(frames)


## Find pitch only for voiced parts of speech
## Using autocorrelation method
from pitch import framePitch

# To see the plot of specific frame and its autocorrelation function
print("Enter frame number whose spectrum and autocorrelation you like to see")
print("\nFrame number should be less than {0} (Total availabel frame)".format(numOfFrames))
fnum = int(input())
if fnum > numOfFrames:
    print("#### You enter a inccorrect frame number  ####")
    print("Plot of deafault frame and its autocorrelation will be obtained")
    fnum = 29
pitch = framePitch(frames_label, fs, fnum)


## Generaing csv file having pitch and voived/unvoiced label   
data = []
for idx in range(len(pitch)):
    data.append([ pitch[idx], frames_label[idx][1] ])

data_csv = pd.DataFrame(data, columns = ["Pitch", "Voiced/Unvoiced"])

print("----Provide the address where you want to store pitch output----")
Outaddress = str(input()).split('/')
filename = str(input("Provide filename to store file: "))
Outaddress.append(filename)
Outaddress = ('\\').join(Outaddress)

print("\n----Enter your choice to generate the file format having pitch values----")
File_Choice = str(input("Enter c to generate .csv file and t for .txt file: "))

if File_Choice == 'c' or File_Choice == 'C':
    Outaddress = Outaddress + str(".csv")
    data_csv.to_csv(Outaddress, index=False)
elif File_Choice == 't' or File_Choice == 'T':
    Outaddress = Outaddress + str(".txt")
    data_csv.to_csv(Outaddress, index=True)
    # np.savetxt(r'C:\Users\laksh\Desktop\New\Project\Frame_Pitches.txt', data, delimiter=' | ', encoding = 'int8')
else:
    print("Please enter the correct format")
