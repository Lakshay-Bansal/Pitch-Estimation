# Pitch-Estimation
Pitch estimation can be performed with the different algorithm like YIN,
MPM, Cepstrum based, SIFT or a deep learning-based algorithm. In
this project we are using autocorrelation for pitch estimation as also used
in YIN algorithm. 

We obtain frames from speech signal either by sampling
it with by the rectangular or hamming window function. Number of frames
obtained after sampling depend upon the total samples present in the speech,
window size and hop length. Also, the size of each frame which is used for
pitch estimation is determined by window size and hop length will determine
the overlap from previous frame. We label each generated frame being voiced
or unvoiced based on frame energy calculated using discrete time signal
energy formula. We first normalised each frame energy and from plot of
normalised energy vs frame number, we take a value to threshold the frame
being voiced or unvoiced. We are estimating the pitch only for the voiced
frame. We calculate the autocorrelation only for voiced frame and then
calculate its period (using difference in indexes of peaks which give maximum
difference). The inverse of a period of voiced frame autocorrelation gives the
pitch for that frame. Program can also generate a .csv or a .txt file for a
purpose to store the obtained pitch value along with its label whether voiced
or unvoiced for future reference.

Function of different file used in project:
1. main.py - The file to be run to obtain pitch. It calls the generate_Frames.py, voicedFrame.py, pitch.py
in the sequence to perform pitch estimation.
3. generate_Frames.py - It have a enframe() function defined in it which generates the frame for speech signal. It generate frame those depend upon winsize,hoplength and wintype provided.
4. voicedFrame.py - This file have voiceSeg() function, which calculate the normalised frame energy plot. And also threshold the   
5. pitch.py

##Contact at below mail address in case of query:

t21011@students.iitmandi.ac.in
