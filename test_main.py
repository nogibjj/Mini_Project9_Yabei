import unittest
import pandas as pd
from main import main
from lib import load_data, data_summary


class TestScript(unittest.TestCase):
    def setUp(self):
        self.data_path = "https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv"
        self.df = pd.read_csv(self.data_path, sep=";")

    def test_load_data(self):
        data = load_data(self.data_path)
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

    def test_data_summary(self):
        summary = data_summary(self.df)
        self.assertIsNotNone(summary)
        self.assertTrue(len(summary) > 0)

    def test_main_function(self):
        main()


if __name__ == "__main__":
    unittest.main()
