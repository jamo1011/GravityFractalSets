#!/usr/bin/env python3


####################### Initialization ################################

import time
startTime = time.time()

#libraries
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np
import csv


######################### Definitions ################################

def run(dt=0.01,
        numOfIterations=100,
        starLocations=[0+0*1j],
        imageSize=(2,3),
        xlim_=(-1,1),
        ylim_=(-0.5625,0.5625),
        G=1):       #gravitational constant

    #initialize
    numOfPoints = imageSize[0]*imageSize[1]
    pos = np.zeros(numOfPoints,dtype=np.complex_)
    X = np.linspace(xlim_[0], xlim_[1], imageSize[0])
    Y = np.linspace(ylim_[0], ylim_[1], imageSize[1])
    for i in range(0,len(Y)):
        for k in range(0,len(X)):
            pos[imageSize[0]*i+k] = X[k] + 1j*Y[i]
    vel = np.zeros(numOfPoints,dtype=np.complex_)

    t = time.localtime()
    date = str(t.tm_sec) + '_' + str(t.tm_hour) + '_' + str(t.tm_mday) + '_' + str(t.tm_mon,) + '_' + str(t.tm_year)
    print(date)
    filename = date + '.csv'
    print('filename: {}'.format(filename))
    print('Initialization Time: {}'.format(time.time()-startTime))

    #Open file to write 
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['########Parameters########'])
        writer.writerow(['dt', dt])
        writer.writerow(['starLocations', starLocations])
        writer.writerow(['imageSize', imageSize])
        writer.writerow(['xlim_', xlim_])
        writer.writerow(['ylim_', ylim_])
        writer.writerow(['G', G])
        writer.writerow(['########Iterations########'])
        #Loop
        for i in range(0,numOfIterations):

            #Gravity equations
            acc = np.zeros(numOfPoints)
            for loc in starLocations:
                r = loc-pos
                acc = acc+G*r
            vel = vel+acc*dt
            pos = pos+vel*dt
            #print(pos)

            #Append pos and vel to file
            writer.writerow(pos)
            writer.writerow(vel)

    print('Run Time: {}'.format(time.time()-startTime))

run()
