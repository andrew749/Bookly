from imports import *
baseurl = "https://www.ebooks-it.net/"
url = baseurl + "search/?q=%s&type=title"
def searchBook(query):
    text = urllib2.urlopen(url%query).read()
    page = html.fromstring(text)
    listitems = page.xpath(".//h3/a")
    for x in listitems:
        title = x.xpath("./text()")
        link = x.xpath("./@href")

        newpage = html.fromstring(urllib2.urlopen(link).read())

    print htmlstring
