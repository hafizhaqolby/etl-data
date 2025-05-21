import pandas as pd
import numpy as np

def clean_data(raw_data):
    df = pd.DataFrame(raw_data)
    print("Awal:", df.shape)

    # Cek apakah kolom-kolom penting ada
    required_columns = ['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'Timestamp']
    for col in required_columns:
        if col not in df.columns:
            df[col] = np.nan  # Tambahkan kolom kosong jika tidak ada

    # Filter title yang valid
    df = df[df['Title'].astype(str).str.strip().str.lower() != 'unknown product']
    print("Setelah hapus unknown title:", df.shape)

    # Membersihkan kolom Price
    df['Price'] = df['Price'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce') * 16000
    print("Setelah konversi price:", df.shape)

    # Membersihkan kolom Rating
    df['Rating'] = df['Rating'].astype(str).str.extract(r'([\d.]+)')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    print("Setelah parsing rating:", df.shape)

    # Membersihkan kolom Colors
    df['Colors'] = df['Colors'].astype(str).str.extract(r'(\d+)')
    df['Colors'] = pd.to_numeric(df['Colors'], errors='coerce')
    print("Setelah parsing colors:", df.shape)

    # Membersihkan kolom Size & Gender
    df['Size'] = df['Size'].astype(str).str.replace('Size: ', '', regex=False)
    df['Gender'] = df['Gender'].astype(str).str.replace('Gender: ', '', regex=False)

    # Drop baris yang tidak punya data penting
    df = df.dropna(subset=['Price', 'Rating', 'Title'])
    print("Setelah dropna:", df.shape)

    return df