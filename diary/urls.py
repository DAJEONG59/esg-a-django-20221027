from importlib.resources import path
from django.urls import path
from diary import views

urlpatterns = [
    path('',views.diaryindex),
    path('<int:pk>/',views.dsingle_post_page),
    

]