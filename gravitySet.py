#!/usr/bin/env python3

import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np
import csv
from PIL import Image

class GravitySet:

    def run(self):
        startTime = time.time()

        #initialize
        pos_temp = np.zeros(self.numOfPoints,dtype=np.complex_)
        X = np.linspace(self.xlim_[0], self.xlim_[1], self.imageSize[0])
        Y = np.linspace(self.ylim_[0], self.ylim_[1], self.imageSize[1])
        for i in range(0,len(Y)):
            for k in range(0,len(X)):
                pos_temp[self.imageSize[0]*i+k] = X[k] + 1j*Y[i]
        vel_temp = np.zeros(self.numOfPoints,dtype=np.complex_)

        #Loop
        print('Running Simulation...')
        acc_temp = np.zeros(self.numOfPoints,dtype=np.complex_)
        for i in range(0,self.numOfIterations):

            #Gravity equations
            acc_temp = acc_temp*0
            for loc in self.starLocations:
                r = loc-pos_temp
                mag = np.absolute(r)
                temp = self.G*r/(mag*mag*mag)
                acc_temp = acc_temp+temp
            vel_temp = vel_temp+acc_temp*self.dt
            pos_temp = pos_temp+vel_temp*self.dt

            if self.test:
                self.posArr[:,i] = pos_temp

            #check if point escaped
            self.results[np.bitwise_and(self.results==0 , np.absolute(pos_temp) > 5)] = i  #change 5 if needed

            print('{} / {} iterations ran'.format(i, self.numOfIterations), end='\r')

        if not self.test:
            self.posArr = pos_temp

        self.results[self.results==0] = np.max(self.results)
        print('Run time: {}'.format(time.time()-startTime))

        return 0

    def __init__(self,
            dt=0.01,
            numOfIterations=100,
            starLocations=[0+0*1j],
            imageSize=(30,20),
            xlim_=(-1,1),
            ylim_=(-0.5625,0.5625),  #ratio for HP Spectre
            G=1,
            test=True):

        self.startTime = time.time()

        self.dt = dt
        self.numOfIterations = numOfIterations
        self.starLocations = np.array(starLocations, dtype=np.complex_)
        self.imageSize = imageSize
        self.xlim_ = xlim_
        self.ylim_ = ylim_
        self.G = G
        self.test = test

        self.numOfPoints = self.imageSize[0]*self.imageSize[1]
        self.results = np.zeros((self.numOfPoints))

        if self.test:
            self.posArr = np.zeros((self.numOfPoints, self.numOfIterations), dtype=np.complex_)
        else:
            self.posArr = np.zeros((self.numOfPoints))

        self.runTime = 0.0

        self.fileName = 'Total Runtime'

        print('DeltaT: {}'.format(self.dt))
        print('Number of Iterations: {}'.format(self.numOfIterations))
        print('Star Locations: {}'.format(self.starLocations))
        print('Image Size: {}'.format(self.imageSize))
        print('X limits: {}'.format(self.xlim_))
        print('Y limits: {}'.format(self.ylim_))
        print('Gravitational Constant: {}'.format(self.G))
        print('File: {}'.format(self.fileName))

        self.run()
        self.animatePos()
        self.woah()

        print('Total Time: {} seconds'.format(time.time()-self.startTime))

    def plotPoint(self):
        if not self.test:
            print('plotPoint only works in Test mode')
            return 0

        r = self.posAtItr[0,:].real
        i = self.posAtItr[0,:].imag
        plt.plot(r,i)
        plt.show()
        return 0

    def animatePos(self, interval_=20):

        if not self.test:
            print('animatePos only works in Test mode')
            return 0

        fig, ax = plt.subplots()
        ax = plt.axis([self.xlim_[0], self.xlim_[1], self.ylim_[0], self.ylim_[1]])
        x = self.posArr[:,0].real
        y = self.posArr[:,0].imag
        x_star = self.starLocations.real
        y_star = self.starLocations.imag
        plot_star = plt.plot(x_star, y_star, 'xr')
        plot, = plt.plot(x,y, 'ob')

        def animate(i):
            x = self.posArr[:,i].real
            y = self.posArr[:,i].imag
            plot.set_data(x,y)
            return plot,

        anim = animation.FuncAnimation(fig, animate, frames=self.numOfIterations, interval=interval_,
                blit=True, repeat=True)
        plt.show()
        return 0

    def woah(self):
        startTime = time.time()
        print('creating image...')

        #reshape array and convert to image
        temp = self.results/np.max(self.results)
        temp2 = np.zeros(self.imageSize)
        for i in range(self.imageSize[1]):
            temp2[:,i] = temp[i*self.imageSize[0]:(i+1)*self.imageSize[0]]
        im = Image.fromarray(np.transpose(temp2*255))
        im = im.convert('L')
        im.show()
        self.fileName = 'results/{}.png'.format(time.time()-self.startTime)
        im.save(self.fileName)
        print('woah time: {}'.format(time.time()-startTime))

    def addColor(self, colors):
        pass

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        return list(int(value[i:i+2], 16) for i in (0,2,4))

    def export(self):
        pass
