from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def snippet_list(request):
    print(reverse('snippets:list'))
    return HttpResponse('snippet list...')

def snippet_detail(request, id):
    return HttpResponse(f'snippet detail with the id of {id}')
