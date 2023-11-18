from theflixer.Show import Show
from typing import Generator
import regex as re
import requests, xmltodict

headers = {}

def search(query: str) -> Generator[Show, None, None]:
    r = requests.get(f"https://theflixer.tv/search/{query.replace(' ', '-')}")

    html = re.search('<div class="film_list-wrap">((.|\n)*)<\!--End\: Main-->', r.text).group(0)
    html = re.sub('    ', '', html)
    html = re.sub('<div class="clearfix">\n*<\/div>', '', html)
    html = re.sub('(?<=<img .*\n.*\n.*)>', '/>', html)
    html = re.sub('rel=\&#34;nofollow\&#34;', '', html)
    html = "\n".join(html.split("\n")[:1092])

    json = xmltodict.parse(html)
    
    return (Show(o["div"]) for o in json["div"]["div"])
