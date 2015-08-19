import json
class SearchResult():
    def __init__(self, name, magnet, link, size, seeders, leachers, page,type=1):
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


