from imports import *
baseurl = "http://www.gutenberg.org/"
url = baseurl+"ebooks/search/?query="
def searchBook(query):
    searchResults = []
    try:
        text = urllib2.urlopen(url+query).read()
        page = html.fromstring(text)
        ulitems = page.xpath(".//li[@class='booklink']")
        count = 0
        for x in ulitems:
            if(count < 5):
                count += 1
                try:
                    title = x.xpath(".//span[@class='title']/text()")[0]
                    author = x.xpath(".//span[@class='subtitle']/text()")[0]
                    link = x.xpath(".//a/@href")[0]
                    newpage = html.fromstring(urllib2.urlopen(baseurl+link).read())
                    li2 = newpage.xpath("//a[@class='link' and @type='application/epub+zip']/@href")[0]
                    finalLink = li2[2:]
                    tempResult = SearchResult(title, finalLink, type=0)
                    searchResults.append(tempResult)
                except:
                    pass
    except:
        pass
    return searchResults
