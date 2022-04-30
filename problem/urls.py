from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'problem'

urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("post/<int:pk>/",views.PostDetail.as_view(),name="postdetail"),
    path("post/<int:pk>/delete",views.DeletePost.as_view(),name="delete"),
    path("post/<int:pk>/update", views.post_status_change,name="update"),
    path("post/<int:pk>/highlight", views.post_status_highlight,name="highlight"),
    path("post/<int:pk>/upload", views.postform_upload, name='postupload'),
    path("post/<int:pk>/reply", views.create_reply_to_post, name='create_reply'),
    path("reply/<int:pk>/delete", views.DeleteReply.as_view(), name='removereply'),
    path("reply/<int:pk>/upload", views.replyform_upload, name='replyupload'),
    path('search/', views.PostSearch, name='search'),
    ]
