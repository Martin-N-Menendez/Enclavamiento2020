from pylab import *
figure(figsize=(8,8))
ax=subplot(aspect='equal')

#plot one circle (the biggest one on bottom-right)
#circles(1, 0, 0.5, 'r', alpha=0.2, lw=5, edgecolor='b', transform=ax.transAxes)

#plot a set of circles (circles in diagonal)
#a=arange(11)
#out = circles(a, a,a*0.2, c=a, edgecolor='k')
#colorbar(out)

a=arange(4)

circles(5, 5,1/1, c='r', edgecolor='k')
circles(5, 5,1/2, c='g', edgecolor='k')
circles(5, 5,1/3, c='b', edgecolor='k')
xlim(0,10)
ylim(0,10)