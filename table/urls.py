from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('table/', views.FetchTable.as_view(), name='table')
]
