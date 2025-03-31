import numpy as np
xrange = np.linspace(-1, 1, 10)
yrange = np.linspace(-1, 1, 10)
x,y = np.meshgrid(xrange, yrange)
s = [slice(0,len(x), 2),slice(0,len(x), 3)]
print(x[*s])