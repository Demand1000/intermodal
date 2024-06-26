import matplotlib.pyplot as plt

def scatter_line_plot(df,input_station):
    #preprocessing
    df = df[df["Station"] == input_station]
    df = df.sort_values(by='Arrival Planned')

    #plotting scatter points
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Arrival Planned'], df['Arrival Planned Count min'], label='Arrival Planned', alpha=0.5, marker='o')  #create dots
    plt.scatter(df['Arrival Changed'], df['Arrival Changed Count min'], label='Arrival Changed', alpha=0.5, marker='x')  # create dots

    plt.title(f'Scatter Plot of Arrival Trains in {input_station}')
    plt.xlabel('Time')
    plt.ylabel('Arrival Count min')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()