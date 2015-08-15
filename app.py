from flask import Flask,request,render_template
import requests
from lxml import html
import lxml
import time
import pdb
import kat
app = Flask(__name__)
import json

class SearchResult():
    def __init__(self, name, magnet, link, size, seeders, leachers):
        self.title = name
        self.magnet = magnet
        self.link = link
        self.size = size
        self.quality = seeders/leachers

class ResultList():
    def __init__(self, name):
        self.name = name
        self.results = []
    def appendResult(self, result):
        self.results.append(result)
    def appendResults(self,results):
        self.results += results


searchResults = []
@app.route('/')
def serveMain():
    pass

@app.route('/popular')
def returnTop():
    return kat.popular(category=kat.Categories.BOOKS)

@app.route('/search')
def searchBook():
    query = request.args.get('q')

    resultList = ResultList(query)

    results = kat.search(query)

    for x in results:
        tempResult = SearchResult(x.title, x.magnet, x.download, x.size, x.seeders, x.leechers)
        resultList.appendResult(tempResult)

    searchResults.append(resultList)
    return "Success"

#Start the application
if __name__ == '__main__':
    app.run(debug=True)
