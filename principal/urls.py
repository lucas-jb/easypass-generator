from django.conf import settings
from django.urls import path
from principal import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='principal'),
]