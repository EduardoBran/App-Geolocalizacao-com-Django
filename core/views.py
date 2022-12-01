from django.shortcuts import render
from django.views.generic import View

from .utils import get_client_data, yelp_search


class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        items = []
        city = None
        
        # loop até encontrar um ip que tenha nome de cidade (alguns ips gerados aleatoriamente nao retornam nome de cidade)
        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']
        
        termo = request.GET.get('key', None) # termo
        loc = request.GET.get('loc', None) # localidade
        location = city
        
        context = {
            'city': city,
            'busca': False
        }
        
        if loc:
            location = loc
        if termo:
            items = yelp_search(keyword=termo, location=location)
            context = {
                'termo': termo,
                'items': items,
                'city': location,
                'busca': True
            }
        
        return render(request, 'index.html', context)