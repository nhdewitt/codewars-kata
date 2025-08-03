"""
Get the list of integers for Codewars Leaderboard score (aka Honor) in descending order

Note:
if it was the bad timing, the data could be updated during your test cases.
Try several times if you had such experience.


https://www.codewars.com/kata/5a57d101cadebf03d40000b9/train/python
"""

from bs4 import BeautifulSoup
import requests

def get_leaderboard_honor():
    leaderboard = []
    url = "https://www.codewars.com/users/leaderboard"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    honor = soup.find_all("td", class_="honor")
    for score in honor:
        amt = score.text.strip().replace(",","")
        leaderboard.append(int(amt))
    return leaderboard