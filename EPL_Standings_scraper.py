from bs4 import BeautifulSoup as bs
import requests
import csv 

sauce = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats')
soup = bs(sauce.text, 'lxml')

table = soup.find('table', id='stats_squads_standard_for')
if not table:
    print("Data not found!")
    exit()

filename = "d:\Python files\premier_league_stats.csv"
f = open(filename, "w", newline='', encoding='utf-8')
headers = ["Team", "Matches Played", "Wins", "Draws", "Losses", "Goals For", "Goals Against", "Goal Difference", "Points"]
outputWriter = csv.writer(f)
outputWriter.writerow(headers)

rows = table.find_all('tr')[1:] 
for row in rows:
    team = row.find('th').text.strip()
    cols = row.find_all('td')
    data = [col.text.strip() for col in cols[:8]]  
    full_row = [team] + data
    outputWriter.writerow(full_row)

f.close()