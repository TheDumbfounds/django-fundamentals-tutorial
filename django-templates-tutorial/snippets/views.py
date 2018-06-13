from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def snippet_list(request):
    name = 'bob'
    is_expired = False
    return render(request, 'snippets/snippet_list.html', {'name': name, 'is_expired': is_expired})

def snippet_detail(request, id):
    return HttpResponse(f'snippet detail with the id of {id}')
