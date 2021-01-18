'''
Program that google searches a chunk of text then scrapes results and
returns the first result with lyrics in the headline
'''

import urllib
import requests
import re
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

query = "Im not even half as pretty I gave her your sweater" + " Lyrics"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='g'):
        # anchor div
        rc = g.find('div', class_='rc')
        s = g.find('div', class_='s')
        if rc:
            divs = rc.find_all('div', recursive=False)
            if len(divs) >= 2:
                anchor = divs[0].find('a')
                title = anchor.find('h3').text
                results.append(title)

    # search through results
    lyricsites = ('Genius Lyrics', 'MetroLyrics', 'AZLyrics.com')
    reslyric = []

    for str in results:
        resdict = {}
        if str.endswith(lyricsites):
            r = str.replace(' Lyrics', '').replace(' | ', ' – ').replace(' - ', ' – ')
            text = re.split(' – ', r)
            resdict['artist'] = text[0]
            resdict['song'] = text[1]
            resdict['site'] = text[2]
            reslyric.append(resdict)
    i = 0
    guess = 'n'
    while guess == 'n':
        guess = input(f"Is the song {reslyric[i]['song']} by {reslyric[i]['artist']}? [y/n] : ")
        if guess == 'y':
            print(f"Noice! I guessed it! I love listening to the song {reslyric[i]['song']} as well!")
        elif guess == 'n' and i == len(reslyric)-1:
            print("Damn, I'm stumped! Maybe try singing some other lyrics, because I have no idea.")
            break
        else:
            print("hmm let me guess again...")
            i+=1
