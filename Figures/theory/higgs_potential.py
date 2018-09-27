import numpy as np
import matplotlib.pyplot as plt
font = "sans-serif"


def arrowed_spines(ax=None, arrow_length=20, labels=('', ''), arrowprops=None):
    xlabel, ylabel = labels
    if ax is None:
        ax = plt.gca()
    if arrowprops is None:
        arrowprops = dict(arrowstyle='-|>', facecolor='black')

    for i, spine in enumerate(['left', 'bottom']):
        # Set up the annotation parameters
        t = ax.spines[spine].get_transform()
        xy, xycoords = [1, 0], ('axes fraction', t)
        xytext, textcoords = [arrow_length, 0], ('offset points', t)
        ha, va = 'left', 'bottom'

        # If axis is reversed, draw the arrow the other way
        top, bottom = ax.spines[spine].axis.get_view_interval()
        if top < bottom:
            xy[0] = 0
            xytext[0] *= -1
            ha, va = 'right', 'top'

        if spine is 'bottom':
            xarrow = ax.annotate(xlabel, xy, xycoords=xycoords, xytext=xytext, 
                        textcoords=textcoords, ha=ha, va='center',
                        arrowprops=arrowprops)
        else:
            yarrow = ax.annotate(ylabel, xy[::-1], xycoords=xycoords[::-1], 
                        xytext=xytext[::-1], textcoords=textcoords[::-1], 
                        ha='center', va=va, arrowprops=arrowprops)
    return xarrow, yarrow


mu2 = -2
lam = 6
r = np.arange(-1,1,.02)

mu_pos = np.add(0.5*mu2*np.power(r,2), 0.25*lam*np.power(r,4))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(r,mu_pos,'k',color='#2196F3',linewidth=4)
ax.set_ylim([-0.2,1])
ax.grid(False)
ax.set_title('')

# using 'spines', new in Matplotlib 1.0
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

#ax.spines['left'].set_smart_bounds(True)
#ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axhline(linewidth=2,color="black")
ax.axvline(linewidth=2,color="black")
plt.text(0.05, 0.8, "$V(\phi)$", ha="left", family=font, size=25)
plt.text(0.9, -0.1, r"$\Re{\left( \phi\right)}$", ha="left", family=font, size=25)
plt.text(0.6, -0.3, r"$\nu$", ha="center", family=font, size=25)
plt.text(-0.6, -0.3, r"$-\nu$", ha="center", family=font, size=25)

ax.set_yticklabels([])
ax.set_xticklabels([])
plt.savefig("Higgs_potential.png")
plt.show()
