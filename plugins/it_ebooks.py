from imports import *
def searchBook(query):
    baseurl = "http://it-ebooks.info/"
    url = baseurl + "search/?q=%s&type=title"
    finalurl = url % query
    req = urllib2.Request(finalurl, headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    text = urllib2.urlopen(req).read()
    page = html.fromstring(text)
    listitems = page.xpath(".//table//table//tr")
    for x in listitems:
        pdb.set_trace()
        title = x.xpath(".//a/@title")[0]
        link = x.xpath(".//a/@href")[0]
        newpage = html.fromstring(urllib2.urlopen(link).read())
        print htmlstring
searchBook("software")
