import json
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
