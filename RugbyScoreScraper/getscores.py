import requests
import time
import sys
import functions



###############################################################################
# Prints the score and other details initially and then whenever the score
# changes until full time.
#
# in:
#   url - url of required webpage
#   debug - debug value
###############################################################################
def print_score(url, debug=0):
    old_score = "0 - 0"
    fulltime = "not"
    soup = functions.get_soup(url, debug)

    while True and soup != False and "Full Time" not in fulltime:
        score    = soup.find("div", {"class" : "score"}).text
        lions    = soup.find("div", {"class" : "hometeam"}).text
        tahs     = soup.find("div", {"class" : "awayteam"}).text
        fulltime = soup.find("div", {"class" : "infocopy"}).text
        new_score = "%s %s %s"%(lions, score, tahs)

        if (new_score != old_score):
            old_score = new_score
            print("\n\t\t\t"+new_score)
            print(fulltime)

        soup = functions.get_soup(url)

###############################################################################
# Todo: Modify to search for a match thread using the arguments
###############################################################################
if __name__ == "__main__":
    debug = 0
    URL = 'https://www.sport24.co.za/rugby/livescoring?mid=75250235&st=rugby'
    if len(sys.argv) > 1:
        debug = int(sys.argv[1])

    print_score(URL, debug)
