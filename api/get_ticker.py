import os
import json
from pathlib import Path

"""
Given a comment string that has been retrieved from a scraping source we
need to find the mentioned stock tickers in that comment. For this implementation
you are assuming that the comments are scraped for you and you can run
poetry run pytest to check your impementation. This only has a few examples
so if you wish to write more tests you can have a look in the tests/comments.txt file.

You should also check if the stock ticker is a valid one. Which means that you
need to check if this is an actual ticker listed on the stock exchange.

The return is a list of strings of stock tickers.
"""
def get(comment):
    print(comment)

    return "Not implemented", 501
