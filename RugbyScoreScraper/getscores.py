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
while True:
    soup = get_soup(URL)

    score = soup.find("div", {"class" : "score"}).text
    lions = soup.find("div", {"class" : "hometeam"}).text
    tahs  = soup.find("div", {"class" : "awayteam"}).text

    print("%s %s %s"%(lions, score, tahs))
