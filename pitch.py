# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 22:15:16 2021

@author: lakshay
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import find_peaks

def framePitch(frames_label, fs, fnum):
    pitch = [ ]
    cnt = 1
    for fl in frames_label:
        frame = fl[0].copy()
        label  = fl[1]
        p_Hz = 0   # Pitch of single frame
        if(label == 1):
            ## Auto correlation
            acf = signal.correlate(frame, frame, method='auto')
            half_acf = acf[len(acf)//2:]
            peaks_locs, _ = find_peaks(half_acf, height=0)
            if fnum == cnt:
                plt.plot(frame, label = "Frame")
                plt.plot(half_acf, label = "ACF")
                plt.plot(peaks_locs, half_acf[peaks_locs], "x")
                plt.legend(["Frame", "ACF"])
                plt.xlabel("Number of Sample")
                plt.title("Frame " + str(fnum))
                plt.show()
                
            peaks_locs_diff = np.diff( np.pad(peaks_locs, (1,0), 'constant', constant_values=(0)) )
            try:
                p_Hz = fs / (max(peaks_locs_diff)*2)
            except ValueError:
                p_Hz = 0
            # t = int(fs/( np.argmax(half_acf[10:])+10) )
            # p.append(t)
        pitch.append(round(p_Hz, 2))
        cnt += 1
    return pitch
    
## Autocorrelation from scratch
# frame_len = len(sig)
# acf = np.array([np.dot(sig[0:frame_len-w],sig[w:frame_len])*(1-w/frame_len) for w in range(frame_len)])
# peaks_acf, _ = find_peaks(acf, height=0)    # Finding Peaks
# plt.figure()
# plt.plot(acf)
# plt.plot(peaks_acf, acf[peaks_acf], "x")
# plt.show() 
