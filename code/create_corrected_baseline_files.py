import pandas as pd
import glob
from baseline_correction import normalize_data_with_Baseline

A_csv_file = glob.glob("../data_raw/A*.csv") # Mencari semua berkas CSV yang dimulai dengan 'A' dalam direktori 'data'
B_csv_file = glob.glob("../data_raw/B*.csv") # Mencari semua berkas CSV yang dimulai dengan 'B' dalam direktori 'data'

ATTRIBUTE_NAMES = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']
def create_new_csv_files(CSV_files, label):
    """create new CSV files from corrected baseline data

    Args:
        CSV_files (list): csv files
        label (list): label
    """
    for i, csv_file in enumerate(CSV_files):
        df = pd.read_csv(csv_file)
        df = normalize_data_with_Baseline(df, ATTRIBUTE_NAMES)
        df.to_csv(f"data_baseline/_{label}_{i+1}.csv", index=False)        
        
if __name__ == "__main__":
    create_new_csv_files(A_csv_file, "A")
    create_new_csv_files(B_csv_file, "B")