from account import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('adduser',views.addUser.as_view(), name="adduser")

]
