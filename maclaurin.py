#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:45:16 2021

@author: Jaimew
"""

import numpy as np
import matplotlib.pyplot as plt
import decimal
from math import factorial

maclaurin1 = np.linspace(-4*np.pi,4*np.pi, 500)
maclaurin2 = np.linspace(-4*np.pi,4*np.pi, 500)
    
for n in range(50):
    if n != 0:
        maclaurin2 = maclaurin2 + ((-1)**n * maclaurin1**(2*n+1) / factorial(2*n+1))
    print(maclaurin2)
    
    print()
    plt.plot(maclaurin1, maclaurin2)
plt.plot(maclaurin1, np.sin(maclaurin1))

plt.gca().set_ylim(-4, 4)

