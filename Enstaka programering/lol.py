import requests
def lamao(url):
    r = requests.get(url)
    response_dictionary = r.json()
    print(response_dictionary)