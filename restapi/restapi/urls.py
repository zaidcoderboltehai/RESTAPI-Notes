from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from firstapp.views import *

router = routers.DefaultRouter()
router.register('users', UserView)
router.register('accounts', AccountView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(router.urls))
]
