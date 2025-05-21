import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

import unittest
import pandas as pd
from load import save_to_csv, save_to_google_sheets
from unittest.mock import patch, MagicMock

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "title": ["Item 1", "Item 2"],
            "price": [10000, 20000],
            "rating": [4.5, 3.8],
            "colors": [2, 3],
            "size": ["M", "L"],
            "gender": ["Male", "Female"],
            "timestamp": ["2024-01-01T12:00:00", "2024-01-01T12:05:00"]
        })
        self.test_filename = "test_output.csv"

    def test_save_to_csv(self):
        save_to_csv(self.df, self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

        df_loaded = pd.read_csv(self.test_filename)
        self.assertEqual(len(df_loaded), 2)
        self.assertIn("title", df_loaded.columns)

    @patch("load.build")
    @patch("load.Credentials")
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        mock_service = MagicMock()
        mock_spreadsheets = MagicMock()
        mock_values = MagicMock()
        mock_values.clear.return_value.execute.return_value = {}
        mock_values.update.return_value.execute.return_value = {"updatedCells": 10}

        mock_spreadsheets.values.return_value = mock_values
        mock_service.spreadsheets.return_value = mock_spreadsheets
        mock_build.return_value = mock_service

        result = save_to_google_sheets(
            self.df,
            "dummy_sheet_id",
            "Sheet1!A1",
            "dummy_creds.json"
        )

        self.assertTrue(result)
        mock_creds.from_service_account_file.assert_called_once()
        mock_build.assert_called_once()

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

if __name__ == '__main__':
    unittest.main()