from django.urls import path
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views

urlpatterns = [
    path('', RedirectView.as_view(url='customers/', permanent=False)),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



