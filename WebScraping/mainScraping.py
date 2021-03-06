import pandas as pd
import os


import ZacksWebScraping

if __name__ == "__main__":
    wd = os.getcwd()
    tickersData = pd.read_csv(wd+'/docs/Symbols.csv')
    tickers = list(tickersData['Symbol'])
    sector = list(tickersData['GICS Sector'])

    zScraping = ZacksWebScraping.tabScrap()

    performEpsScraping = False
    performFundamentalsScraping = True

    errorFix = False

    if performEpsScraping:
        zScraping.epsScraping(tickers,wd)
    
    if performFundamentalsScraping and not errorFix:
        fundamentalsData = pd.read_csv(wd+'/docs/FundamentalsList.csv')
        fundamentalsListMark,fundamentalsListUnit = list(fundamentalsData['Mark']),list(fundamentalsData['Unit'])

        fundamentalsList = [(x,y) for x,y in zip(fundamentalsListMark,fundamentalsListUnit)]

        zScraping.fundamentalsScraping(tickers,fundamentalsList,wd,errorFix)

    if errorFix:
        fundamentalsData = pd.read_csv(wd+'/docs/FundamentalsList.csv')
        f = wd+'/docs/failed_queries_Fundamentals.txt'
        zScraping.fixErrorTickers(f,fundamentalsData,wd)


