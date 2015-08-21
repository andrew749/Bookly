from imports import *
url = "http://www.gutenberg.org/ebooks/search/?query="
def searchBook(query):
    text = urllib2.urlopen(url+query).read()
    page = html.fromstring(text)
    ulitems = page.xpath("//ul[@class = 'results']/li[@class = 'booklink']")
    for x in ulitems:
        print("\n\n\n")
        title = x.xpath("//span[@class = 'title']/text()")
        print title
    pdb.set_trace()
searchBook("sherlock")
