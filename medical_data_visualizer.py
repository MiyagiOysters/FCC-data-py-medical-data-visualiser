import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')


# 2
height_meters = df['height'] / 100
df['overweight'] = df['weight'] / (height_meters) ** 2
overweight_mask = df['overweight'] > 25
df['overweight'] = np.where(overweight_mask, 1, 0)


# 3
cholesterol_mask = df['cholesterol'] == 1
glucose_mask = df['gluc'] == 1
df['cholesterol'] = np.where(cholesterol_mask, 0, 1)
df['gluc'] = np.where(glucose_mask, 0, 1)


# 4
def draw_cat_plot():
    # 5
    

    # 6
    

    # 7


    # 8


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
