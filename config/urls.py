from django.contrib import admin
from django.urls import path
from configapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', Hello.as_view()),
    # path('api1/', Hello.post),
]
