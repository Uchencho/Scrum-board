from django.conf.urls import url

from .api import ListApi, CardApi
from django.urls import path, include


urlpatterns = [
    path('lists/', ListApi.as_view()),
    path('card/', CardApi.as_view()),
]