"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addition/",views.AdditionView.as_view(),name="add"),
    path("subtraction/",views.SubtractionView.as_view(),name="subtraction"),
    path("multi/",views.MultiplicationView.as_view(),name="multiplication"),
    path("divi/",views.DivisionView.as_view(),name="division"),
    path("fact/",views.FactorialView.as_view(),name="factorial"),
    path("prime/",views.PrimeView.as_view(),name="prime"),
    path("palindrome/",views.PalindromeView.as_view(),name="palindrome"),
    path("armstrong/",views.ArmstrongView.as_view(),name="armstrong"),
    path("limit/",views.LimitView.as_view(),name="limit"),
    
    path("health/",views.HealthView.as_view(),name="health"),
    path("temp/",views.TemparatureView.as_view(),name="temp"),
    path("exponent/",views.ExponentView.as_view(),name="exponent"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("geo/",views.GeoView.as_view(),name="geo"),
    path("",views.HomeView.as_view(),name="home"),

]
