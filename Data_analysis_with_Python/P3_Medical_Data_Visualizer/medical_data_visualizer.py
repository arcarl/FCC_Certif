import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1. Cholesterol
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# Glucose
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Need to create an order to respect the example/pic1 representation
    order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=order)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.concat([df_cat[df_cat['cardio'] == 0].value_counts().reset_index(name='total'),
                        df_cat[df_cat['cardio'] == 1].value_counts().reset_index(name='total')])

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='total', hue='value', kind='bar', col='cardio', order=order, data=df_cat)

    # Get the figure for the output
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.where((df['ap_hi'] >= df['ap_lo']) &
                       df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975)) &
                       df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975))
                       ).dropna()

    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = pd.DataFrame(True, index=corr.index, columns=corr.columns)
    # Resolving some np.triu issues
    mask = mask.where(np.triu(np.ones(corr.shape)).astype(bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=corr.shape)

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, annot=True, cmap='magma')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
