from django.urls import path
from . import views
app_name='lap'
urlpatterns = [
    path('',views.Home,name='home'),
    path('laps/',views.laps,name='laps'),
    path('<slug:c_slug>/',views.laps,name='product_by_category'),
    path('details/<int:id>',views.Details,name='details'),
    path('support/',views.support,name='support'),


]
