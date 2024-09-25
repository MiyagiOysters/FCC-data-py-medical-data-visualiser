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
    df_cat = df.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    

    # 6
    df_cat = df_cat.groupby(by=['cardio', 'variable', 'value']).value_counts().reset_index(name='total')

    
    # 7
    fig = sns.catplot(data=df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value').fig

    # 8


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    bp_mask = df['ap_lo'] <= df['ap_hi']
    height_mask = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    weight_mask = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[height_mask & weight_mask & bp_mask] 

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(11, 9))
    
    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f')

    # 16
    fig.savefig('heatmap.png')
    return fig
