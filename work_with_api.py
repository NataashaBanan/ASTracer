import requests


def ipinfo_request(address: str) -> dict:
    url = 'https://ipinfo.io/{}/json'.format(address)
    data = requests.get(url)
    data = data.json()
    keys = ("org", "city", "country")
    return {key: data[key] if key in data.keys() else '?' for key in keys}


def ip_api_request(address: str) -> dict:
    url = 'http://ip-api.com/json/{}'.format(address)
    data = requests.get(url)
    data = data.json()
    keys = ("org", "city", "country")
    return {key: data[key] if (key in data.keys() and data[key]) else '?' for key in keys}


def request_ip_data(address: str) -> dict:
    ip_apis = (ip_api_request,
               ipinfo_request)
    for api in ip_apis:
        try:
            data = api(address)
        except requests.RequestException:
            continue
        else:
            break
    else:
        return {}
    return data
