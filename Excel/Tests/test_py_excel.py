import unittest
from ..py_excel import Excel
import os


class TestWriteExcel(unittest.TestCase):
    """write_excel unit tests"""

    def setUp(self):
        self.ex = Excel()

    def test_case_1(self):
        folder_path = "Excel/Data"
        num_initial_files = len(os.listdir(folder_path))

        file_path = "Excel/Data/test_case_1.xlsx"
        data = {
            "Employees": {"Name": ["João", "Luís"], "Age": [27, 32]},
            "Cars": {"Brand": ["Opel", "Nissan"], "Color": ["Blue", "Red"]}
        }

        self.ex.write_excel(file_path, data)

        self.assertEqual(num_initial_files, len(os.listdir(folder_path)))

        os.remove(file_path)


