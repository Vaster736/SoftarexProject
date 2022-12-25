
from django.urls import path
from . import views
from .views import LoginUser

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',LoginUser.as_view(), name='authopage'),
    path('aboutuser',views.aboutuser, name='aboutuser'),
    path('mainpage',views.PostFormMain.as_view(), name='main'),
    path('authopage',LoginUser.as_view(), name='authopage'),
    path('register',views.RegisterUser.as_view(), name='register'),
    path('exit',views.exit, name='exit'),
    path('addimage',views.addimage, name='addimage'),
    path('addtofile', views.addtofile, name='addtofile'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)