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



eln,ab,cc = np.loadtxt("10022_REE.dat",usecols=(1,2,3), unpack=True)
el = np.array(['x','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu'])

ratio = ab/cc

ax.set_yscale('log')

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_major_formatter(plt.FixedFormatter(el))

formatter = plt.FuncFormatter(log_10_product)
ax.yaxis.set_major_formatter(formatter)

plt.plot(eln,ratio,linewidth=2,color='b')
plt.plot(eln,ratio,'o',markersize=15,color='r')

plt.xlim(56.5,71.5)
plt.ylim(8.0,500)

plt.xlabel('\nElement', fontdict=font)
plt.ylabel('Sample / Chondrite', fontdict=font)

plt.subplots_adjust(bottom=0.15, left=.15, right=.99, top=.99)

plt.savefig('test.png',dpi=300)
#plt.show()


