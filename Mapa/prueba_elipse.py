import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

figure(figsize=(8,8))
ax=subplot(aspect='equal')



bg = (250, 241, 220)

x = Ellipse((1, 1), 2, 2) 
y = Ellipse((1, 1), 1, 1) 

ax.add_artist(x)
ax.add_artist(y)


plt.xlim(-2, 4)
plt.ylim(-1, 3)

plt.show()