from flask import Flask,request,render_template, Response
import requests
from lxml import html
import lxml
import time
import pdb
app = Flask(__name__)
import json
import ResultList, SearchResult
from plugins import katmod
#from plugins import *
"""
An object to represent a Search result
:param name: The title of the result
:param magnet: The magnet link(if the result is a torrent)
:param link: A download link
:param size: The size of the file.
:param quality: A general measurement used traditionally for torrents
:param type: The type of result (0 for torrent, 1 for direct download)
"""
searchResults = []

@app.route('/')
def serveMain():
    return "Success"

@app.route('/popular')
def returnTop():
    return kat.popular(category=kat.Categories.BOOKS)

@app.route('/search')
def searchBook():
    query = request.args.get('q')
    songResultList = ResultList(query)
    kat_results = katmod.searchBook(query)

    songResultList.appendResults(results)
    searchResults.append(songResultList)

    return Response(response = songResultList.toJSON(),
                    status = 200,
                    mimetype='application/json')

#Start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
