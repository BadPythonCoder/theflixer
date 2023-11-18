class Show:
    def __init__(self, obj):
        self.poster = obj[0]["img"]["@data-src"]
        self.watchlink = obj[0]["a"]["@href"]
        self.releaseyear = int(obj[1]["div"][0]["span"][0]["#text"])
        self.is_series = (False, True)[ obj[1]["div"][0]["span"][1]["strong"] == "TV" ]
        self.name = obj[1]["h2"]["a"]["#text"]

    def __repr__(self):
        return f"Name: {self.name}\nReleased in: {self.releaseyear}\nSeries?: {self.is_series}\nPoster: {self.poster}\nWatch Link: {self.watchlink}"