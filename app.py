from flask import Flask,request,render_template, Response
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
        leachers = int(leachers)
        seeders = int(seeders)
        if not leachers == 0:
            self.quality = int(seeders)/int(leachers)
        else:
            self.quality = seeders
    def toJSON(self):
        return json.dumps({"title":self.title,'magnet':self.magnet, 'link':self.link, 'size':self.size, 'quality':self.quality})

class ResultList():
    def __init__(self, name):
        self.name = name
        self.results = []
    def appendResult(self, result):
        self.results.append(result)
    def appendResults(self,results):
        self.results += results
    def toJSON(self):
        return [x.toJSON() for x in self.results]


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
    results = kat.search(query, category = kat.Categories.BOOKS)
    resultList = convertResultToDataKAT(query, results)
    searchResults.append(resultList)
    return Response(response = resultList.toJSON(),
                    status = 200,
                    mimetype='application/json')

def convertResultToDataKAT(query, results):
    resultList = ResultList(query)
    for x in results:
        tempResult = SearchResult(x.title, x.magnet, x.download, x.size, x.seeders, x.leechers)
        resultList.appendResult(tempResult)
    return resultList

#Start the application
if __name__ == '__main__':
    app.run(debug=True)
