import os
import requests
import json


class YahooFinance:
    """
    Yahoo Finance

    Documentation: https://www.yahoofinanceapi.com/
    Examples: https://www.yahoofinanceapi.com/tutorial
    """

    def __init__(self, version):
        try:
            self.API_KEY = os.environ["YAHOO_FINANCE_API_KEY"]
        except KeyError:
            raise Exception("API_KEY is empty check env. variable YAHOO_FINANCE_API_KEY was set.")
        self.SERVER = "https://yfapi.net"
        self.VERSION = version
        self.headers = {'x-api-key': self.API_KEY}

    def get_competitors(self, symbol, limit=5):
        """
        :param symbol: [String]
        :param limit: [Integer]
        :return: [List of String]
        """

        # Check symbol not empty
        if symbol == "":
            raise Exception("No symbol provided.")

        url = f"{self.SERVER}/{self.VERSION}/finance/recommendationsbysymbol/{symbol}"
        response = requests.request("GET", url, headers=self.headers)
        json_response = json.loads(response.text)

        print(f"Found {len(json_response['finance']['result'][0]['recommendedSymbols'])} competitors.")

        # Sort competitors by score
        sorted_response = sorted(json_response["finance"]["result"][0]["recommendedSymbols"], key=lambda x: x["score"], reverse=True)
        competitors = []

        for competitor in sorted_response:
            if len(competitors) == limit:
                break
            else:
                competitors.append(competitor["symbol"])

        print(f"Returning {len(competitors)} competitors: {', '.join(competitors)}")

        return competitors

    def get_data(self, symbols):
        """
        :param symbols: [List]
        :return: [Dictionary]
        """

        # Check symbol not empty
        if len(symbols) == 0:
            raise Exception("No symbols provided.")

        url = f"{self.SERVER}/{self.VERSION}/finance/quote"
        querystring = {"symbols": ",".join(symbols)}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        data = json.loads(response.text)

        print("get_data returned following response: " + str(data["quoteResponse"]["result"]))

        return data["quoteResponse"]["result"]

    def get_research_data(self, symbol):
        """
        :param symbol: [String]
        :return: [List of Dictionaries]
        """

        # Check symbol not empty
        if symbol == "":
            raise Exception("No symbol provided.")

        url = f"{self.SERVER}/ws/insights/{self.VERSION}/finance/insights"
        querystring = {"symbol": symbol}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        research_data = json.loads(response.text)

        print("get_data returned following response: " + str(research_data["finance"]["result"]))

        return research_data["finance"]["result"]




