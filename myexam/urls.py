from django.contrib import admin
from django.urls import path, include
from .views import HomePage, Split, Step3, Step2, Step4, Step5, Step6, Terminal
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage, name='homepage' ),
    path('step1', views.Split, name='step1'),
    path('step3', views.Step3, name='stept'),
    path('step2', views.Step2, name='step2'),
    path('step4', views.Step4),
    path('step5', views.Step5, name='step5'),
    path('step6', views.Step6),
    path('', views.Terminal, name='terminal'),
]