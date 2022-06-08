from django.urls import path
from . import views

# app_name = "hospital"

urlpatterns=[
    path('',views.home,name='home'),
    path('register/<str:pk>',views.register_user,name='register'),
    path('login/<str:pk>',views.login_user,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout_user,name='logout'),

]