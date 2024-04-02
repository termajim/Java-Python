# Chuck Norris vitsi ohjelma

import requests
import json


def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['value']


if __name__ == "__main__":
    # Hae satunnainen Chuck Norris -vitsi
    vitsi = hae_chuck_norris_vitsi()

    if vitsi:
        print(vitsi)
