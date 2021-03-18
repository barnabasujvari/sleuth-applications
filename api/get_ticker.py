import os
import json
from pathlib import Path

"""
Given a comment string that has been retrieved from a scraping source we
need to find the mentioned stock tickers in that comment. For this implementation
you are assuming that the comments are scraped for you and you can run
poetry run pytest to check your impementation.

You should also check if the stock ticker is a valid one. Which means that you
need to check if this is an actual ticker listed on the stock exchange.

The return is a list of string of stock tickers.

Examples (retrieved for r/wallstreetbets):
In: YOLOing my stimmy tomorrow during the short attack. Valhalla is waiting for us
Out: []

In: This is the 8th market day in a row that GME has closed above $200 GME has not closed below $100 since February 25th, 22 days in a row
Out: ["GME"]

In: PSYCH!!!!! AH is gonna be a snore fest but come PM we gonna see the rocket boosters engage and we are going straight to the fucking moon
Out: []
"""
def get(comment):
    print(comment)

    return "Not implemented", 501
