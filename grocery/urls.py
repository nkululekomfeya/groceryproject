from django.urls import path
from grocery.views import HomeView
from django.views.generic import TemplateView

urlpatterns=[
    path('',HomeView.as_view()),

]
