from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contactPage',contactPage,name="contactPage"),
    path('productPage',productPage,name="productPage"),
]
