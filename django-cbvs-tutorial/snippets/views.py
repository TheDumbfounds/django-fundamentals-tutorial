from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet
from django.views import View
from django.views.generic import ListView, DetailView


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'

    # Use the following snippet to override the context data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # access context dictionary here...
    #     return context


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'
