import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_analysis(df):

    print("\n--- Basic Info ---")
    print(df.info())

    print("\n--- Cancellation Rate ---")
    cancellation_rate = df['cancelled'].mean() * 100
    print(f"Cancellation Rate: {cancellation_rate:.2f}%")

    print("\n--- Average Delivery Time by Region ---")
    region_perf = df.groupby('region')['delivery_time_min'].mean()
    print(region_perf)

    print("\n--- Delay Percentage ---")
    delay_rate = df['is_delayed'].mean() * 100
    print(f"Delay Rate: {delay_rate:.2f}%")

    # Plot regional performance
    sns.barplot(x=region_perf.index, y=region_perf.values)
    plt.title("Average Delivery Time by Region")
    plt.ylabel("Minutes")
    plt.show()

    return cancellation_rate, delay_rate, region_perf
