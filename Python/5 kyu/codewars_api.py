"""
Get the list of integers for 'totalAuthored' and 'totalCompleted' of the nth ranker at Codewars Leaderboard.

(1 <= n <= 500)

See Example Test Cases for the expected data format.

(Note 1 : Mind the title of this kata as well as https://dev.codewars.com/ )

(Note 2 : It is recommended to finish Codewars Leaderboard before this kata. )


https://www.codewars.com/kata/5a6b80cb880385a8f7000089/train/python
"""

from bs4 import BeautifulSoup
import requests
from functools import lru_cache

s = requests.Session()

BASE_URL = "https://www.codewars.com"
LEADERBOARD = "/users/leaderboard"
API = "/api/v1/users"

def fetch(url: str) -> requests.Response:
    resp = s.get(url)
    resp.raise_for_status()
    return resp

@lru_cache(maxsize=None)
def get_leaderboard(url: str) -> list[str]:  
    soup = BeautifulSoup(fetch(url).text, "html.parser")
    rows = soup.find_all(attrs={"data-username": True})
    return [row["data-username"] for row in rows]
    
def get_json(url: str) -> list[int]:
    data = fetch(url).json()
    return [data["codeChallenges"]["totalAuthored"], data["codeChallenges"]["totalCompleted"]]

    
def get_code_challenges(n: int) -> list[int]:
    leaderboard = get_leaderboard(BASE_URL + LEADERBOARD)
    user = leaderboard[n - 1]
    
    return get_json(BASE_URL + API + "/" + user)