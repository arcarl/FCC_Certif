import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.where(
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
    ).dropna()


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(16, 5))
    plt.plot("date", "value", data=df, color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Using the same xticks from examples/Figure_1.png
    x_ticks = ["2016-07-01", "2017-01-01", "2017-07-01", "2018-01-01",
              "2018-07-01", "2019-01-01", "2019-07-01", "2020-01-01"]
    plt.xticks(x_ticks)

    fig = plt.gcf()
    # Save image and return fig (don't change this part)
    fig.savefig('picts/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]

    # Solving test_bar_plot_legend_labels
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']


    # Draw bar plot
    plt.figure(figsize=(15.14, 13.3))
    sns.barplot(data=df_bar, x='year', y='value', hue='month', hue_order=hue_order,  ci=None, palette='tab10')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')

    fig = plt.gcf()
    # Save image and return fig (don't change this part)
    fig.savefig('picts/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Plot Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Plot Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Set the x-axis labels for the month-wise box plot
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes[1].set_xticklabels(month_labels)

    # Adjust layout for better spacing
    plt.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('picts/box_plot.png')
    return fig
