#!/usr/bin/env python
# coding: utf-8

# In[34]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
sensor = pd.read_csv('sensor.csv')
display(sensor)
y = [0.17, 1.75,3.19,3.79,4.05,4.16,4.27,4.38,4.44,4.49,4.52,4.56,4.59,4.61]
plt.plot(sensor['Distância (cm)'], y, '-.',color='black', marker='o')
plt.xticks(sensor['Distância (cm)'])
plt.yticks([0,1,2,3,4,5])
plt.title('TCRT5000')
plt.ylabel('Tensão (Vo)')
plt.xlabel('Distância (cm)')
plt.show()


# In[ ]:




