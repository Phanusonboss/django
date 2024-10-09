from django.contrib import admin
from django.urls import path
from templatesApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstTemplate/', views.renderTemplate),
    path('empInfo/',views.renderEmployee),
]
