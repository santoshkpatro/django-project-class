from django.contrib import admin
from django.urls import path

from . import views
# from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about_us/', views.about_us),
]
