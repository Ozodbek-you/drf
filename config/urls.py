from django.contrib import admin
from django.urls import path
from configapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',actor_get_post),
    # path('actor/<int:pk>/',actor_put,name = 'actor'),
    path('movie/',MovieApi.as_view()),
    path("movie/<int:pk>/",MovieDetailAPI.as_view()),
    path('movies/<int:start_year>/', MovieDataAPI.as_view()),
    path('movies/<int:start_year>/<int:end_year>/', MovieDataAPI.as_view()),
    path('movies/', MovieDataAPI.as_view()),
]
