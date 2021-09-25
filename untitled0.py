#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:52:59 2019

@author: Saad
"""

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

income = np.random.normal(0, 0.5, 10000)

plt.hist(income, 50)
plt.show()

np.mean(income)
np.var(income)
sp.skew(income)
sp.kurtosis(income)


