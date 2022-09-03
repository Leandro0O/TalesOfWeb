from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('linguagens/', views.Linguagens,name='linguagens'),
    path('contato/', views.Email,name='email'),
    path('webdeveloper/', views.ProgramadorWeb,name='webdeveloper'),
    path('webdesign/', views.WebDesign,name='webdesign'),
    path('sobre/', views.Sobre,name='sobre'),
    path('', views.Home,name='home'),
    path('todosposts/', views.PostList,name='lista'),
    path('<slug:slug>/', views.PostDetailView.as_view(),name='detail'),
]