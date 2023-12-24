from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.home , name='homepage'),
   path('signup/', views.singup, name='signup'),
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('profile/pass_change',views.pass_change, name='pass_change'),
   path('profile/pass_change2',views.pass_change2, name='pass_change2'),
]
