from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
   path('signin',views.SigninView.as_view(),name='login'),
   path('user/home',views.user_home,name='userhome'),
   path('admin/home',views.admin_home,name='adminhome'),
   path('signout',views.signout,name='logout'),

]

