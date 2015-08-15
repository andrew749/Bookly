from flask import Flask
import requests
from lxml import html
import lxml
#from urllib.parse import quote
import time
import pdb
#from urllib.request import urlopen,Request

app = Flask(__name__)

@app.route('/')
def serveMain():
    pass

@app.route('/search')
def searchBook():
    return "Hello World"

#Start the application
if __name__ == '__main__':
    app.run()
