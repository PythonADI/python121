from django.urls import path
from polls.views import home_view

urlpatterns = [
    path("", home_view)
]
