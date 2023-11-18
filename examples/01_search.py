import theflixer

shows = theflixer.search("adventure time")
show = next(shows)

print(show)