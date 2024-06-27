"""
URL configuration for cer3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from backend.views import *

from backend.views import NumberViewSet, CreateRandomNumber, PokemonViewSet

router = DefaultRouter()
router.register(r'numbers', NumberViewSet)
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('random/', CreateRandomNumber.as_view(), name='create_random_number'),
    path('admin/', admin.site.urls),
]