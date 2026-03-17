from wsgiref import headers

import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"
    headers = {
        "x-api-key": "live_FwEelqgH1QuGNhai6Cy2PC6K6yPF63Ado5cH92iU3SECrVeaHvBBgdtSu2DninUc",
    }
    resposta = requests.get(url, headers=headers)
    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"
    resposta = requests.get(url)
    return resposta.json()[0]