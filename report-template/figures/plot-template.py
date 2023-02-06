# +---------------------------------------------+
# | Author: Jose Antonio Quiñonero Gris         |
# | Creation date: Saturday 15:24:39 05-11-2022 |
# +---------------------------------------------+

#
# Libreries
#
import numpy as np
import matplotlib.pyplot as plt
import os
colores=['#56B4E9', '#E69F00', '#009E73', '#0072B2', '#D55E00', '#CC79A7', '#F0E442']
#
# Style
#
style_file = 'mine.mplstyle'
style_file = os.path.dirname(__file__)+'/{}'.format(style_file)
plt.style.use(style_file)

#
# Input data
#
# fichero_datos = '<-->'
# fichero_datos = os.path.dirname(__file__)+'/{}'.format(fichero_datos)
# <--> = np.loadtxt(fichero_datos, unpack=True, skiprows=0)

#
# Plot
#
fig, ax = plt.subplots()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

ax.plot(t1, f(t1), 'ro', t2, f(t2), 'k')

# fig, axs = plt.subplots(1,2,figsize=(6*2,4.45), sharey=True)
# fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)

# fig.suptitle()

#
# First plot
#
# ax=axs[0]
#
# ax.hlines()
# ax.plot()
# ax.text(x, y, fontsize=14, horizontalalignment='center', verticalalignment='bottom')
#
# ax.ticklabel_format(axis='y', style='sci', scilimits=(2,2))
# ax.ticklabel_format(useOffset=False)
# ax.locator_params(axis='x', nbins=4)
#
# ax.set_xlim(0.5,3.5)
# ax.set_ylim(-50,40)
#
# ax.set(
#         title=r'Energy, $\Delta E$',
#        # xlabel=r'Scan coordinate ($\mathrm{\AA}$)',
#        ylabel=r'Energy, $\Delta E$ ($\mathrm{kcal/mol}$)'
#       )
#
# ax.set_xticklabels(['','Reactants','TS','Products',''], fontsize=18)
#
# ax.legend()
#
# ax.grid(False)


nombre_grafica = os.path.basename(__file__).replace(".py", ".pdf")
plt.savefig(nombre_grafica, transparent='True', bbox_inches='tight')
