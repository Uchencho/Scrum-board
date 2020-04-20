from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .api import ListApi, CardApi
from .api import ListViewSet, CardViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'card', CardViewSet)

#urlpatterns = [
#    path('lists/', ListApi.as_view()),
#    path('card/', CardApi.as_view()),
#    path('home/', TemplateView.as_view(template_name='scrumboard/home.html')),
#]

urlpatterns = router.urls