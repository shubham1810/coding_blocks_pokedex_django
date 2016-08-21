from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from random import shuffle
import time
import os

from search.models import Pokedex
from pokemon_data_file import pokemon_data


def search_pokemon(search_string, result_type='arr'):
    result_arr = []

    if search_string == '*' and result_type == 'dict':
        for key, value in pokemon_data.iteritems():
            result_arr.append(dict(name=key, image_url=value))
        return result_arr

    if search_string == '*' and result_type == 'arr':
        for key, value in pokemon_data.iteritems():
            result_arr.append([key, value])
        return result_arr

    for key, value in pokemon_data.iteritems():
        if key.lower().startswith(search_string.lower()):
            if result_type == 'arr':
                result_arr.append([key, value])

            elif result_type == 'dict':
                data_dict = dict(name=key, image_url=value)
                result_arr.append(data_dict)

    return result_arr


def srchlistjs(request):
    search_string = request.GET.get('searchstring') or ''
    context_dict = {'search_string': search_string, 'result_arr': search_pokemon(search_string,
                                                                                 result_type='dict')}

    return render(request, 'search/searchLISTJS.html', context_dict)


def srchredirect(request, search_string):
    context_dict = {'search_string': search_string, 'result_arr': search_pokemon(search_string,
                                                                                 result_type='dict')}

    return render(request, 'search/searchREDIRECT.html', context_dict)


def srchpost(request):
    search_string = request.POST.get("searchstring") or ''

    context_dict = {'search_string': search_string, 'result_arr': search_pokemon(search_string)}

    return render(request, 'search/searchPOST.html', context_dict)


def srchget(request):
    search_string = request.GET.get("searchstring") or ''

    context_dict = {'search_string': search_string, 'result_arr': search_pokemon(search_string)}

    return render(request, 'search/searchGET.html', context_dict)


def index(request):
    today_date = time.ctime()
    context_dict = {'date': today_date}

    list_dir = os.listdir(os.path.join(settings.STATIC_PATH,
                                       'images'))
    shuffle(list_dir)

    context_dict['list_dir'] = list_dir
    context_dict['pokedex'] = Pokedex.objects.all()

    return render(request, 'search/index.html', context_dict)


def random(request):
    list_dir = os.listdir(os.path.join(settings.STATIC_PATH, 'images'))
    shuffle(list_dir)
    context_dict = {'list_dir': list_dir}
    return render(request, 'search/random.html', context_dict)
