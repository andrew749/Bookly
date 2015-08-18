from flask import Flask,request,render_template, Response
import requests
from lxml import html
import lxml
import time
import pdb
import kat
app = Flask(__name__)
import json
"""
An object to represent a Search result
:param name: The title of the result
:param magnet: The magnet link(if the result is a torrent)
:param link: A download link
:param size: The size of the file.
:param quality: A general measurement used traditionally for torrents
:param type: The type of result (0 for torrent, 1 for direct download)
"""
class SearchResult():
    def __init__(self, name, magnet, link, size, seeders, leachers,type=1, page):
        self.title = name
        self.magnet = magnet
        self.link = link
        self.size = size
        self.type = type
        self.page = page
        leachers = int(leachers)
        seeders = int(seeders)
        if not leachers == 0:
            self.quality = int(seeders)/int(leachers)
        else:
            self.quality = seeders
    def toJSON(self):
        return json.dumps({"title":self.title,'magnet':self.magnet, 'link':self.link, 'size':self.size, 'quality':self.quality, 'type':self.type, 'page':self.page},indent = 4)

class ResultList():
    def __init__(self, name):
        self.name = name
        self.results = []
    def appendResult(self, result):
        self.results.append(result)
    def appendResults(self,results):
        self.results += results
    def toJSON(self):
        return json.dumps([x.toJSON() for x in self.results], indent = 4)


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
        tempResult = SearchResult(x.title, x.magnet, x.download, x.size, x.seeders, x.leechers, x.page, 0)
        resultList.appendResult(tempResult)
    return resultList

#Start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
