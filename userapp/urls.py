from django.urls import path
from.import views

app_name='auth'
urlpatterns = [
    path('register/',views.registerUser,name='register'),
    path('loginuser/',views.loginUser,name='loginuser'),
    path('logout/',views.logout,name='logout'),
]