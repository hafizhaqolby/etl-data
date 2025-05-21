from utils.extract import scrape_all_pages
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_google_sheets

def main():
    print("Mulai scraping data...")
    raw_data = scrape_all_pages()

    import pandas as pd
    df = pd.DataFrame(raw_data)
    print(f"Data berhasil diambil: {len(raw_data)} baris")
    print(df.head())

    print("Membersihkan dan mentransformasi data...")
    transformed_data = clean_data(raw_data)

    print("Menyimpan ke CSV...")
    save_to_csv(transformed_data, 'products.csv')

    print("Mengirim ke Google Sheets...")
    save_to_google_sheets(transformed_data, '1xH2zoMKZJ5fWlS-IU4sYTrTk2pVlURQW6cUURL9SMgA', 'Sheet1!A1', 'etl-data-fashion-ededbc565ed6.json')

    print("ETL pipeline selesai.")

if __name__ == "__main__":
    main()