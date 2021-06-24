from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url

	path('orders/', views.orders, name="orders"),
	path('shipping/', views.shipping, name="shipping"),
	path('pickTicket/', views.pickTicket, name="pickTicket"),

	path('service/', views.service, name="service"),
	path('updateOrder/<str:pk>/', views.updateOrder, name="updateOrder"),
	path('serviceOrder/<str:pk>/', views.serviceOrder, name="serviceOrder"),


]