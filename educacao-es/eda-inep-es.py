#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:06:04 2022

@author: lucaspb
"""

#packages

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

# Setting working directory

os.chdir(r'/Users/lucaspb/git-repositories/portifolio-projects')


# Ploting School, Type of School and City for Fundamental School


plt.figure(figsize=(15,18))
df_escolascount_fund.unstack().plot(
    kind='bar', 
    stacked=True
    )
plt.ylabel('Número de Escolas');

sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.savefig('educacao-es/output/images/type_school - city - fundamental.png', quality=95, dpi=600, bbox_inches = "tight")
plt.show()