from django.urls import path
from .views import CarListApiView,CarCreateApiView,CarEditApiView,CarDeleteApiView, CarDetailApiView, CarMixedApiView



urlpatterns=[
    path('cars/',CarListApiView.as_view(),name='cars'),
    path('cars/create/',CarCreateApiView.as_view(),name='cars_create'),
    path('cars/edit/<int:pk>/',CarEditApiView.as_view(),name='edit'),
    path('cars/delete/<int:pk>/',CarDeleteApiView.as_view(),name='car-delete'),
    path('cars/<int:pk>/', CarDetailApiView.as_view(), name='car_detail'),
    path('cars/mix/<int:pk>', CarMixedApiView.as_view(), name='car_mixed'),

]