import requests


URL = "https://ntfy.artic42.com/LiveRPG"


def sendExplosionNtfy():
    requests.post(URL,
                  data="Bomb has exploded in the game",
                  headers={
                       "Title": "Bomb has exploded in the game",
                       "Priority": "urgent",
                       "Tags": "warning,skull"
                  })
