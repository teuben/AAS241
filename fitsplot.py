#! /usr/bin/env python
#
#  fitsplot.py :    adapted from an LMTOY routine to plot a fits file
#                   with an optional histogram on the side
#

import os
import sys
import aplpy
import argparse
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


help_main = ["Simple color plot of a FITS image",
             "colormaps and plot file extension can also be changed",
             "plot file name is derived from input FITS file",
             ]

help_color =  ['Popular colors: viridis, gist_heat gist_ncar (default)',
               '                rainbow, jet, nipy_spectral', 
               'https://matplotlib.org/stable/tutorials/colors/colormaps.html']


parser = argparse.ArgumentParser(description="\n".join(help_main),
                                 formatter_class=argparse.RawTextHelpFormatter)
                                 # formatter_class=argparse.ArgumentDefaultsHelpFormatter)
           

parser.add_argument('fitsfile',    help="input FITS file",        default=None)
parser.add_argument('--color',     help="\n".join(help_color),    default='gist_ncar')
parser.add_argument('--ext',       help="plot type ([png],pdf)",  default='png')
parser.add_argument('--hist',      help="add histogram",          action="store_true")
parser.add_argument('--size',      help="plot size (inch)",       default=8,             type=float)

args  = parser.parse_args()

fitsfile = args.fitsfile
color    = args.color
ext      = args.ext
size     = args.size

hdu = fits.open(fitsfile)
data = hdu[0].data

#  flag out where data is NaN or 0
data = data[~np.isnan(data)]
data = data[data != 0]

#   report true data min/max/mean/std
dmin = np.min(data)
dmax = np.max(data)
dmean = np.mean(data)
dstd  = np.std(data)
print("Data min/max/mean/sig: %g %g %g %g" % (dmin,dmax,dmean,dstd))

#   use only 3*std around mean for histogram
dmin = dmean - 3*dstd;
dmax = dmean + 3*dstd;
print("Data min/max: %g %g" % (dmin,dmax))
bins = np.linspace(dmin, dmax, 32)
if args.hist:
    print("BINS: ",bins)

# define some sub-boxes
box1 = [0.1,0.1,0.8,0.8]   # full size, image
box2 = [0.1,0.1,0.5,0.5]   # left side, image
box3 = [0.7,0.15,0.2,0.4]  # right side, histo

try:
    # define a square image
    fig = plt.figure(figsize=(size, size))
    if args.hist:
        f1 = aplpy.FITSFigure(fitsfile, figure=fig, subplot=box2)
        ax_hist = fig.add_axes(box3)
        ax_hist.hist(data, bins=bins, orientation='horizontal', facecolor='blue', log=True)
    else:
        f1 = aplpy.FITSFigure(fitsfile, figure=fig, subplot=box1)
except:
    print("problem processing %s in %s" % (fitsfile,os.getcwd()))
    sys.exit(0)
    
f1.show_grayscale()
f1.show_colorscale(cmap=color)
f1.add_colorbar()

try:
    f1.add_beam()
except:
    pass

# f.show_contour(fitsfile, levels=10)
f1.add_grid()
fig.canvas.draw()

idx = fitsfile.rfind('.fits')
pfile = fitsfile[:idx] + ".%s" % ext
# fig.subplots_adjust(right=0.15)   
fig.savefig(pfile)
print("Writing ",pfile)
# plt.show()
