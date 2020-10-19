import requests

def open_url(URL, params):
    """
    Request function to call external urls
    """
    r = requests.get(URL + "?", params=params)
    return r.text