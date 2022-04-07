from zipfile import Path
from django.urls import path,include
from . import views


urlpatterns = [
   path('employee/',views.employe_form,  name = 'insert'),
   path('', views.employe_list, name = 'list'),
   path('<int:id>/', views.employe_form, name ='update'),
   path('delete/<int:id>/', views.employe_delete, name ='delete'),

   
]
