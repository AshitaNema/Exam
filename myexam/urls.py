from django.contrib import admin
from django.urls import path, include
from .views import HomePage, Split
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage, name='homepage' ),
    path('step1', views.Split, name='step1'),
    
]