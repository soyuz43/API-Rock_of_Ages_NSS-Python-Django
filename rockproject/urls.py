# File Path: API-Rock_of_Ages_NSS-Python-Django/rockproject/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rockapi.views import TypeView, RockView  # ! Added import for RockView
from rockapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'types', TypeView, 'type')
router.register(r'rocks', RockView, 'rock')  # ! Registered RockView for '/rocks'

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
