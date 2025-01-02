from typing import Dict
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


def plot_yearly_statistics(threads_by_year: Dict[int, int], emails_by_year: Dict[int, int]):
    """
    Create and display plots for yearly thread and email counts, with values shown on the bars.
    
    Args:
        threads_by_year: Dictionary of year to thread count
        emails_by_year: Dictionary of year to email count
    """
    # Set up the plotting style
    sns.set_style("whitegrid")
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot thread counts
    thread_data = pd.DataFrame.from_dict(threads_by_year, orient='index', columns=['count'])
    thread_plot = sns.barplot(data=thread_data.reset_index(), x='index', y='count', ax=ax1, color='skyblue')
    ax1.set_title('Unique Threads by Year')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Threads')
    
    # Add values to the bars (Thread count)
    for p in thread_plot.patches:
        ax1.annotate(f'{int(p.get_height())}', 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     xytext=(0, 5),  # Offset label slightly
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10, color='black')
    
    # Plot email counts
    email_data = pd.DataFrame.from_dict(emails_by_year, orient='index', columns=['count'])  
    email_plot = sns.barplot(data=email_data.reset_index(), x='index', y='count', ax=ax2, color='lightgreen')
    ax2.set_title('Total Emails by Year')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Number of Emails')
    
    # Add values to the bars (Email count)
    for p in email_plot.patches:
        ax2.annotate(f'{int(p.get_height())}', 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     xytext=(0, 5),  # Offset label slightly
                     textcoords='offset points',
                     ha='center', va='bottom', fontsize=10, color='black')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()