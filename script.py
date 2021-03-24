#!/usr/bin/env python3

import gravitySet

GS = gravitySet.GravitySet(
        dt=0.001,
        imageSize=(400,200),
        numOfIterations=10000,
        starLocations=[-.25-.25*1j , .25-.25*1j , .25+.25*1j  , -.25+.25*1j],
        xlim_=(0,2),
        ylim_=(0,1),
        test=False)
