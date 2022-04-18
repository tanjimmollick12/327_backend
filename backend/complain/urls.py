from complain import views
from django.urls import path

urlpatterns = [
    path('createcomplain', views.createComplain.as_view(), name="createComplain"),
    path('complainlist', views.ComplainList.as_view(), name="ComplainList"),
    path('respcomplain/<int:complain_id>/', views.respComplain.as_view(), name="responseComplain"),
]
