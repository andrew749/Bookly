import os,sys
parentdir = os.path.dirname(__file__)
sys.path.insert(0,parentdir)

import kat
from ResultList import ResultList
from SearchResult import SearchResult
#helper method to conver the data to an object
def convertResultToDataKAT(query, results):
    resultList = ResultList(query)
    for x in results:
        tempResult = SearchResult(x.title, x.magnet, x.download, x.size, x.seeders, x.leechers, x.page, 0)
        resultList.appendResult(tempResult)
    return resultList

def searchBook(query):
    results = kat.search(query, category = kat.Categories.BOOKS)
    resultList = convertResultToDataKAT(query, results)
    return resultList
