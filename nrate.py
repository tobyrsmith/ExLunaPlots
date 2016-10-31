#!/home/toby/anaconda/bin/python

import matplotlib.pyplot as plt
import numpy as np


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

ax.set_yscale('log')

plt.xlim(4.60,-0.250)
plt.ylim(5e-6,9e-1)

plt.xlabel('Age (billion years)', fontdict=font)
plt.ylabel('N(1)', fontdict=font)

n1 = np.array([64, 6.68, 370, 0.21, 3600, 340, 100, 0.6, 0.39])
age = np.array([3.59, 0.80, 3.87, 0.025, 4.15, 3.92, 3.89, 0.096, 0.047])

N1 = n1 * 1e-4

t = np.arange(0,5,0.01)

A = 5.44e-14
B = 6.93
C = 8.38e-4

NFit = A * (np.exp(B*t) - 1.0) + (C * t)
CFit = C * t

plt.plot(t, NFit, color='r', marker='None', linestyle='-',linewidth=4)
plt.plot(t, CFit, color='g', marker='None', linestyle='--',linewidth=2)
plt.plot(age,N1,'o',markersize=16,color='b')

plt.text(3.48,58e-4, '10022', fontdict=sfont)
plt.text(0.74,8.5e-4, '12033', fontdict=sfont)
plt.text(3.75,325e-4, '14321', fontdict=sfont)
plt.text(0.47,0.18e-4, '14321', fontdict=sfont)
plt.text(4.03,3200e-4, '15415', fontdict=sfont)
plt.text(4.38,300e-4, '67015', fontdict=sfont)
plt.text(4.35,86e-4, '72535', fontdict=sfont)
plt.text(0.50,0.33e-4, '67015', fontdict=sfont)
plt.text(0.54,0.54e-4, '72535', fontdict=sfont)

plt.subplots_adjust(bottom=0.15, left=.15, right=.99, top=.99)
plt.savefig('test.png',dpi=300)


#plt.show()


