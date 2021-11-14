import unittest
from ..py_yahoo_finance import YahooFinance


class TestGetCompetitors(unittest.TestCase):
    """get_competitors unit tests"""

    def setUp(self):
        self.yfinance = YahooFinance(version="v6")

    def test_case_1(self):
        """Testing with GOOG and limit=2"""

        symbol = "GOOG"
        limit = 2
        competitors = self.yfinance.get_competitors(symbol, limit)

        self.assertEqual(len(competitors), 2)


class TestGetData(unittest.TestCase):
    """get_data unit tests"""

    def setUp(self):
        self.yfinance = YahooFinance(version="v6")

    def test_case_1(self):
        """Testing with GOOG, NVDA and MSFT"""

        symbols = ["GOOG", "NVDA", "MSFT"]
        data = self.yfinance.get_data(symbols)

        self.assertEqual(len(data), len(symbols))


class TestResearchGetData(unittest.TestCase):
    """get_research_data unit tests"""

    def setUp(self):
        self.yfinance = YahooFinance(version="v1")

    def test_case_1(self):
        """Testing with GOOG"""

        symbol = "GOOG"
        research_data = self.yfinance.get_research_data(symbol)

        self.assertIsNotNone(research_data)


if __name__ == "__main__":
    unittest.main()
