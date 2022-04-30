from django.urls import path
from . import views

app_name = 'work_instruction'
urlpatterns = [
    path('', views.WIDocList.as_view(), name='index'),
    path('create/', views.WIDoc_upload, name='create_wi'),
    path('detail/<int:pk>', views.WIDocDetail.as_view(), name='detail'),
    path('revise/<int:pk>', views.WIDocRevise, name='create_revise'),
    path('update/<int:pk>', views.WIDoc_update, name='update'),
    path('search/', views.WISearch, name='search'),
    ]
