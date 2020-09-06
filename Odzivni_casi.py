#!/usr/bin/env python
# coding: utf-8

# In[151]:


import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
fn = './aws_test_pls.txt'


# In[152]:


df = pd.read_csv(fn, delimiter='\t')
df['seconds'] -= df['seconds'].min()
df = df.set_index(['seconds']).sort_index()
display( df.head() )


# In[153]:


R = 100
plt.plot(df['ttime'].rolling(R).mean(), linewidth=0.5)
plt.suptitle('Drseče povprečje (%d zahtev) odzivnega časa' % R)
plt.xlabel('Čas (s)')
plt.ylabel('Odzivni čas (ms)')
display( pd.DataFrame(df.describe()).T )


# In[ ]:




