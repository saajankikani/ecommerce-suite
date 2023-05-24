import requests 
from bs4 import BeautifulSoup
import json

# Look for shreddit-comment to find comments for a page
URL = "https://www.reddit.com/comments/12jqlpw.json"

page = requests.get(URL).content
print(page)

parse = BeautifulSoup(page, "html.parser")


# shreddit_comment = parse.find(id = "-post-rtjson-content")
# print(shreddit_comment)
