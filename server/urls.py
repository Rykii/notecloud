from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('signIn', views.signIn),
    path('home', views.home)
]