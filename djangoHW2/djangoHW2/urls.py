"""djangoHW2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from clientManager.views import managerSignin, managerSignUp, clientSearch, add, delete, search, update


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^managerSignin/', managerSignin.as_view(), name="managerSignin"),
    url(r'^managerSignup/', managerSignUp.as_view(), name="managerSignup"),
    url(r'^clientSearch/', clientSearch.as_view(), name="clientSearch"),
    url(r'^add/', add.as_view(), name="add"),
    url(r'^search/', search.as_view(), name="search"),
    url(r'^update/', update.as_view(), name="update"),
    url(r'^delete/', delete.as_view(), name="delete"),
]
