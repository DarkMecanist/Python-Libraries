import unittest
import os
from ..py_sql_lite import SQLLite


class TestCreateTable(unittest.TestCase):
    """create_table unit tests"""

    def setUp(self):
        self.database_path = "SQLLite/Data/test_create_table.db"
        self.sql = SQLLite(self.database_path)

    def test_case_1(self):
        """Testing with schema"""
        table_name = "monthly_report"
        schema = {
            "symbol": ["TEXT", "NOT NULL"],
            "avg_margin_safety": ["REAL", "NOT NULL"],
            "latest_market_price": ["REAL", "NOT NULL"],
            "avg_fair_price": ["REAL", "NOT NULL"],
            "avg_target_buy_price": ["REAL", "NOT NULL"],
            "recommendation": ["TEXT", "NOT NULL"],
        }

        self.sql.create_table(table_name=table_name, schema=schema, close_connection=True)
        self.assertTrue(os.path.isfile(self.database_path))
        os.remove(self.database_path)

    def test_case_2(self):
        """Testing with query"""
        query = "CREATE TABLE monthly_report(" \
                "symbol TEXT NOT NULL,"\
                "avg_margin_safety REAL NOT NULL,"\
                "latest_market_price REAL NOT NULL,"\
                "avg_fair_price REAL NOT NULL,"\
                "avg_target_buy_price REAL NOT NULL,"\
                "recommendation TEXT NOT NULL"\
                ")"

        self.sql.create_table(query=query, close_connection=True)
        self.assertTrue(os.path.isfile(self.database_path))
        os.remove(self.database_path)


class TestExecuteQuery(unittest.TestCase):
    """execute_query unit tests"""

    def setUp(self):
        self.database_path = "SQLLite/Data/test_execute_query.db"
        self.sql = SQLLite(self.database_path)

    def test_case_1(self):
        """Testing with INSERT, SELECT and DELETE queries"""

        # Create Database and Table
        table_name = "monthly_report"
        schema = {
            "symbol": ["TEXT", "NOT NULL"],
            "avg_margin_safety": ["REAL", "NOT NULL"],
            "latest_market_price": ["REAL", "NOT NULL"],
            "avg_fair_price": ["REAL", "NOT NULL"],
            "avg_target_buy_price": ["REAL", "NOT NULL"],
            "recommendation": ["TEXT", "NOT NULL"],
        }

        self.sql.create_table(table_name=table_name, schema=schema)

        # INSERT
        insert_query = 'INSERT INTO monthly_report ' \
                       'VALUES(:symbol, :avg_margin_safety, :latest_market_price, :avg_fair_price, :avg_target_buy_price, :recommendation)'

        parameters = {
            "symbol": "AAPL",
            "avg_margin_safety": 30.0,
            "latest_market_price": 160.0,
            "avg_fair_price": 140.0,
            "avg_target_buy_price": 140.0 * 0.3,
            "recommendation": "Don't Buy"
        }

        self.sql.execute_query(insert_query, parameters)

        # SELECT & check 1 result
        select_query = 'SELECT * FROM monthly_report'

        result = self.sql.execute_query(select_query)
        self.assertEqual(len(result), 1)

        # DELETE
        delete_query = 'DELETE FROM monthly_report WHERE symbol = :symbol'

        parameters = {
            "symbol": "AAPL"
        }

        self.sql.execute_query(delete_query, parameters)

        # SELECT & check 0 results
        result = self.sql.execute_query(select_query, close_connection=True)
        self.assertEqual(len(result), 0)
        os.remove(self.database_path)


if __name__ == "__main__":
    unittest.main()
