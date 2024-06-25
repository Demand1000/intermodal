import matplotlib.pyplot as plt

def scatter_line_plot(df):
    df = df.sort_values(by='Arrival Planned')
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Arrival Planned'], df['Arrival Planned Count min'], label='Arrival Planned')  #create dots
    plt.plot(df['Arrival Planned'], df['Arrival Planned Count min'], linestyle='-', color='orange', label='Arrival Planned') ##create line
    plt.title('Line Plot of Arrival Planned Count min')
    plt.xlabel('Time')
    plt.ylabel('Arrival Planned Count min')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()