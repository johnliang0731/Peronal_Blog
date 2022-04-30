from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.Project_List.as_view(), name='index'),
    path('<int:pk>', views.Project_DetailView.as_view(), name='detail'),
    path('create/', views.Create_Project.as_view(), name='create'),
    path('update/<int:pk>/', views.Project_UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.Project_DeleteView.as_view(), name='delete'),
    path('upload/<int:pk>/', views.model_form_upload, name='upload'),
    path('document/<int:pk>/delete/', views.document_delete, name='doc_delete'),
    ]
