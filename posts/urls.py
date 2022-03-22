from django.urls import path


from . import views 

app_name= 'post'

urlpatterns = [
    path('', views.Home,name='home'),
    path('todosposts/', views.PostList,name='lista'),
    path('<slug:slug>/', views.PostDetailView.as_view(),name='detail'),
]



