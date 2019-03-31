# We created this to give the specific app based (blog) urls that our overall
# project (my site) will use
from django.urls import path
from . import views

# post_list will be the view to see when hitting 127.0.0.1:8000/ since
# path is '' and you should go to this view
urlpatterns = [
                path('', views.post_list, name='post_list'),
                path('post/<int:pk>/', views.post_detail, name="post_detail"),
                path('post/new/', views.post_new, name='post_new'),
                path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
              ]
