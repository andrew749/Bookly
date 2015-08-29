import os,sys
parentdir = os.path.dirname(__file__)
sys.path.insert(0,parentdir)

import kat
from SearchResult import SearchResult
#helper method to conver the data to an object
def convertResultToDataKAT(query, results):
    resultList = []
    for x in results:
        tempResult = SearchResult(x.title, x.download, x.size, x.page, x.leechers, x.magnet, x.seeders, 1)
        resultList.append(tempResult)
    return resultList

def searchBook(query):
    results = kat.search(query, category = kat.Categories.BOOKS)
    resultList = convertResultToDataKAT(query, results)
    return resultList
