import requests
import time
import lxml.html
from bs4 import BeautifulSoup

URL = 'https://www.sport24.co.za/rugby/livescoring?mid=75250235&st=rugby'

def get_soup(url):
    for i in range (3):
        with requests.session() as session:
            try:
                time.sleep(0.01)
                request = session.get(url)
                return BeautifulSoup(request.content, "lxml")

            except:
                print("\nAttempt: %d\n"%i)
    return(False)

old_score = "0 - 0"
soup = get_soup(URL)
while True and soup != False:


    score = soup.find("div", {"class" : "score"}).text
    lions = soup.find("div", {"class" : "hometeam"}).text
    tahs  = soup.find("div", {"class" : "awayteam"}).text

    new_score = "%s %s %s"%(lions, score, tahs)

    if (new_score != old_score):
        old_score = new_score
        print(new_score)

    soup = get_soup(URL)
