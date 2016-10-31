#!/home/toby/anaconda/bin/python

import matplotlib.pyplot as plt
import numpy as np

def log_10_product(x, pos):
    if (x < 1.0):
      return '%3.1f' % (x)
    else:
      return '%i' % (x)


cc = '0.10'

font = {'family' : 'DejaVu Serif',
        'weight' : 'normal',
        'size' : 20,
}

tfont = {
    'family' : 'DejaVu Serif',
    'weight' : 'normal',
    'size' : 14}

sfont = {
        'family' : 'DejaVu Serif',
        'weight' : 'bold',
        'style': 'italic',
        'size' : 10}

plt.rc('font', **tfont)
plt.rc("axes", linewidth=2.0,edgecolor=cc)

fig, ax = plt.subplots()

ax = plt.subplot(111, axisbg='0.90', axisbelow=True)

ax.grid(b=True, which='major', color='#ffffff', linewidth=2, linestyle='-')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

ax.xaxis.set_tick_params(width=2,length=4)
ax.yaxis.set_tick_params('minor',width=2,length=0)
ax.yaxis.set_tick_params('major',width=2,length=4)

ax.yaxis.label.set_color(cc)
ax.xaxis.label.set_color(cc)
ax.tick_params(axis='x', colors=cc)
ax.tick_params(axis='y', colors=cc)

# End Defaults

c,d = np.loadtxt("marecc.dat",usecols=(0,1), unpack=True)
cH,dH = np.loadtxt("highcc.dat",usecols=(0,1), unpack=True)

ax.set_yscale('log')
ax.set_xscale('log', basex=2)
formatter = plt.FuncFormatter(log_10_product)
ax.xaxis.set_major_formatter(formatter)

plt.plot(d,c,'o',markersize=15,color='r')
plt.plot(dH,cH,'o',markersize=15,color='b')

xx = np.arange(0.01,1000,0.1)
yy = 0.0025 * xx ** -2.0
zz = 0.05 * xx ** -2.0

plt.plot(xx,yy,marker='None',color='g')
plt.plot(xx,zz,marker='None',color='g')

plt.xlim(1.0,800)
plt.ylim(5e-8,2e-3)

plt.xlabel('Crater Size (km)', fontdict=font)
plt.ylabel('Num Craters / km$^2$', fontdict=font)

plt.subplots_adjust(bottom=0.15, left=.15, right=.99, top=.99)

plt.savefig('test.png',dpi=300)
#plt.show()


