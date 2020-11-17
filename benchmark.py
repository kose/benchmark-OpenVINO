#!/usr/bin/env python
# coding: UTF-8

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

csvfile = "benchmark.cvs"

df = pd.read_csv(csvfile, index_col=0)

def make_chart(idx):

    title = df.index[idx]
    df2 = df.loc[title]

    cols = len(df2)
    index = [df2.index[i] for i  in range(0, cols, 2)]
    index = [re.sub(" / [0-9 a-zA-Z]*", "", str) for str in index]
    yolo = [df2[i] for i  in range(0, cols, 2)]
    hpe = [df2[i] for i  in range(1, cols, 2)]

    fig = plt.figure(figsize=(10, 2.5))
	
    bar_width = 0.45
    x = np.arange(len(index))
	
    plt.title(title)
    plt.barh(x - bar_width/2, yolo, bar_width, color="tab:blue", label="YoLo v3")
    plt.barh(x + bar_width/2, hpe, bar_width, color="tab:orange", label="Human Pose Estimation")
    plt.legend()
    plt.subplots_adjust(left=0.16, right=0.98)
    plt.gca().invert_yaxis() # 上下並びを逆順に
    plt.yticks(x, index)
    plt.grid(axis='x')

    plt.pause(5)
    fig.savefig("images/" + str(idx) + ".png")

##
##
##
make_chart(2)
make_chart(3)

# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###


