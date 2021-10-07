#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:45:16 2021

@author: Jaimew
"""

# Modules
import numpy as np
import matplotlib.pyplot as plt
import decimal
from math import factorial, ceil
from matplotlib.widgets import Slider, Button

# Create matplotlib figure
fig = plt.figure()
ax = fig.add_subplot(111, title="Maclaurin series of $\sin x$")
ax.set_ylim(-4, 4)
plt.subplots_adjust(bottom=0.30)

# Initial variables
maclaurin1 = np.linspace(-4*np.pi,4*np.pi, 500)
maclaurin2 = np.linspace(-4*np.pi,4*np.pi, 500)

# Function for plotting
def maclaurin(maclaurin1, maclaurin2, monomials):
    ax.clear()
    ax.set_ylim(-4, 4)
    ax.set_title("Maclaurin series of $\sin x$")
    plt.subplots_adjust(bottom=0.30)
    for n in range(monomials):
        if n != 0:
            maclaurin2 = maclaurin2 + ((-1)**n * maclaurin1**(2*n+1) / factorial(2*n+1))
        print(maclaurin2)
        
        print()
    ax.plot(maclaurin1, np.sin(maclaurin1), "b")
    ax.plot(maclaurin1, maclaurin2, "r")


maclaurin(maclaurin1, maclaurin2, 0)

#Create sliders
ax_monomials = plt.axes([0.19, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
monomials_slider = Slider(
    ax = ax_monomials,
    label="No. of monomials",
    valmin=0,
    valmax=18,
    valinit=0,
    valfmt='%0.0f')

## Function that is called whenever sliders are changed.
def update(val):
    monomials = int(ceil(monomials_slider.val))
    
    maclaurin(maclaurin1, maclaurin2, monomials)

## Detect when sliders change 
monomials_slider.on_changed(update)
