import requests
import time
import sys
import functions

###############################################################################
# Prints the details of every match from the given soup within the constraints
# of the input variables. needs sport24 page soup.
#
# in:
#   soup    - soup of required webpage
#   team    - Team to view games of
#   debug   - debug value
###############################################################################
def print_scores(soup, team="none", debug=0):
    scores = soup.findAll("tr", {"class":"results-alt"})

    for score in scores:
        if team == "none":
            print(score.text)
        elif score.find("label", {"id":"lblHomeTeam"}).text.lower() == \
        team.lower() or score.find("label", {"id":"lblAwayTeam"}).text.lower()\
         ==  team.lower():
            print(score.text)
        else:
            pass


###############################################################################
# Executes when main
#
#
#
#
#
#
###############################################################################
if __name__ == "__main__":
    debug = 0
    team = "none"
    URL = 'https://www.sport24.co.za/rugby/superrugby/results'

    if len(sys.argv) > 1:
        team = sys.argv[1]
        if len(sys.argv) == 3:
            debug = int(sys.argv[2])
        elif len(sys.argv) != 2:
            print("Usage: python3 getTeamScores.py [Team Name] [debug]")
            exit()

    soup = functions.get_soup(URL, debug)
    print_scores(soup, team=team, debug=debug)
