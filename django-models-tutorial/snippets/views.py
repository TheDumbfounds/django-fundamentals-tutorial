from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet

def snippet_list(request):
    snippet_list = Snippet.objects.all()
    return render(request, 'snippets/snippet_list.html', {'snippet_list': snippet_list})

def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})
