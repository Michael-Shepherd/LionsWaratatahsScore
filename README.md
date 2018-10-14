# Super Rugby Scraper

Written in python3

## Overview

This repository contains the means to settle any argument or satisfy any itch for knowledge (As long as it is regarding uper rugby scores)

## Usage
### Get Scores for the Lions vs Waratahs 2018 Semi-final
```
python3 getscores.py [debug] [refreshtime]
```
This will only be useful for about half an hour...I was bored. I will try to make it actually useful at some point.

### Fetch the season scores for the 2018 Super rugby season for either all teams or a specified team.
```
python3 getTeamScores.py [Team Name] [debug]
```

### Return all of the Super rugby scores from a specified season, as long as that season is in the www.superxv.com archives 
```
Usage python3 getSeasonScores.py <year> [debug]
```
## TODO
* Find issue with getTeamScores for older seasons
* change getscores to fetch live scores if any are currently happening
* Integrate all functions into one smooth flowing program
* Implement a gui for usability
* New use cases

