import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys

f = np.loadtxt(
    './outfarg_new.txt', 
    unpack='False',
    delimiter = '\t',
    skiprows=1,
    usecols=4
)

print(np.max(f))
print(np.mean(f))



plt.hist(f, bins=int(np.max(f)/10))
plt.xlabel('Odzivni cas(ms)')
plt.ylabel('Stevilo zahtev')
plt.show()