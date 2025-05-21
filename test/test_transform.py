import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

import unittest
import pandas as pd
from transform import clean_data

class TestTransform(unittest.TestCase):

    def test_clean_data_valid_input(self):
        raw_data = [
            {
                "Title": "Cool Jacket",
                "Price": "$10.00",
                "Rating": "4.5 / 5",
                "Colors": "3 Colors",
                "Size": "Size: L",
                "Gender": "Gender: Male",
                "Timestamp": "2024-01-01T12:00:00"
            },
            {
                "Title": "Unknown Product",
                "Price": "$5.00",
                "Rating": "3 / 5",
                "Colors": "1 Color",
                "Size": "Size: M",
                "Gender": "Gender: Female",
                "Timestamp": "2024-01-01T12:00:00"
            }
        ]

        df = clean_data(raw_data)

        # Cek hasil
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)  # Unknown Product harus dibuang
        self.assertAlmostEqual(df.iloc[0]['Price'], 160000.0)  # 10 USD * 16000
        self.assertEqual(df.iloc[0]['Size'], "L")
        self.assertEqual(df.iloc[0]['Gender'], "Male")

    def test_clean_data_empty(self):
        raw_data = []
        df = clean_data(raw_data)
        self.assertTrue(df.empty)

if __name__ == '__main__':
    unittest.main()