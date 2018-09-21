from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)