import os
import json
from pathlib import Path
import regex as re

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

def read_3_char_NASDAQ_tickers():
    '''
    for memory efficiency reasons I only include 3 char or longer names, as I only search for those anyway
    '''
    ticker_dict = {}
    # csv dowloaded from https://www.nasdaq.com/market-activity/stocks/screener without any filter
    with open("nasdaq_screener.csv") as f:
        for line in f.readlines():
            ticker = line.strip().split(',')[0]
            if len(ticker)>2:
                ticker_dict[ticker] = 1
    return ticker_dict

# reading once for efficiency
ticker_dict = read_3_char_NASDAQ_tickers()

def get(comment):
    global ticker_dict
    # argument for using only the 3 char or longer tickers, is that 1 or 2 uppercase letters would have such high rate of false positives (DD and A are valid stock tickers but are likely not mentioned as a stock in most cases) that I coinsidered them better to
    # not include
    potential_tickers = re.findall(r'[A-Z]{3,}',comment)
    tickers = []
    blacklist = ["WSB", "YOLO", "ETH", "BTC"]
    for tic in potential_tickers:
        if (tic not in blacklist) and (tic in ticker_dict) and (tic not in tickers):
            tickers.append(tic)

    return tickers, 200



