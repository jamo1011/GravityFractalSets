#!/usr/bin/env python3

import gravitySet

#GS = gravitySet.GravitySet(dt=0.005, imageSize=(1000,1000), numOfIterations=15000, starLocations=[-.25-.25*1j , .25+0*1j , 0+.25*1j ], xlim_=(-1,1), ylim_=(-1,1), test=False)

GS = gravitySet.GravitySet(
        dt=0.001,
        imageSize=(4000,2000),
        numOfIterations=10000,
        starLocations=[-.25-.25*1j , .25-.25*1j , .25+.25*1j  , -.25+.25*1j],
        xlim_=(0,2),
        ylim_=(0,1),
        test=False)
