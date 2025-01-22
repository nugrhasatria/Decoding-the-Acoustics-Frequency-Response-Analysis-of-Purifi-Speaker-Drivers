import matplotlib.pyplot as plt
import pandas as pd
import os

# Path ke folder data
data_folder = "../data"

# Fungsi untuk memuat dan memplot data
def plot_frequency_response(file_name):
    file_path = os.path.join(data_folder, file_name)
    
    # Membaca file
    data = pd.read_csv(file_path, sep="\t", skiprows=1, header=None, names=["Frequency (Hz)", "SPL (dB)", "Phase (deg)"])
    
    # Plot SPL vs Frequency
    plt.figure(figsize=(10, 6))
    plt.plot(data["Frequency (Hz)"], data["SPL (dB)"], label=file_name)
    plt.xscale('log')
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.title("Frequency Response")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Sound Pressure Level (dB)")
    plt.legend()
    plt.show()

# Plot masing-masing file
for file_name in ["PTT10.0X04-NAB-01 - SPL_0deg.txt",
                  "PTT10.0X04-NAB-01 - SPL_30deg.txt",
                  "PTT10.0X04-NAB-01 - SPL_60deg.txt"]:
    plot_frequency_response(file_name)
