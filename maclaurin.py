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

maclaurin1 = np.linspace(0,2*np.pi, 50)
maclaurin2 = maclaurin1 - (maclaurin1**3/factorial(3))
sinx = np.sin(maclaurin1)
print(maclaurin1)
print()
print(maclaurin2)
print()
print(sinx)

plt.plot(maclaurin1, maclaurin1)
plt.plot(maclaurin1, maclaurin2)
plt.plot(maclaurin1, np.sin(maclaurin1))
