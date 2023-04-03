from django.urls import path

from . import views

from .views import RegisterView, LoginView, UserView, LogoutView, ValidateCodeView

urlpatterns = [
    path('', views.Home.__str__, name='form'),

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('codetotp', ValidateCodeView.as_view()),

    # path('login', views.LoginTest, name="LoginTest"),
    # path('user', views.UserTest, name="UserTest"),
    # path('logout', views.LogoutTest, name="LogoutTest"),
]