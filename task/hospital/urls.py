from django.urls import path
from . import views

# app_name = "hospital"

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/<str:pk>', views.register_user, name='register'),
    path('login/<str:pk>', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('blog/', views.all_blog, name='blog'),
    path('create_blog/', views.blog_create, name='create-blog'),
    path('view-blog/', views.view_blog, name='view-blog'),
    path('update-blog/<str:pkk>', views.update_blog, name='update-blog'),
    path('delete-blog/<str:pkk>', views.delete_blog, name='delete-blog'),


]
