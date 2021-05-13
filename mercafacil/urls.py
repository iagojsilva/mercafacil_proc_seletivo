"""mercafacil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from contatos_varejo.views import ContatoVarejoViewSet
from contatos_macapa.views import ContatoMacapaViewSet

router = routers.DefaultRouter()
router.register('contato/varejo', ContatoVarejoViewSet, 'contato_varejo')
router.register('contato/macapa', ContatoMacapaViewSet, 'contato_macapa')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
