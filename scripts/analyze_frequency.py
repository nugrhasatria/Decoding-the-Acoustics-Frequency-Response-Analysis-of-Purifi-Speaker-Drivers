import pandas as pd
import os

# Path ke folder data
data_folder = "../data"

# Fungsi untuk analisis data
def analyze_frequency_response(file_name):
    file_path = os.path.join(data_folder, file_name)
    
    # Membaca file
    data = pd.read_csv(file_path, sep="\t", skiprows=1, header=None, names=["Frequency (Hz)", "SPL (dB)", "Phase (deg)"])
    
    # Analisis dasar
    max_spl = data["SPL (dB)"].max()
    min_spl = data["SPL (dB)"].min()
    peak_frequency = data.loc[data["SPL (dB)"].idxmax(), "Frequency (Hz)"]

    print(f"File: {file_name}")
    print(f"  Max SPL: {max_spl:.2f} dB at {peak_frequency:.2f} Hz")
    print(f"  Min SPL: {min_spl:.2f} dB")
    print("-" * 40)

# Analisis masing-masing file
for file_name in ["PTT10.0X04-NAB-01 - SPL_0deg.txt",
                  "PTT10.0X04-NAB-01 - SPL_30deg.txt",
                  "PTT10.0X04-NAB-01 - SPL_60deg.txt"]:
    analyze_frequency_response(file_name)
