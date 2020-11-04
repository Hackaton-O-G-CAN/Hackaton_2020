import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
from utils import cleanData

b = cleanData.cleanData()
df_dict = b.cleanData()

fig = plt.figure()
ax = plt.axes()

group = df_dict['2019'].groupby('contrato').sum()
campo = "ABANICO"
data = group.loc[campo,"enero":"diciembre"].T
x = pd.period_range('2019-01', periods=12, freq='M')
x_temp = np.arange(0,12)
ax.plot(x, data.loc[:],'o', color = 'black')
    
arps_start = "enero"
arps_b = 0.5
arps_Di = 0.04
arps_prediction = np.zeros(12);
arps_prediction = data[arps_start] / pow( 1 + arps_b * arps_Di * x_temp, 1/arps_b)

ax.plot(x-x[0], arps_prediction,'--', color = 'blue');
print(x)
print(x-x[0])

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html