from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.TastListView.as_view(), name='list'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateTaskView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='delete'),

]