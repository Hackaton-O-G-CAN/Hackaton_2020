import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
from utils import downloadData
from utils import dataProc
import pickle

read = 0
if read:
    data = dataProc.dataProc()
    df = data.loadData()
    df_dict = data.cleanData(df)
    with open('df_dict.pickle', 'wb') as handle:
        pickle.dump(df_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('df_dict.pickle', 'rb') as handle:
    df_dict = pickle.load(handle)



fig = plt.figure()
ax = plt.axes()
year = '2019'
campo = "ABANICO"
date_0 = pd.to_datetime(f"01 of Jan,{year}")
print(date_0)
#x2 = date_0 + pd.to_timedelta(np.arange(12), 'M')
#print(x2)
x = pd.period_range('2019-01', periods=12, freq='M')
x2 = x.to_timestamp()
print(x2)
print(x)
x_temp = np.arange(0,12)

group = df_dict[year].groupby('contrato').sum()
data = group.loc[campo,"enero":"diciembre"].T

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