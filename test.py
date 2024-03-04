import unittest
from parse_csv import read_csv, create_database, create_tables, insert_data
import os
import sqlite3

class TestParseCSV(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup that runs once before all tests
        cls.test_db = 'test_ecommerce.db'
        cls.csv_file_path = 'order_details.csv' # Ensure this CSV exists for testing

    @classmethod
    def tearDownClass(cls):
        # Cleanup that runs once after all tests
        os.remove(cls.test_db)

    def test_read_csv(self):
        # Test reading CSV files
        data = read_csv(self.csv_file_path)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)  # Assuming the CSV is not empty
        self.assertIsInstance(data[0], dict)  # Each row should be a dict

    def test_create_database(self):
        # Test database creation
        conn = create_database(self.test_db)
        self.assertIsInstance(conn, sqlite3.Connection)

    def test_create_tables_and_insert_data(self):
        # Combined test for creating tables and inserting data due to dependency
        conn = create_database(self.test_db)
        create_tables(conn)
        data = read_csv(self.csv_file_path)
        self.assertTrue(insert_data(conn, data))
        # Optionally, verify data insertion here by querying each table

if __name__ == '__main__':
    unittest.main()
