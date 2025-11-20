from django.urls import path
from .views import CarListApiView,CarCreateApiView,CarEditApiView,CarDeleteApiView, CarDetailApiView, CarMixedApiView,BookDetailApiView,BookMixedApiView,BookListApiView,BookCreateApiView,BookDeleteApiView,BookEditApiView



urlpatterns=[
    path('cars/',CarListApiView.as_view(),name='cars'),
    path('cars/create/',CarCreateApiView.as_view(),name='cars_create'),
    path('cars/edit/<int:pk>/',CarEditApiView.as_view(),name='edit'),
    path('cars/delete/<int:pk>/',CarDeleteApiView.as_view(),name='car-delete'),
    path('cars/<int:pk>/', CarDetailApiView.as_view(), name='car_detail'),
    path('cars/<int:pk>', CarMixedApiView.as_view(), name='car_mixed'),
    #######
    path('book/',BookListApiView.as_view(),name='book'),
    path('book/create/',BookCreateApiView.as_view(),name='book_create'),
    path('book/edit/<int:pk>/',BookEditApiView.as_view(),name='edit'),
    path('book/delete/<int:pk>/',BookDeleteApiView.as_view(),name='book-delete'),
    path('book/<int:pk>/', BookDetailApiView.as_view(), name='book_detail'),
    path('book/<int:pk>', BookMixedApiView.as_view(), name='book_mixed'),
]