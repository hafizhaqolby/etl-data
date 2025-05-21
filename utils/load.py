import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename} dengan {df.shape[0]} baris.")

def save_to_google_sheets(df, spreadsheet_id, range_name, credentials_file):
    credentials = Credentials.from_service_account_file(
        credentials_file,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    # Kosongkan range dulu
    sheet.values().clear(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()

    # Siapkan dan kirim data
    values = [df.columns.tolist()] + df.values.tolist()
    body = {'values': values}

    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"Data berhasil dikirim ke Google Sheets pada {spreadsheet_id} di range {range_name}")
    return True  # penting untuk unit test
