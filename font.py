#!/home/toby/anaconda/bin/python

import matplotlib.font_manager as mfm

y = mfm.findSystemFonts(fontpaths=None, fontext='ttf')

for i in mfm.fontManager.ttflist:
    print i


