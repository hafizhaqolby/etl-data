import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

import unittest
from extract import scrape_main, scrape_all_pages, fetch_page_content

class TestExtract(unittest.TestCase):
    def test_fetch_page_content(self):
        url = "https://fashion-studio.dicoding.dev/"
        content = fetch_page_content(url)
        self.assertIsNotNone(content)
        self.assertIsInstance(content, bytes)  # HTML content dalam bentuk byte

    def test_scrape_main_valid_page(self):
        url = "https://fashion-studio.dicoding.dev/"
        result = scrape_main(url)
        self.assertIsInstance(result, list)
        if result:  # Jika ada data
            self.assertIn("Title", result[0])
            self.assertIn("Price", result[0])

    def test_scrape_all_pages_limit(self):
        result = scrape_all_pages(total_pages=2)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()