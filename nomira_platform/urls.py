from django.contrib import admin
from django.urls import path, include
from flask import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # كل روابط الموقع ستكون في main/urls.py
        path('_nested_admin/', include('nested_admin.urls')),

]
