import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from modules import get_lum_all
import FLARE.filters

###Defining input values
fac = 0.0315
h = 0.6777
z = [5, 6, 7, 8, 9, 10]
tags = ['010_z005p000', '009_z006p000', '008_z007p000', '007_z008p000', '006_z009p000', '005_z010p000']
tags_ref = ['008_z005p037', '006_z005p971', '005_z007p050', '004_z008p075', '003_z008p988', '002_z009p993']
filters = FLARE.filters.TH


df_filter_lims = pd.DataFrame({'z': z})
percentile = np.empty((len(z), len(filters)))


for ii, jj in enumerate(z):

    data = get_lum_all(fac, tags[ii], LF = False, filters = filters)

    for kk in range(38):

        if kk == 0:
            Mlum = data[kk][0]
            part = data[kk][1]
        else:
            Mlum = np.append(Mlum, data[kk][0], axis = 0)
            part = np.append(part, data[kk][1])

    ok = np.where(part == 100)

    percentile[ii] = np.percentile(Mlum[ok], 5, axis = 0)

for ii, jj in enumerate(filters):

    df_filter_lims[jj] = percentile[:, ii]

print (df_filter_lims)

df_filter_lims.to_csv('Magnitude_limits.txt')
