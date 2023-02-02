import numpy as np

x = np.arange(1,151,1)
y = np.arange(1,151,1)
z = np.arange(1,151,1)

for a in range(150):
    for b in range(150):
        for c in range(150):
            if(x[a]**3 + y[b]**3 == z[c]**3):
                print(x[a], y[b], z[c])
