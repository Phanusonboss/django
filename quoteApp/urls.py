from django.urls import path
from quoteApp.views import displayQoute


urlpatterns = [
    path('quote/', displayQoute),
]