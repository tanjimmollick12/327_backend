from complain import views
from django.urls import path

urlpatterns = [
    path('createcomplain', views.createComplain.as_view(), name="register")
]
