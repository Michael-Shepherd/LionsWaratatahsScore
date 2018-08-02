import requests
import time
import sys
import functions

def print_scores(soup, debug=0):
    # | Team | Score | vs | Team | Score | Date | MatchReport | Hilights |
    tables = soup.findAll("table", {"class":"fixturestable"})
    for table in tables:
        rows = table.findAll("tr");
        for row in rows:
            columns = row.findAll("td")
            for column in columns:
                if ('<div align="center">Team</div>')
                print(column)
            print("___________")
        print(table)





# Usage python3 getSeasonScores.py <year> [debug]
if __name__ == "__main__":
    argc = len(sys.argv)
    debug = 0;

    if argc < 2:
        print('Usage: python3 getSeasonScores.py <year> [debug]')
        exit()

    URL = 'http://www.superxv.com/results/{}-super-rugby-results/'.format(sys.argv[1]);

    if argc == 3:
        debug = argv[2]

    soup = functions.get_soup(URL, debug);

    print(soup.find("img", {"src":"/decor/404.jpg"}))
    if(soup.find("img", {"src":"/decor/404.jpg"}) != None):
        print("Year Not Found")
        exit()

    # TODO: Action
    print_scores(soup, debug)
