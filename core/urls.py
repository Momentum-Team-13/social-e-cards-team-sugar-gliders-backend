"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ecards_api import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.getDankMeme),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('followers/', views.FollowersListCreate.as_view()),
    path('followers/<int:pk>', views.FollowersRemove.as_view()),
    path('ecards/', views.GreetingCardCreate.as_view()),
    path('ecards/me/', views.GreetingCardCreate.as_view()),
    path('ecards/<int:pk>', views.GreetingCardEdit.as_view()),
    path('users/', views.UserList.as_view()),
]

