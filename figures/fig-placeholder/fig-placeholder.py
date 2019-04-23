#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import os

basename = os.path.splitext(__file__)[0]


# --- Import data here ---

# (Junk data for plot)
x = np.linspace(0, 10, 201)
y = (x-5)*np.sin((x-5)**2)

# --- Make the plot ---

plt.figure(figsize=(3.25, 2.44)) # inches, 4x3 aspect ratio
ax=plt.gca() # axis handle

plt.plot(x, y, 'k-', label='example data')

plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.xlim([0, 10])
plt.ylim([-5,5])
plt.legend(fontsize=8, loc='upper right')

# setup text box in the middle
tbox = plt.text(0.5, 0.5, 'Placeholder', horizontalalignment='center', 
  verticalalignment='center', fontsize=16, transform=ax.transAxes)
tbox.set_bbox(dict(facecolor='white', alpha=0.85, edgecolor='gray', 
  boxstyle='round'))

plt.tight_layout(pad=0.15);
plt.savefig(basename+'.pdf', transparent=True)
plt.savefig(basename+'.eps', transparent=True) # many journals want eps figures

