from django.conf.urls import url
from django.views.generic import TemplateView

from .api import ListApi, CardApi
from django.urls import path, include


urlpatterns = [
    path('lists/', ListApi.as_view()),
    path('card/', CardApi.as_view()),
    path('home/', TemplateView.as_view(template_name='scrumboard/home.html')),
]