import requests
import time
import sys
import functions
import re

###############################################################################
# This function will print all of the scores in the given soup from
# www.superxv.com
#
# in:
#   soup - soup of required webpage
#   debug - debug value
###############################################################################
def print_scores(soup, debug=0):
    # | Team | Score | vs | Team | Score | Date | MatchReport | Hilights |
    print_list = True
    template = "{} \n {} {} - {} {}"
    tables = soup.findAll("table", {"class":"fixturestable"})
    for table in tables:
        rows = table.findAll("tr");
        for row in rows:
            row_list = []
            columns = row.findAll("td")
            for column in columns:
                # Do not store header rows or bye rows
                if "Team" in column.text or "Bye" in column.text:
                    print_list = False
                    break
                row_list.append(re.sub('\s+', '', column.text))
            if not print_list:
                print_list = True
            else:
                print(template.format(row_list[5], row_list[0], row_list[1],\
                row_list[3], row_list[4]))
                print("__________________________________")

###############################################################################
# Usage python3 getSeasonScores.py <year> [debug]
#
# This function will return all of the Super rugby scores from a specified
# season, as long as that season is in the www.superxv.com archives
###############################################################################
if __name__ == "__main__":
    argc = len(sys.argv)
    debug = 0

    if argc < 2:
        print('Usage: python3 getSeasonScores.py <year> [debug]')
        exit()

    URL = 'http://www.superxv.com/results/{}-super-rugby-results/'.\
    format(sys.argv[1])

    if argc == 3:
        debug = sys.argv[2]

    soup = functions.get_soup(URL, debug)

    if(soup.find("img", {"src":"/decor/404.jpg"}) != None):
        print("Year Not Found")
        exit()

    # TODO: Action
    print_scores(soup, debug)
