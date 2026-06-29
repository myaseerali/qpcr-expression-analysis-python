import pandas as pd

file_path= "data/raw/tb_qpcr_export.csv"

df=pd.read_csv(file_path)

print("dataset loaded successfully!")
print()
print("Shape:", df.shape)
print()
print(df.head)