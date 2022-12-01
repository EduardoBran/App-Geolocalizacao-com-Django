from random import randint

import requests
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2, geoip2

# endereço da plataforma YELP que utilizamos para fazer
# as buscas com os nossos parâmetros
YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'


# vamos buscar através de uma palavra chave(keyword) uma localidade (location)
def yelp_search(keyword=None, location=None):
    headers = {"Authorization": "Bearer " + settings.YELP_API_KEY}
    
    if keyword and location:
        params = {'term': keyword, 'location': location}
    else:
        params = {'term': 'Pizzaria', 'location': 'Rio de Janeiro'}
    
    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    return r.json()


# o ip gerado automaticamente sendo passado para o geolocat
def get_client_data():
    g = GeoIP2()
    ip = get_random_ip()
    
    try:
        return g.city(ip)
    except geoip2.erros.AddressNotFoundError:
        return None

# gerando string separada cada elemento por .
# gera ips automaticamente
def get_random_ip():
    return '.'.join([str(randint(0, 255)) for x in range(4)])