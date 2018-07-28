import requests
import time
import sys
import lxml.html
from bs4 import BeautifulSoup

URL = 'https://www.sport24.co.za/rugby/livescoring?mid=75250235&st=rugby'

def get_soup(url, debug=0):
    for i in range (3):
        with requests.session() as session:
            try:
                time.sleep(0.01)
                request = session.get(url)
                return BeautifulSoup(request.content, "lxml")

            except:
                if debug != 0:
                    print("\nAttempt: %d\n"%i)
                else:
                    pass
    return(False)

if __name__ == "__main__":
    debug = 0

    if len(sys.argv) > 1:
        debug = sys.argv[1]

    old_score = "0 - 0"
    soup = get_soup(URL, debug)
    while True and soup != False:


        score = soup.find("div", {"class" : "score"}).text
        lions = soup.find("div", {"class" : "hometeam"}).text
        tahs  = soup.find("div", {"class" : "awayteam"}).text

        new_score = "%s %s %s"%(lions, score, tahs)

        if (new_score != old_score):
            old_score = new_score
            print(new_score)

        soup = get_soup(URL)
