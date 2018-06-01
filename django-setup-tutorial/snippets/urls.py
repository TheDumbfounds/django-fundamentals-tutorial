
from django.urls import path, include
from . import views

app_name = 'snippets'
urlpatterns = [
    path('', views.snippet_list, name='list'),
    path('<int:id>/', views.snippet_detail, name='detail')
]
