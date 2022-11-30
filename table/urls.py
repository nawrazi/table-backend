from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('table/1', views.PremierLeague.as_view(), name='table'),
    path('table/2', views.Championship.as_view(), name='table'),
    path('table/3', views.LaLiga.as_view(), name='table'),
    path('table/4', views.Bundesliga.as_view(), name='table'),
    path('table/5', views.League1.as_view(), name='table')
]
