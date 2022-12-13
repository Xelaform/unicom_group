import pandas as pd
import numpy as np
import matplotlib


n = 10000  # количество данных 

########### генерация данных # начата ###########
array, noise = np.random.rand(n), np.random.rand(n)-0.5*np.ones(n)
for i in range(n):
    array[i] = array[i]**2 + (noise[i] if noise[i]>0.4 else 0.05*noise[i]) 
df = pd.DataFrame(array, columns=['value'])
########### генерация данных # окончена ########### df

df['value'].hist(bins=20)